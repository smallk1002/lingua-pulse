// ============================================================
// 逐词发音工具 — 复用后端 edge-tts（微软语音）
// 点击单词 → /api/tts/synthesize → 缓存命中 → 即播
// 首次合成需等待后端生成，通过 canplaythrough 事件处理
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
    currentAudio.removeAttribute("src");
    currentAudio.load();
    currentAudio = null;
  }

  const audio = new Audio();
  audio.src = getTtsUrl(clean);
  currentAudio = audio;

  // 首次点击时后端可能需要合成音频，等数据就绪后再播放
  const tryPlay = () => {
    audio.play().catch(() => {
      // 如果立即播放失败（数据未就绪），等待 canplaythrough
      const onReady = () => {
        audio.removeEventListener("canplaythrough", onReady);
        audio.play().catch(() => {});
      };
      audio.addEventListener("canplaythrough", onReady);
    });
  };

  // 如果音频已缓存/就绪，直接播；否则等待加载
  if (audio.readyState >= 2) {
    // HAVE_CURRENT_DATA 以上，已经有足够数据
    audio.play().catch(() => {});
  } else {
    tryPlay();
  }
}
