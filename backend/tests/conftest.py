"""
共享 Fixtures 和测试辅助工具
"""

import uuid
import pytest
import pytest_asyncio
from datetime import datetime, timedelta
from httpx import AsyncClient, ASGITransport

# ============================================================
# 测试数据工厂（每次调用生成唯一数据，避免冲突）
# ============================================================

_counter = 0

def _unique_suffix():
    global _counter
    _counter += 1
    return f"{uuid.uuid4().hex[:8]}{_counter}"

def make_user(email=None, username=None, password="Test123456"):
    suffix = _unique_suffix()
    return {
        "email": email or f"test{suffix}@example.com",
        "username": username or f"testuser{suffix}",
        "password": password,
    }


def make_course_pack(title="测试课程包", description="测试描述", is_public=True):
    return {
        "title": title,
        "description": description,
        "is_public": is_public,
    }


def make_course(title="测试课程", description="测试课程描述", order=1):
    return {
        "title": title,
        "description": description,
        "order": order,
    }


def make_statement(chinese="他每天早上都去跑步。", english="He goes jogging every morning.",
                   soundmark="/hi ɡoʊz ˈdʒɑɡɪŋ ˈɛvri ˈmɔrnɪŋ/",
                   grammar=None, order=1):
    if grammar is None:
        grammar = [
            {"text": "He", "role": "S"},
            {"text": "goes", "role": "V"},
            {"text": "jogging", "role": "V"},
            {"text": "every", "role": "A"},
            {"text": "morning", "role": "A"},
        ]
    return {
        "chinese": chinese,
        "english": english,
        "soundmark": soundmark,
        "grammar": grammar,
        "order": order,
    }


def make_settings(game_mode="chinese_to_english", auto_next=False, space_submit=True,
                  tts_voice="default", tts_speed=1.0, tts_play_count=2, tts_interval=3,
                  theme="dark", font_size="medium", daily_goal=20):
    return {
        "game_mode": game_mode,
        "auto_next": auto_next,
        "space_submit": space_submit,
        "shortcut_keys": {"showAnswer": "ctrl+h", "playSound": "ctrl+j", "markMastered": "ctrl+m"},
        "tts_voice": tts_voice,
        "tts_speed": tts_speed,
        "tts_play_count": tts_play_count,
        "tts_interval": tts_interval,
        "theme": theme,
        "font_size": font_size,
        "daily_goal": daily_goal,
    }


def make_stats(xp=0, level=1, streak=0, longest_streak=0,
               total_statements=0, total_duration=0):
    return {
        "xp": xp,
        "level": level,
        "streak": streak,
        "longest_streak": longest_streak,
        "total_statements": total_statements,
        "total_duration": total_duration,
    }


# ============================================================
# HTTP 客户端 Fixture
# ============================================================

@pytest_asyncio.fixture
async def client() -> AsyncClient:
    """创建测试 HTTP 客户端"""
    from app.main import app
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


# ============================================================
# 邮件验证码 Mock（测试不真实发邮，捕获验证码供注册使用）
# ============================================================

_captured_codes: dict[str, str] = {}


@pytest.fixture(autouse=True)
def mock_email(monkeypatch):
    """全局 mock 邮件发送，并把最近一次验证码存入 _captured_codes"""
    from app.api import auth as auth_module
    from app.services.email_service import build_code_email as real_build

    async def fake_send_email(to, subject, html):
        pass

    def capturing_build(app_name, code, minutes):
        subject, html = real_build(app_name, code, minutes)
        _captured_codes["last"] = code
        return subject, html

    monkeypatch.setattr(auth_module, "send_email", fake_send_email)
    monkeypatch.setattr(auth_module, "build_code_email", capturing_build)
    yield


async def register_with_code(client: AsyncClient, user_data: dict):
    """完整验证码注册流程：发送验证码 → 携带验证码注册"""
    resp = await client.post("/api/auth/send-code", json={"email": user_data["email"]})
    assert resp.status_code == 200, f"发送验证码失败: {resp.text}"
    code = _captured_codes["last"]
    return await client.post("/api/auth/register", json={**user_data, "code": code})


# ============================================================
# 认证 Token Fixture
# ============================================================

@pytest_asyncio.fixture
async def auth_headers(client: AsyncClient):
    """注册用户并返回带 JWT 的请求头"""
    resp = await register_with_code(client, make_user())
    assert resp.status_code == 201, f"注册失败: {resp.text}"
    token = resp.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


# ============================================================
# 课程数据 Fixture
# ============================================================

@pytest_asyncio.fixture
async def course_pack_id(client: AsyncClient, auth_headers: dict):
    """创建课程包并返回 ID"""
    resp = await client.post("/api/admin/course-packs", json=make_course_pack(), headers=auth_headers)
    return resp.json()["id"]


@pytest_asyncio.fixture
async def course_id(client: AsyncClient, auth_headers: dict, course_pack_id: str):
    """创建课程并返回 ID"""
    resp = await client.post("/api/admin/courses", json={
        **make_course(), "course_pack_id": course_pack_id
    }, headers=auth_headers)
    return resp.json()["id"]


@pytest_asyncio.fixture
async def statement_id(client: AsyncClient, auth_headers: dict, course_id: str):
    """创建句子并返回 ID"""
    resp = await client.post("/api/admin/statements", json={
        **make_statement(), "course_id": course_id
    }, headers=auth_headers)
    return resp.json()["id"]


# ============================================================
# Mock 辅助
# ============================================================

class MockTTSService:
    """Mock TTS 服务，避免测试时真正调用 edge-tts"""

    async def generate(self, text: str, voice: str = "default", speed: str = "+0%"):
        return "/api/tts/audio/mock_abc123.mp3"

    async def generate_batch(self, statement_ids: list, voice: str = "default"):
        return [{"statement_id": sid, "url": f"/api/tts/audio/mock_{sid[:8]}.mp3"} for sid in statement_ids]

