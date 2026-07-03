"""
边缘 TTS 服务

使用 edge-tts 生成 MP3 音频。
缓存到 static/audio/ 目录。
"""

import hashlib
import os
import uuid

import edge_tts

from app.core.config import settings


VOICE_MAP = {
    "default": "en-US-AndrewNeural",
    "female": "en-US-JennyNeural",
    "british": "en-GB-RyanNeural",
    "british_f": "en-GB-SoniaNeural",
}


async def generate_audio(text: str, voice: str = "default", speed: str = "+0%") -> str:
    """
    生成 TTS 音频文件，返回相对 URL。

    缓存策略：按 text + voice + speed 的 hash 命名文件。
    """
    voice_id = VOICE_MAP.get(voice, voice)  # 不在 map 中则直接用原始 voice ID 透传
    text_hash = hashlib.md5(f"{text}{voice_id}{speed}".encode()).hexdigest()
    filename = f"{text_hash}.mp3"
    filepath = os.path.join(settings.AUDIO_DIR, filename)

    # 缓存命中
    if os.path.exists(filepath):
        return f"/api/tts/audio/{filename}"

    # 确保目录存在
    os.makedirs(settings.AUDIO_DIR, exist_ok=True)

    # 生成音频
    communicate = edge_tts.Communicate(text, voice_id, rate=speed)
    await communicate.save(filepath)

    return f"/api/tts/audio/{filename}"


async def generate_batch(
    texts: list[tuple[str, str]], voice: str = "default"
) -> list[dict]:
    """
    批量生成 TTS，返回 statement_id -> url 映射。

    Args:
        texts: [(statement_id, text), ...]
    """
    results = []
    for sid, text in texts:
        url = await generate_audio(text, voice)
        results.append({"statement_id": sid, "url": url})
    return results
