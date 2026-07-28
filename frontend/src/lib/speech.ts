// ============================================================
// 逐词发音工具 — 复用后端 edge-tts（微软语音）
// 点击单词 → /api/tts/synthesize → 缓存命中的 MP3 → 即播
// ============================================================

import { getTtsUrl } from "./api";

let currentAudio: HTMLAudioElement | null = null;

/**
 * 播放单个单词/短语（使用后端微软 TTS）
 * 自动停止前一个音频，点击即播
 */
export function speakWord(text: string): void {
  if (!text || typeof window === "undefined") return;

  // 清理标点，让 TTS 纯读单词
  const clean = text.replace(/[^\w\s'-]/g, "").trim();
  if (!clean) return;

  // 停止正在播放的音频
  if (currentAudio) {
    currentAudio.pause();
    currentAudio.currentTime = 0;
    currentAudio = null;
  }

  const audio = new Audio(getTtsUrl(clean));
  audio.play().catch(() => {
    // 音频可能还在加载中（首次请求需后端合成），静默忽略
  });
  currentAudio = audio;
}
