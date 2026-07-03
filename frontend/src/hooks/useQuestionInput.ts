// ============================================================
// useQuestionInput - 逐词输入核心逻辑
// ============================================================

"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import type { WordSlot } from "@/lib/types";
import { useGameStore } from "@/stores/gameStore";

export function useQuestionInput() {
  const inputRef = useRef<HTMLInputElement>(null);
  const {
    wordSlots,
    fixSlots,
    phase,
    isComposing,
    isLastWord,
    mode,
    setWordSlots,
    setComposing,
    setIsLastWord,
    submitAnswer,
  } = useGameStore();

  const [isFocused, setIsFocused] = useState(true);

  // ---- 聚焦控制 ----

  const focusInput = useCallback(() => {
    inputRef.current?.focus();
    setIsFocused(true);
  }, []);

  // 挂载时自动聚焦（DOM 就绪后）
  useEffect(() => {
    const timer = setTimeout(() => focusInput(), 100);
    return () => clearTimeout(timer);
  }, [focusInput]);

  // 切换题目时自动聚焦
  const { currentStatementIndex } = useGameStore();
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

  // ---- 单词槽辅助 ----

  const getActiveSlotIndex = useCallback((): number => {
    const slots = phase === "fix" ? fixSlots : wordSlots;
    return slots.findIndex((s) => s.status === "active");
  }, [phase, wordSlots, fixSlots]);

  // ---- 空格切换到下一词 ----

  const advanceToNextSlot = useCallback(
    (slots: WordSlot[]): WordSlot[] => {
      const activeIdx = slots.findIndex((s) => s.status === "active");
      if (activeIdx === -1 || activeIdx === slots.length - 1) {
        setIsLastWord(true);
        return slots;
      }
      const newSlots = slots.map((s, i) => {
        if (i === activeIdx) return { ...s, status: "correct" as const };
        if (i === activeIdx + 1) return { ...s, status: "active" as const };
        return s;
      });
      setIsLastWord(activeIdx + 1 === slots.length - 1);
      return newSlots;
    },
    [setIsLastWord]
  );

  // ---- 退格 ----

  const handleBackspace = useCallback(
    (slots: WordSlot[]): WordSlot[] => {
      const activeIdx = slots.findIndex((s) => s.status === "active");
      if (activeIdx === -1) return slots;

      if (slots[activeIdx].userInput.length > 0) {
        // 删除当前单词的最后一个字符
        return slots.map((s, i) =>
          i === activeIdx
            ? { ...s, userInput: s.userInput.slice(0, -1) }
            : s
        );
      } else if (activeIdx > 0) {
        // 当前已清空 → 回退到上一个单词
        setIsLastWord(false);
        return slots.map((s, i) => {
          if (i === activeIdx) return { ...s, status: "pending" as const };
          if (i === activeIdx - 1)
            return {
              ...s,
              status: "active" as const,
              userInput: s.userInput.slice(0, -1),
            };
          return s;
        });
      }
      return slots;
    },
    [setIsLastWord]
  );

  // ---- 字符输入 ----

  const handleCharacterInput = useCallback(
    (slots: WordSlot[], char: string): WordSlot[] => {
      if (char === " ") {
        return advanceToNextSlot(slots);
      }

      const activeIdx = slots.findIndex((s) => s.status === "active");
      if (activeIdx === -1) return slots;

      return slots.map((s, i) =>
        i === activeIdx ? { ...s, userInput: s.userInput + char } : s
      );
    },
    [advanceToNextSlot]
  );

  // ---- 键盘事件处理器 ----

  const handleKeyDown = useCallback(
    (e: React.KeyboardEvent<HTMLInputElement>) => {
      // Ctrl+Backspace — 删除整个单词（在 Ctrl 拦截之前）
      if (e.key === "Backspace" && (e.ctrlKey || e.metaKey)) {
        e.preventDefault();
        if (phase === "fix") {
          const activeIdx = fixSlots.findIndex((s) => s.status === "active");
          if (activeIdx !== -1) {
            const newFixSlots = fixSlots.map((s, i) =>
              i === activeIdx ? { ...s, userInput: "" } : s
            );
            useGameStore.setState({ fixSlots: newFixSlots });
          }
        } else {
          const activeIdx = wordSlots.findIndex((s) => s.status === "active");
          if (activeIdx !== -1) {
            const newSlots = wordSlots.map((s, i) =>
              i === activeIdx ? { ...s, userInput: "" } : s
            );
            setWordSlots(newSlots);
          }
        }
        return;
      }

      // 🔑 Ctrl/⌘ 组合键全部交给全局快捷键处理，input 不处理
      //    （参照 Earthworm：避免输入法将预输入字符上屏）
      if (e.ctrlKey || e.metaKey) {
        e.preventDefault();
        return;
      }

      // Answer 阶段 — 空格或 Enter 推进到下一题
      if (phase === "answer") {
        if (e.key === " " || e.key === "Enter") {
          e.preventDefault();
          const { nextStatement, status: gameStatus } =
            useGameStore.getState();
          if (gameStatus !== "completed") {
            nextStatement();
          }
        }
        return;
      }
      // 禁止方向键
      if (
        ["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"].includes(e.key)
      ) {
        e.preventDefault();
        return;
      }

      // Enter 提交
      if (e.key === "Enter" && !isComposing) {
        e.preventDefault();
        submitAnswer();
        return;
      }

      // Backspace
      if (e.key === "Backspace") {
        e.preventDefault();
        if (phase === "fix") {
          const newFixSlots = handleBackspace(fixSlots);
          useGameStore.setState({ fixSlots: newFixSlots });
        } else {
          const newSlots = handleBackspace(wordSlots);
          setWordSlots(newSlots);
        }
        return;
      }

      // 空格
      if (e.key === " ") {
        e.preventDefault();
        if (isLastWord) {
          submitAnswer();
          return;
        }
        if (phase === "fix") {
          const newFixSlots = advanceToNextSlot(fixSlots);
          useGameStore.setState({ fixSlots: newFixSlots });
        } else {
          const newSlots = advanceToNextSlot(wordSlots);
          setWordSlots(newSlots);
        }
        return;
      }

      // 普通字符输入
      if (e.key.length === 1) {
        e.preventDefault();
        if (phase === "fix") {
          const newFixSlots = handleCharacterInput(fixSlots, e.key);
          useGameStore.setState({ fixSlots: newFixSlots });
        } else {
          const newSlots = handleCharacterInput(wordSlots, e.key);
          setWordSlots(newSlots);
        }
      }
    },
    [
      isComposing,
      isLastWord,
      phase,
      wordSlots,
      fixSlots,
      setWordSlots,
      submitAnswer,
      handleBackspace,
      handleCharacterInput,
      advanceToNextSlot,
    ]
  );

  // ---- 失焦/聚焦 ----

  const onBlur = useCallback(() => {
    setIsFocused(false);
  }, []);

  const onFocus = useCallback(() => {
    setIsFocused(true);
  }, []);

  // ---- 中文输入法兼容 ----

  const onCompositionStart = useCallback(() => {
    setComposing(true);
  }, [setComposing]);

  const onCompositionEnd = useCallback(() => {
    setComposing(false);
  }, [setComposing]);

  return {
    inputRef,
    isFocused,
    handleKeyDown,
    focusInput,
    onBlur,
    onFocus,
    onCompositionStart,
    onCompositionEnd,
    getActiveSlotIndex,
  };
}
