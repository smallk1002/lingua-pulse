"""
边缘 TTS 服务

使用 edge-tts 实时生成 MP3 音频流。
不落磁盘，所有音频在内存中生成后直接返回。
"""

import asyncio
import io
import time
import threading
from collections import OrderedDict

import edge_tts


VOICE_MAP = {
    "default": "en-US-AndrewNeural",
    "female": "en-US-JennyNeural",
    "british": "en-GB-RyanNeural",
    "british_f": "en-GB-SoniaNeural",
}


# ── 轻量级内存缓存（LRU，上限 200 条） ──
# 注意：不存磁盘，仅做进程内热点缓存。重启即清空。
# 单个 MP3 约 20-50KB，200 条 ≈ 6-10MB，完全可接受。
_cache_lock = threading.Lock()
_cache: OrderedDict[str, tuple[float, bytes]] = OrderedDict()
_MAX_CACHE_SIZE = 200


def _cache_key(text: str, voice: str, speed: str) -> str:
    return f"{text}|{voice}|{speed}"


def _cache_get(text: str, voice: str, speed: str) -> bytes | None:
    key = _cache_key(text, voice, speed)
    with _cache_lock:
        if key in _cache:
            _cache.move_to_end(key)
            return _cache[key][1]
    return None


def _cache_set(text: str, voice: str, speed: str, data: bytes) -> None:
    key = _cache_key(text, voice, speed)
    with _cache_lock:
        if key in _cache:
            _cache.move_to_end(key)
            _cache[key] = (time.time(), data)
        else:
            _cache[key] = (time.time(), data)
            while len(_cache) > _MAX_CACHE_SIZE:
                _cache.popitem(last=False)


async def _stream_edge_tts(text: str, voice_id: str, speed: str) -> bytes:
    """
    调用 Edge TTS，将所有音频块收集到内存中返回 bytes。
    零磁盘写入。
    """
    communicate = edge_tts.Communicate(text, voice_id, rate=speed)
    audio_buffer = io.BytesIO()
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_buffer.write(chunk["data"])
    return audio_buffer.getvalue()


async def generate_audio_bytes(
    text: str,
    voice: str = "default",
    speed: str = "+15%",
) -> bytes:
    """
    生成 TTS 音频，返回 MP3 bytes。

    优先从内存缓存读取；未命中则实时生成。
    不写磁盘，纯内存操作。
    """
    voice_id = VOICE_MAP.get(voice, voice)

    # 内存缓存命中
    cached = _cache_get(text, voice_id, speed)
    if cached is not None:
        return cached

    # 实时生成
    data = await _stream_edge_tts(text, voice_id, speed)
    _cache_set(text, voice_id, speed, data)
    return data


# 兼容旧调用（返回 bytes 而非 URL）
async def generate_audio(text: str, voice: str = "default", speed: str = "+15%") -> bytes:
    """兼容旧接口：返回 MP3 bytes"""
    return await generate_audio_bytes(text, voice, speed)


async def generate_batch(
    texts: list[tuple[str, str]], voice: str = "default"
) -> list[dict]:
    """
    批量生成 TTS，并发请求，返回 statement_id -> bytes 映射。
    """
    tasks = [
        generate_audio_bytes(stmt_id, voice) for stmt_id, _ in texts
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return [
        {"statement_id": sid, "data": (r if not isinstance(r, Exception) else None)}
        for (sid, _), r in zip(texts, results)
    ]
