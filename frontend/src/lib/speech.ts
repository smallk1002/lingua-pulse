// ============================================================
// 逐词发音工具 — 复用后端 edge-tts（微软语音）
// 每次点击创建新 Audio 元素，click 用户手势直接触发
// ============================================================

import { getTtsUrl } from "./api";

/** 当前正在播放的 Audio（用于取消） */
let currentAudio: HTMLAudioElement | null = null;

/**
 * 播放单个单词（使用后端微软 TTS）
 * 每次创建全新 Audio 元素，确保 click 用户手势能触发浏览器自动播放策略。
 */
export function speakWord(text: string): void {
  if (!text || typeof window === "undefined") return;

  // 清理标点，让 TTS 纯读单词
  const clean = text.replace(/[^\w\s'-]/g, "").trim();
  if (!clean) return;

  // 停止上一次播放
  if (currentAudio) {
    currentAudio.pause();
    currentAudio = null;
  }

  const url = getTtsUrl(clean);
  console.log("[speakWord]", clean, url);

  // 直接 new Audio + click 手势 → 浏览器允许播放
  const audio = new Audio(url);
  currentAudio = audio;

  audio.play().then(() => {
    console.log("[speakWord] 播放成功:", clean);
  }).catch((e) => {
    console.error("[speakWord] 播放失败:", clean, e.message);
  });

  // 播放完/出错后清引用
  audio.onended = () => { currentAudio = null; };
  audio.onerror = () => { currentAudio = null; };
}
