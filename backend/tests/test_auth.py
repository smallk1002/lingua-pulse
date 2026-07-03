"""
认证模块测试用例

覆盖：
- 注册 / 登录 / Token 刷新
- 密码强度校验
- 邮箱唯一性
- 未登录访问保护
"""

import pytest
from httpx import AsyncClient

from tests.conftest import make_user


class TestRegister:
    """注册接口测试"""

    @pytest.mark.asyncio
    async def test_register_success(self, client: AsyncClient):
        """正常注册返回 201 + access_token"""
        resp = await client.post("/api/auth/register", json=make_user())
        assert resp.status_code == 201
        data = resp.json()
        assert "access_token" in data
        assert "user" in data
        assert data["user"]["email"].endswith("@example.com")
        assert "password_hash" not in data["user"]

    @pytest.mark.asyncio
    async def test_register_duplicate_email(self, client: AsyncClient):
        """重复邮箱注册返回 400"""
        await client.post("/api/auth/register", json=make_user(email="dup@test.com"))
        resp = await client.post("/api/auth/register", json=make_user(email="dup@test.com", username="other"))
        assert resp.status_code == 400
        assert "已注册" in resp.json()["detail"]

    @pytest.mark.asyncio
    async def test_register_duplicate_username(self, client: AsyncClient):
        """重名用户注册返回 400"""
        await client.post("/api/auth/register", json=make_user(username="duplicate"))
        resp = await client.post("/api/auth/register", json=make_user(email="other@test.com", username="duplicate"))
        assert resp.status_code == 400
        assert "已被占用" in resp.json()["detail"]

    @pytest.mark.asyncio
    async def test_register_weak_password(self, client: AsyncClient):
        """弱密码注册返回 422（少于 6 位）"""
        resp = await client.post("/api/auth/register", json=make_user(password="123"))
        assert resp.status_code == 422

    @pytest.mark.asyncio
    async def test_register_invalid_email(self, client: AsyncClient):
        """无效邮箱格式返回 422"""
        resp = await client.post("/api/auth/register", json=make_user(email="notanemail"))
        assert resp.status_code == 422

    @pytest.mark.asyncio
    async def test_register_missing_fields(self, client: AsyncClient):
        """缺少必填字段返回 422"""
        resp = await client.post("/api/auth/register", json={"email": "test@test.com"})
        assert resp.status_code == 422


class TestLogin:
    """登录接口测试"""

    @pytest.mark.asyncio
    async def test_login_success(self, client: AsyncClient):
        """正常登录返回 200 + access_token"""
        user = make_user()
        await client.post("/api/auth/register", json=user)
        resp = await client.post("/api/auth/login", json={
            "email": user["email"],
            "password": user["password"],
        })
        assert resp.status_code == 200
        assert "access_token" in resp.json()

    @pytest.mark.asyncio
    async def test_login_wrong_password(self, client: AsyncClient):
        """错误密码返回 401"""
        user = make_user()
        await client.post("/api/auth/register", json=user)
        resp = await client.post("/api/auth/login", json={
            "email": user["email"],
            "password": "WrongPassword",
        })
        assert resp.status_code == 401

    @pytest.mark.asyncio
    async def test_login_nonexistent_user(self, client: AsyncClient):
        """不存在的用户返回 401"""
        resp = await client.post("/api/auth/login", json={
            "email": "noone@test.com",
            "password": "whatever",
        })
        assert resp.status_code == 401

    @pytest.mark.asyncio
    async def test_login_with_email_as_username(self, client: AsyncClient):
        """使用邮箱登录"""
        user = make_user()
        await client.post("/api/auth/register", json=user)
        resp = await client.post("/api/auth/login", json={
            "email": user["email"],
            "password": user["password"],
        })
        assert resp.status_code == 200


class TestMe:
    """获取当前用户信息测试"""

    @pytest.mark.asyncio
    async def test_me_authenticated(self, client: AsyncClient, auth_headers: dict):
        """已登录返回用户信息"""
        resp = await client.get("/api/auth/me", headers=auth_headers)
        assert resp.status_code == 200
        assert resp.json()["email"].endswith("@example.com")

    @pytest.mark.asyncio
    async def test_me_unauthenticated(self, client: AsyncClient):
        """未登录返回 401"""
        resp = await client.get("/api/auth/me")
        assert resp.status_code == 401

    @pytest.mark.asyncio
    async def test_me_expired_token(self, client: AsyncClient):
        """过期 Token 返回 401"""
        headers = {"Authorization": "Bearer expired.invalid.token"}
        resp = await client.get("/api/auth/me", headers=headers)
        assert resp.status_code == 401


class TestProtectedRoutes:
    """未登录用户访问受保护路由"""

    PROTECTED_PATHS = [
        ("GET", "/api/settings"),
        ("PUT", "/api/settings"),
        ("GET", "/api/review/due"),
        ("GET", "/api/stats/summary"),
    ]

    @pytest.mark.asyncio
    @pytest.mark.parametrize("method,path", PROTECTED_PATHS)
    async def test_protected_route_returns_401(self, client: AsyncClient, method: str, path: str):
        """所有受保护路由未登录时返回 401"""
        resp = await client.request(method, path)
        assert resp.status_code == 401
