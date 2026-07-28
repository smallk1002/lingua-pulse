// ============================================================
// 逐词发音工具 — 复用后端 edge-tts（微软语音）
// 点击单词 → /api/tts/synthesize → 缓存命中 → 即播
// ============================================================

import { getTtsUrl } from "./api";

let wordAudio: HTMLAudioElement | null = null;

/**
 * 播放单个单词/短语（使用后端微软 TTS）
 * 复用一个 Audio 元素，行为与整句播放保持一致
 */
export function speakWord(text: string): void {
  if (!text || typeof window === "undefined") return;

  // 清理标点，让 TTS 纯读单词
  const clean = text.replace(/[^\w\s'-]/g, "").trim();
  if (!clean) return;

  if (!wordAudio) {
    wordAudio = new Audio();
  }

  const url = getTtsUrl(clean);
  wordAudio.pause();
  wordAudio.src = url;
  wordAudio.currentTime = 0;

  // 加载失败时打印原因，方便排查
  wordAudio.onerror = () => {
    console.error("[speakWord] 音频加载失败:", url, clean);
  };

  const playPromise = wordAudio.play();
  if (playPromise !== undefined) {
    playPromise.catch((err) => {
      console.error("[speakWord] 播放失败:", err, "word:", clean, "url:", url);
    });
  }
}
