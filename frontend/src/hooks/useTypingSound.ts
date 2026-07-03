// ============================================================
// useTypingSound - 键盘打字音效
// 基于 Earthworm 项目的 Web Audio API 方案
// ============================================================

"use client";

import { useCallback, useEffect, useRef } from "react";

const PLAY_INTERVAL_MS = 60; // 两次播放最小间隔

let audioCtxRef: AudioContext | null = null;
let audioBuffer: AudioBuffer | null = null;
let lastPlayTime = 0;
let initPromise: Promise<void> | null = null;

async function ensureAudioContext(): Promise<AudioContext> {
  if (!audioCtxRef) {
    // 在用户手势中创建 AudioContext 才能自动进入 running 状态
    audioCtxRef = new AudioContext();
  }
  if (audioCtxRef.state === "suspended") {
    await audioCtxRef.resume();
  }
  return audioCtxRef;
}

async function loadAudioBuffer(url: string): Promise<AudioBuffer> {
  const ctx = await ensureAudioContext();
  const response = await fetch(url);
  const arrayBuffer = await response.arrayBuffer();
  audioBuffer = await ctx.decodeAudioData(arrayBuffer);
  return audioBuffer;
}

function ensureAudio(): void {
  if (initPromise) return;
  initPromise = (async () => {
    try {
      await ensureAudioContext();
      await loadAudioBuffer("/sounds/typing.mp3");
      console.log("🔊 键盘音效初始化成功");
    } catch (e) {
      console.warn("🔇 键盘音效初始化失败:", e);
      audioBuffer = null;
    }
  })();
}

export function useTypingSound() {
  const keyboardSoundEnabled = useRef(true);

  useEffect(() => {
    // 从 localStorage 读取键盘音效开关
    const stored =
      typeof window !== "undefined"
        ? localStorage.getItem("keyboardSoundEnabled")
        : null;
    if (stored !== null) {
      keyboardSoundEnabled.current = stored !== "false";
    }
  }, []);

  const playTypingSound = useCallback(() => {
    if (!keyboardSoundEnabled.current) return;

    // 延迟初始化：首次按键时才创建 AudioContext（利用用户手势）
    ensureAudio();

    if (!audioBuffer) return;

    const now = Date.now();
    if (now - lastPlayTime < PLAY_INTERVAL_MS) return;
    lastPlayTime = now;

    try {
      if (!audioCtxRef) return;
      const source = audioCtxRef.createBufferSource();
      source.buffer = audioBuffer;
      source.connect(audioCtxRef.destination);
      source.start();
    } catch {
      // 播放失败静默处理
    }
  }, []);

  const checkPlayTypingSound = useCallback((e: KeyboardEvent) => {
    // 忽略修饰键
    if (e.altKey || e.ctrlKey || e.metaKey) return false;
    return (
      /^[a-zA-Z0-9]$/.test(e.key) ||
      ["Backspace", " ", "'"].includes(e.key)
    );
  }, []);

  const setKeyboardSoundEnabled = useCallback((enabled: boolean) => {
    keyboardSoundEnabled.current = enabled;
    if (typeof window !== "undefined") {
      localStorage.setItem("keyboardSoundEnabled", String(enabled));
    }
  }, []);

  return {
    playTypingSound,
    checkPlayTypingSound,
    setKeyboardSoundEnabled,
    isEnabled: keyboardSoundEnabled.current,
  };
}

// ---- 正确/错误提示音 ----

let rightAudio: HTMLAudioElement | null = null;
let errorAudio: HTMLAudioElement | null = null;

function getRightAudio(): HTMLAudioElement {
  if (!rightAudio) {
    rightAudio = new Audio("/sounds/right.mp3");
  }
  return rightAudio;
}

function getErrorAudio(): HTMLAudioElement {
  if (!errorAudio) {
    errorAudio = new Audio("/sounds/error.mp3");
  }
  return errorAudio;
}

export function usePlayTipSound() {
  const playRightSound = useCallback(() => {
    getRightAudio().play().catch(() => {});
  }, []);

  const playErrorSound = useCallback(() => {
    getErrorAudio().play().catch(() => {});
  }, []);

  return { playRightSound, playErrorSound };
}
