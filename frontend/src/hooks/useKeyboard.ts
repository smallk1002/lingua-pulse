// ============================================================
// useKeyboard - 全局快捷键（参照 earthworm 设计）
//
// 设计原则：
// 1. 使用 Ctrl/⌘ 组合键，不与字符输入冲突
// 2. input handler 拦截所有 Ctrl 键并 preventDefault
// 3. 全局 listener 处理 Ctrl 快捷键，无需 capture 阶段
// 4. 同时匹配 e.key 和 e.code，兼容不同键盘布局
// ============================================================

"use client";

import { useEffect, useCallback } from "react";
import { useGameStore } from "@/stores/gameStore";

/** 从 localStorage 读取用户自定义快捷键，回退默认值 */
function getShortcutKeys() {
  const defaults: Record<string, string> = {
    sound: "'",
    hint: ";",
    skip: ".",
    previous: ",",
    pause: "p",
  };
  try {
    const raw = localStorage.getItem("shortcutKeys");
    if (raw) {
      const stored = JSON.parse(raw);
      for (const key of Object.keys(defaults)) {
        let val = stored[key];
        if (typeof val === "string") {
          // 归一化：去掉前缀如 "ctrl+"、"meta+"、"command+"，只保留按键字符
          val = val.replace(/^(ctrl|command|meta|alt)\+/i, "");
          defaults[key] = val;
        }
      }
    }
  } catch { /* ignore */ }
  return defaults;
}

/** 同时检查 e.key 和 e.code，兼容 macOS/CJK 等键盘布局 */
function matchKey(e: KeyboardEvent, targetKey: string): boolean {
  if (e.key === targetKey) return true;

  const codeMap: Record<string, string> = {
    "'": "Quote",
    '"': "Quote",
    ";": "Semicolon",
    ":": "Semicolon",
    ".": "Period",
    ">": "Period",
    ",": "Comma",
    "<": "Comma",
    "p": "KeyP",
    "P": "KeyP",
  };
  return e.code === codeMap[targetKey];
}

export function useKeyboard() {
  const { status, toggleShowAnswer, pauseGame, resumeGame } = useGameStore();

  const handleGlobalKeyDown = useCallback(
    (e: KeyboardEvent) => {
      const keys = getShortcutKeys();
      const ctrl = e.ctrlKey || e.metaKey;

      // Ctrl+' — 播放发音
      if (ctrl && matchKey(e, keys.sound)) {
        e.preventDefault();
        window.dispatchEvent(new CustomEvent("play-tts"));
        return;
      }

      // Ctrl+; — 显示/隐藏答案提示
      if (ctrl && matchKey(e, keys.hint)) {
        e.preventDefault();
        toggleShowAnswer();
        return;
      }

      // Ctrl+. — 下一题
      if (ctrl && matchKey(e, keys.skip)) {
        e.preventDefault();
        const { nextStatement, status: gs } = useGameStore.getState();
        if (gs !== "completed") nextStatement();
        return;
      }

      // Ctrl+, — 上一题
      if (ctrl && matchKey(e, keys.previous)) {
        e.preventDefault();
        useGameStore.getState().prevStatement();
        return;
      }

      // Ctrl+p — 暂停/恢复
      if (ctrl && matchKey(e, keys.pause)) {
        e.preventDefault();
        if (status === "playing") pauseGame();
        else if (status === "paused") resumeGame();
        return;
      }

      // Escape — 暂停/恢复
      if (e.key === "Escape") {
        e.preventDefault();
        if (status === "playing") pauseGame();
        else if (status === "paused") resumeGame();
        return;
      }
    },
    [status, toggleShowAnswer, pauseGame, resumeGame]
  );

  useEffect(() => {
    // input handler 已拦截 Ctrl 键，所以用普通冒泡监听即可
    window.addEventListener("keydown", handleGlobalKeyDown);
    return () => window.removeEventListener("keydown", handleGlobalKeyDown);
  }, [handleGlobalKeyDown]);
}
