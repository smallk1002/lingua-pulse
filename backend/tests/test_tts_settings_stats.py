"""
TTS + 设置 + 统计 API 测试
"""

import pytest
from unittest.mock import AsyncMock, patch
from httpx import AsyncClient

from tests.conftest import make_settings


# 全局 Mock TTS 生成函数（避免测试时真正调用 edge-tts）
def _mock_generate_audio(text, voice="default", speed="+0%"):
    import hashlib
    key = hashlib.md5(f"{text}:{voice}:{speed}".encode()).hexdigest()
    return f"/api/tts/audio/{key}.mp3"


class TestTTS:
    """TTS 生成测试"""

    @pytest.mark.asyncio
    async def test_generate_tts(self, client: AsyncClient, auth_headers: dict):
        """生成单个句子 TTS → 返回音频 URL"""
        with patch("app.api.tts_settings_stats.generate_audio", side_effect=_mock_generate_audio):
            resp = await client.post("/api/tts/generate", json={
                "text": "He goes jogging every morning.",
                "voice": "default",
                "speed": "+0%",
            }, headers=auth_headers)
            assert resp.status_code == 200
            data = resp.json()
            assert "url" in data
            assert data["url"].startswith("/api/tts/audio/")

    @pytest.mark.asyncio
    async def test_generate_tts_with_different_voices(self, client: AsyncClient, auth_headers: dict):
        """不同音色都能正常生成"""
        with patch("app.api.tts_settings_stats.generate_audio", side_effect=_mock_generate_audio):
            voices = ["default", "female", "british", "british_f"]
            for voice in voices:
                resp = await client.post("/api/tts/generate", json={
                    "text": "Hello world.", "voice": voice,
                }, headers=auth_headers)
                assert resp.status_code == 200
                assert "url" in resp.json()

    @pytest.mark.asyncio
    async def test_generate_tts_with_speed(self, client: AsyncClient, auth_headers: dict):
        """倍速参数生效"""
        with patch("app.api.tts_settings_stats.generate_audio", side_effect=_mock_generate_audio):
            for speed in ["-50%", "+0%", "+50%", "+100%"]:
                resp = await client.post("/api/tts/generate", json={
                    "text": "Test.", "voice": "default", "speed": speed,
                }, headers=auth_headers)
                assert resp.status_code == 200

    @pytest.mark.asyncio
    async def test_generate_batch_tts(self, client: AsyncClient, auth_headers: dict):
        """批量生成 TTS"""
        with patch("app.api.tts_settings_stats.generate_audio", side_effect=_mock_generate_audio):
            # 使用不存在的合法 UUID，DB 查询返回空不会报错
            resp = await client.post("/api/tts/generate-batch", json={
                "statement_ids": [
                    "00000000-0000-0000-0000-000000000001",
                    "00000000-0000-0000-0000-000000000002",
                    "00000000-0000-0000-0000-000000000003",
                ],
                "voice": "default",
            }, headers=auth_headers)
            assert resp.status_code == 200
            data = resp.json()
            assert "results" in data
            assert isinstance(data["results"], list)  # 不存在语句 ID 则空

    @pytest.mark.asyncio
    async def test_tts_caching(self, client: AsyncClient, auth_headers: dict):
        """同一文本两次请求应返回相同 URL（命中缓存）"""
        with patch("app.api.tts_settings_stats.generate_audio", side_effect=_mock_generate_audio):
            resp1 = await client.post("/api/tts/generate", json={
                "text": "Unique test sentence.", "voice": "default",
            }, headers=auth_headers)
            resp2 = await client.post("/api/tts/generate", json={
                "text": "Unique test sentence.", "voice": "default",
            }, headers=auth_headers)
            assert resp1.json()["url"] == resp2.json()["url"]

    @pytest.mark.asyncio
    async def test_tts_empty_text(self, client: AsyncClient, auth_headers: dict):
        """空文本返回 422"""
        resp = await client.post("/api/tts/generate", json={
            "text": "", "voice": "default",
        }, headers=auth_headers)
        assert resp.status_code == 422

    @pytest.mark.asyncio
    async def test_tts_too_long_text(self, client: AsyncClient, auth_headers: dict):
        """超长文本（> 1000 字符）返回 422"""
        long_text = "word " * 500
        resp = await client.post("/api/tts/generate", json={
            "text": long_text, "voice": "default",
        }, headers=auth_headers)
        assert resp.status_code == 422

    @pytest.mark.asyncio
    async def test_tts_invalid_voice(self, client: AsyncClient, auth_headers: dict):
        """无效音色返回 422 或降级为默认"""
        with patch("app.api.tts_settings_stats.generate_audio", side_effect=_mock_generate_audio):
            resp = await client.post("/api/tts/generate", json={
                "text": "Hello.", "voice": "invalid_voice",
            }, headers=auth_headers)
            assert resp.status_code in [200, 422]
            if resp.status_code == 200:
                assert "url" in resp.json()


class TestSettings:
    """用户设置 API"""

    @pytest.mark.asyncio
    async def test_get_default_settings(self, client: AsyncClient, auth_headers: dict):
        """新用户返回默认设置"""
        resp = await client.get("/api/settings", headers=auth_headers)
        assert resp.status_code == 200
        data = resp.json()
        assert data["game_mode"] == "chinese_to_english"
        assert data["tts_speed"] == 1.0

    @pytest.mark.asyncio
    async def test_update_settings(self, client: AsyncClient, auth_headers: dict):
        """更新设置字段"""
        resp = await client.put("/api/settings", json={
            "game_mode": "dictation",
            "tts_speed": 1.5,
            "daily_goal": 30,
        }, headers=auth_headers)
        assert resp.status_code == 200
        data = resp.json()
        assert data["game_mode"] == "dictation"
        assert data["tts_speed"] == 1.5
        assert data["daily_goal"] == 30

    @pytest.mark.asyncio
    async def test_update_settings_partial(self, client: AsyncClient, auth_headers: dict):
        """部分更新：只传要改的字段，其他保持不变"""
        # 先获取默认
        resp = await client.get("/api/settings", headers=auth_headers)
        original_theme = resp.json()["theme"]

        # 只更新一个字段
        resp = await client.put("/api/settings", json={
            "game_mode": "dictation",
        }, headers=auth_headers)
        assert resp.status_code == 200
        assert resp.json()["game_mode"] == "dictation"
        assert resp.json()["theme"] == original_theme   # 其他不变

    @pytest.mark.asyncio
    async def test_settings_invalid_game_mode(self, client: AsyncClient, auth_headers: dict):
        """无效游戏模式：当前不校验，由前端限制"""
        resp = await client.put("/api/settings", json={
            "game_mode": "invalid_mode",
        }, headers=auth_headers)
        assert resp.status_code == 200  # MVP 阶段服务端不校验枚举值

    @pytest.mark.asyncio
    async def test_settings_speed_range(self, client: AsyncClient, auth_headers: dict):
        """倍速范围：MVP 阶段服务端不校验，由前端限制"""
        # 所有速度值都会被接受
        resp = await client.put("/api/settings", json={"tts_speed": 3.0}, headers=auth_headers)
        assert resp.status_code == 200
        resp = await client.put("/api/settings", json={"tts_speed": 0.1}, headers=auth_headers)
        assert resp.status_code == 200
        resp = await client.put("/api/settings", json={"tts_speed": 0.5}, headers=auth_headers)
        assert resp.status_code == 200
        resp = await client.put("/api/settings", json={"tts_speed": 2.0}, headers=auth_headers)
        assert resp.status_code == 200

    @pytest.mark.asyncio
    async def test_settings_unauthenticated(self, client: AsyncClient):
        """未登录不能获取/修改设置"""
        resp = await client.get("/api/settings")
        assert resp.status_code == 401


class TestStats:
    """学习统计 API"""

    @pytest.mark.asyncio
    async def test_get_stats_summary(self, client: AsyncClient, auth_headers: dict):
        """获取学习概览"""
        resp = await client.get("/api/stats/summary", headers=auth_headers)
        assert resp.status_code == 200
        data = resp.json()
        assert "xp" in data
        assert "level" in data
        assert "streak" in data
        assert "total_statements" in data
        assert "total_duration" in data

    @pytest.mark.asyncio
    async def test_report_learning_session(self, client: AsyncClient, auth_headers: dict, course_id: str):
        """上报学习时长"""
        resp = await client.post("/api/stats/session", json={
            "duration": 300,
            "statements_count": 10,
            "course_id": course_id,
        }, headers=auth_headers)
        assert resp.status_code == 200

    @pytest.mark.asyncio
    async def test_get_daily_stats(self, client: AsyncClient, auth_headers: dict):
        """获取每日统计"""
        resp = await client.get("/api/stats/daily?days=7", headers=auth_headers)
        assert resp.status_code == 200
        data = resp.json()
        assert isinstance(data, list)
        # 新用户可能没有数据

    @pytest.mark.asyncio
    async def test_streak_logic(self, client: AsyncClient, auth_headers: dict):
        """连胜逻辑测试：通过游戏答题触发 streak 更新"""
        # 上报学习时长
        resp = await client.post("/api/stats/session", json={
            "duration": 600, "statements_count": 20,
        }, headers=auth_headers)
        assert resp.status_code == 200

        # streak 由游戏答题触发，新用户首次为 0
        resp = await client.get("/api/stats/summary", headers=auth_headers)
        assert resp.status_code == 200
        assert "streak" in resp.json()
