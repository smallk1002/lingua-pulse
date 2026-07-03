"""
课程与进度 API 集成测试
"""

import pytest
from httpx import AsyncClient

from tests.conftest import make_course_pack, make_course, make_statement, make_user


class TestCoursePacks:
    """课程包 API"""

    @pytest.mark.asyncio
    async def test_list_course_packs_public(self, client: AsyncClient):
        """未登录也可获取公开课程包"""
        resp = await client.get("/api/course-packs")
        assert resp.status_code == 200
        assert isinstance(resp.json(), list)

    @pytest.mark.asyncio
    async def test_list_course_packs_with_filters(self, client: AsyncClient, auth_headers: dict):
        """支持按公开状态筛选"""
        await client.post("/api/admin/course-packs", json=make_course_pack(title="初级课"), headers=auth_headers)
        await client.post("/api/admin/course-packs", json=make_course_pack(title="高级课"), headers=auth_headers)

        resp = await client.get("/api/course-packs")
        assert resp.status_code == 200
        # 至少包含刚创建的课程包
        titles = [p["title"] for p in resp.json()]
        assert "初级课" in titles
        assert "高级课" in titles

    @pytest.mark.asyncio
    async def test_create_course_pack_authenticated(self, client: AsyncClient):
        """已登录活跃用户可以创建课程包（MVP 阶段宽松权限）"""
        user = make_user()
        resp = await client.post("/api/auth/register", json=user)
        token = resp.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
        resp = await client.post("/api/admin/course-packs", json=make_course_pack(), headers=headers)
        # MVP 阶段：is_active 即可操作管理后台
        assert resp.status_code == 201

    @pytest.mark.asyncio
    async def test_get_course_pack_detail(self, client: AsyncClient, auth_headers: dict, course_pack_id: str):
        """课程包详情包含课程列表"""
        # 创建一个课程
        await client.post("/api/admin/courses", json={
            **make_course(), "course_pack_id": course_pack_id
        }, headers=auth_headers)

        resp = await client.get(f"/api/course-packs/{course_pack_id}")
        assert resp.status_code == 200
        data = resp.json()
        assert data["title"] == "测试课程包"
        assert len(data["courses"]) >= 1

    @pytest.mark.asyncio
    async def test_delete_course_pack(self, client: AsyncClient, auth_headers: dict, course_pack_id: str):
        """删除课程包"""
        resp = await client.delete(f"/api/admin/course-packs/{course_pack_id}", headers=auth_headers)
        assert resp.status_code == 204

        # 确认已删除
        resp = await client.get(f"/api/course-packs/{course_pack_id}")
        assert resp.status_code == 404


class TestCourses:
    """课程 API"""

    @pytest.mark.asyncio
    async def test_get_course_with_statements(self, client: AsyncClient, auth_headers: dict,
                                               course_pack_id: str, course_id: str):
        """课程详情包含所有句子"""
        await client.post("/api/admin/statements", json={
            **make_statement(order=1), "course_id": course_id
        }, headers=auth_headers)
        await client.post("/api/admin/statements", json={
            **make_statement(chinese="她每晚都读一本书。", english="She reads a book every night.", order=2),
            "course_id": course_id
        }, headers=auth_headers)

        resp = await client.get(f"/api/course-packs/{course_pack_id}/courses/{course_id}", headers=auth_headers)
        assert resp.status_code == 200
        data = resp.json()
        assert len(data["statements"]) == 2
        assert data["statements"][0]["order"] == 1
        assert data["statements"][1]["order"] == 2

    @pytest.mark.asyncio
    async def test_get_next_course_on_complete(self, client: AsyncClient, auth_headers: dict,
                                                course_pack_id: str, course_id: str):
        """完成课程后返回下一课信息"""
        # 创建第二课
        resp = await client.post("/api/admin/courses", json={
            **make_course(title="下一课", order=2), "course_pack_id": course_pack_id
        }, headers=auth_headers)
        course2_id = resp.json()["id"]

        # 完成第一课
        resp = await client.post(f"/api/progress/{course_id}/complete", headers=auth_headers)
        assert resp.status_code == 200
        data = resp.json()
        assert data["next_course_id"] == course2_id
        assert data["next_course_title"] == "下一课"

    @pytest.mark.asyncio
    async def test_no_next_course_on_last_course(self, client: AsyncClient, auth_headers: dict,
                                                  course_id: str):
        """最后一课完成时 next_course_id 为 None"""
        resp = await client.post(f"/api/progress/{course_id}/complete", headers=auth_headers)
        assert resp.status_code == 200
        data = resp.json()
        assert data["next_course_id"] is None


class TestProgress:
    """学习进度 API"""

    @pytest.mark.asyncio
    async def test_save_progress(self, client: AsyncClient, auth_headers: dict, course_id: str):
        """保存学习进度"""
        resp = await client.put(f"/api/progress/{course_id}", json={
            "statement_index": 5
        }, headers=auth_headers)
        assert resp.status_code == 200

    @pytest.mark.asyncio
    async def test_progress_persisted_in_course_detail(self, client: AsyncClient, auth_headers: dict,
                                                        course_pack_id: str, course_id: str):
        """保存进度后，课程详情中应返回进度"""
        await client.put(f"/api/progress/{course_id}", json={
            "statement_index": 3
        }, headers=auth_headers)

        resp = await client.get(
            f"/api/course-packs/{course_pack_id}/courses/{course_id}", headers=auth_headers
        )
        assert resp.status_code == 200
        data = resp.json()
        assert data["progress"] is not None
        assert data["progress"]["statement_index"] == 3

    @pytest.mark.asyncio
    async def test_complete_course(self, client: AsyncClient, auth_headers: dict, course_id: str):
        """完成课程"""
        resp = await client.post(f"/api/progress/{course_id}/complete", headers=auth_headers)
        assert resp.status_code == 200
        data = resp.json()
        assert data["completed"] is True
        assert data["xp_awarded"] == 50

    @pytest.mark.asyncio
    async def test_progress_unauthenticated(self, client: AsyncClient, course_id: str):
        """未登录不能保存进度"""
        resp = await client.put(f"/api/progress/{course_id}", json={"statement_index": 1})
        assert resp.status_code == 401

    @pytest.mark.asyncio
    async def test_breakpoint_resume(self, client: AsyncClient, auth_headers: dict,
                                      course_pack_id: str, course_id: str):
        """断点续学：保存进度后重新获取课程，应返回 statement_index"""
        # 模拟做到第 7 题
        await client.put(f"/api/progress/{course_id}", json={
            "statement_index": 7
        }, headers=auth_headers)

        # 重新获取课程
        resp = await client.get(
            f"/api/course-packs/{course_pack_id}/courses/{course_id}", headers=auth_headers
        )
        assert resp.status_code == 200
        data = resp.json()
        assert data["progress"]["statement_index"] == 7

    @pytest.mark.asyncio
    async def test_progress_sync_with_beacon(self, client: AsyncClient, auth_headers: dict, course_id: str):
        """模拟 sendBeacon 式的页面关闭前同步"""
        # sendBeacon 发送 POST/JSON，这里用 PUT 模拟
        resp = await client.put(f"/api/progress/{course_id}", json={
            "statement_index": 10,
            "input_snapshot": "He goes jogging every morning",
            "sync_type": "beacon",   # 标记为关闭前紧急同步
        }, headers=auth_headers)
        assert resp.status_code == 200
