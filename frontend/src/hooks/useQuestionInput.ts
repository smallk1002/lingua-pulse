// ============================================================
// useQuestionInput - 逐词输入核心逻辑
// 性能优化：handleKeyDown 内通过 getState() 读取最新状态，
// 避免将 wordSlots/fixSlots 作为 useCallback 依赖导致
// 每次按键回调重建 + input 元素重渲染
// ============================================================

"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import type { WordSlot } from "@/lib/types";
import { useGameStore } from "@/stores/gameStore";

export function useQuestionInput() {
  const inputRef = useRef<HTMLInputElement>(null);

  // 只订阅 actions（引用稳定），不订阅频繁变化的状态
  const setWordSlots = useGameStore((s) => s.setWordSlots);
  const setComposing = useGameStore((s) => s.setComposing);
  const setIsLastWord = useGameStore((s) => s.setIsLastWord);
  const submitAnswer = useGameStore((s) => s.submitAnswer);

  const [isFocused, setIsFocused] = useState(true);

  // ---- 聚焦控制 ----

  const focusInput = useCallback(() => {
    inputRef.current?.focus();
    setIsFocused(true);
  }, []);

  // 挂载时自动聚焦
  useEffect(() => {
    const timer = setTimeout(() => focusInput(), 100);
    return () => clearTimeout(timer);
  }, [focusInput]);

  // 切换题目时自动聚焦
  const currentStatementIndex = useGameStore((s) => s.currentStatementIndex);
  useEffect(() => {
    const timer = setTimeout(() => focusInput(), 50);
    return () => clearTimeout(timer);
  }, [currentStatementIndex, focusInput]);

  // 窗口/标签页切回来重新聚焦
  useEffect(() => {
    const onFocus = () => {
      const { status } = useGameStore.getState();
      if (status === "playing") {
        setTimeout(() => {
          inputRef.current?.focus();
          setIsFocused(true);
        }, 100);
      }
    };
    window.addEventListener("focus", onFocus);
    document.addEventListener("visibilitychange", () => {
      if (document.visibilityState === "visible") onFocus();
    });
    return () => {
      window.removeEventListener("focus", onFocus);
      document.removeEventListener("visibilitychange", onFocus);
    };
  }, []);

  // ---- 键盘事件处理器（核心） ----
  // 直接通过 getState() 读取最新状态，不通过闭包依赖
  const handleKeyDown = useCallback(
    (e: React.KeyboardEvent<HTMLInputElement>) => {
      const state = useGameStore.getState();
      const { wordSlots, fixSlots, phase, isComposing, isLastWord } = state;
      const slots = phase === "fix" ? fixSlots : wordSlots;
      const activeIdx = slots.findIndex((s) => s.status === "active");

      // Ctrl+Backspace — 删除整个单词（在 Ctrl 拦截之前）
      if (e.key === "Backspace" && (e.ctrlKey || e.metaKey)) {
        e.preventDefault();
        if (activeIdx === -1) return;
        const updated = slots.map((s, i) =>
          i === activeIdx ? { ...s, userInput: "" } : s
        );
        if (phase === "fix") useGameStore.setState({ fixSlots: updated });
        else setWordSlots(updated);
        return;
      }

      // Ctrl/⌘ 组合键 — 全部交给全局快捷键处理
      if (e.ctrlKey || e.metaKey) {
        e.preventDefault();
        return;
      }

      // Answer 阶段 — 空格/Enter 推进下一题
      if (phase === "answer") {
        if (e.key === " " || e.key === "Enter") {
          e.preventDefault();
          const { nextStatement, status: gs } = useGameStore.getState();
          if (gs !== "completed") nextStatement();
        }
        return;
      }

      // 禁止方向键
      if (["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"].includes(e.key)) {
        e.preventDefault();
        return;
      }

      // Enter 提交
      if (e.key === "Enter" && !isComposing) {
        e.preventDefault();
        submitAnswer();
        return;
      }

      // Backspace 退格
      if (e.key === "Backspace") {
        e.preventDefault();
        if (activeIdx === -1) return;

        if (slots[activeIdx].userInput.length > 0) {
          // 删除当前单词最后一个字符
          const updated = slots.map((s, i) =>
            i === activeIdx ? { ...s, userInput: s.userInput.slice(0, -1) } : s
          );
          if (phase === "fix") useGameStore.setState({ fixSlots: updated });
          else setWordSlots(updated);
        } else if (activeIdx > 0) {
          // 当前已清空 → 回退到上一个单词
          setIsLastWord(false);
          const updated = slots.map((s, i) => {
            if (i === activeIdx) return { ...s, status: "pending" as const };
            if (i === activeIdx - 1)
              return {
                ...s,
                status: "active" as const,
                userInput: s.userInput.slice(0, -1),
              };
            return s;
          });
          if (phase === "fix") useGameStore.setState({ fixSlots: updated });
          else setWordSlots(updated);
        }
        return;
      }

      // 空格 — 切换到下一词
      if (e.key === " ") {
        e.preventDefault();
        if (isLastWord) {
          submitAnswer();
          return;
        }
        if (activeIdx === -1 || activeIdx === slots.length - 1) {
          setIsLastWord(true);
          return;
        }
        const nextIsLast = activeIdx + 1 === slots.length - 1;
        const updated = slots.map((s, i) => {
          if (i === activeIdx) return { ...s, status: "correct" as const };
          if (i === activeIdx + 1) return { ...s, status: "active" as const };
          return s;
        });
        setIsLastWord(nextIsLast);
        if (phase === "fix") useGameStore.setState({ fixSlots: updated });
        else setWordSlots(updated);
        return;
      }

      // 普通字符输入
      if (e.key.length === 1) {
        e.preventDefault();
        if (activeIdx === -1) return;
        const updated = slots.map((s, i) =>
          i === activeIdx ? { ...s, userInput: s.userInput + e.key } : s
        );
        if (phase === "fix") useGameStore.setState({ fixSlots: updated });
        else setWordSlots(updated);
      }
    },
    [setWordSlots, setIsLastWord, submitAnswer]
  );

  // ---- 失焦/聚焦 ----
  const onBlur = useCallback(() => setIsFocused(false), []);
  const onFocus = useCallback(() => setIsFocused(true), []);

  // ---- 中文输入法兼容 ----
  const onCompositionStart = useCallback(
    () => setComposing(true),
    [setComposing]
  );
  const onCompositionEnd = useCallback(
    () => setComposing(false),
    [setComposing]
  );

  return {
    inputRef,
    isFocused,
    handleKeyDown,
    focusInput,
    onBlur,
    onFocus,
    onCompositionStart,
    onCompositionEnd,
  };
}
