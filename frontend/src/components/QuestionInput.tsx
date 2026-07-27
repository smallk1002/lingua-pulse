// ============================================================
// QuestionInput - 逐词输入主组件
// ============================================================

"use client";

import { useCallback, useState } from "react";
import { useGameStore } from "@/stores/gameStore";
import { useQuestionInput } from "@/hooks/useQuestionInput";
import { useTypingSound } from "@/hooks/useTypingSound";
import { WordSlot } from "./WordSlot";

import { GrammarBreakdown } from "./GrammarBreakdown";
import { MoreExamples } from "./MoreExamples";

export function QuestionInput() {
  const {
    wordSlots,
    fixSlots,
    phase,
    showAnswer,
    status,
    mode,
    difficulty,
    getCurrentStatement,
  } = useGameStore();

  const {
    inputRef,
    isFocused,
    handleKeyDown,
    focusInput,
    onBlur,
    onFocus,
    onCompositionStart,
    onCompositionEnd,
  } = useQuestionInput();

  const { playTypingSound, checkPlayTypingSound } = useTypingSound();

  const statement = getCurrentStatement();

  // 更多例句展开状态
  const [showMoreExamples, setShowMoreExamples] = useState(false);
  // 语法分析折叠状态
  const [showGrammar, setShowGrammar] = useState(true);

  // 带音效的键盘处理
  const onKeyDown = useCallback(
    (e: React.KeyboardEvent<HTMLInputElement>) => {
      if (checkPlayTypingSound(e.nativeEvent)) {
        playTypingSound();
      }
      handleKeyDown(e);
    },
    [handleKeyDown, playTypingSound, checkPlayTypingSound]
  );

  if (!statement) return null;

  // Fix 模式下显示完整 wordSlots，并合并 fixSlots 的 userInput
  const displaySlots =
    phase === "fix"
      ? wordSlots.map((s) => {
          const fixSlot = fixSlots.find((f) => f.id === s.id);
          return fixSlot ? { ...s, userInput: fixSlot.userInput } : s;
        })
      : wordSlots;

  return (
    <div className="w-full max-w-3xl mx-auto">
      {/* 中文提示 */}
      {mode === "chinese_to_english" && phase !== "answer" && (
        <div className="text-center mb-6">
          <p className="text-2xl font-bold text-gray-800 dark:text-gray-100">
            {statement.chinese}
          </p>
        </div>
      )}

      {mode === "dictation" && phase !== "answer" && (
        <div className="text-center mb-6">
          <button
            onClick={() => window.dispatchEvent(new CustomEvent("play-tts"))}
            className="text-4xl hover:scale-110 transition-transform"
            title="播放发音"
          >
            🔊
          </button>
        </div>
      )}

      {/* 单词槽 */}
      <div
        className={`
          relative flex flex-wrap justify-center gap-1 py-8 px-4
          min-h-[6em] items-center
          rounded-xl
          ${phase === "fix" ? "bg-red-50 dark:bg-red-950/30 border-2 border-red-200 dark:border-red-800" : ""}
        `}
        onClick={focusInput}
      >
        {phase === "fix" && (
          <div className="w-full text-center mb-2 text-red-500 font-medium text-sm">
            🔧 Fix 修复模式 — 只修改标红的错误单词
          </div>
        )}

        {displaySlots.map((slot) => (
          <WordSlot
            key={slot.id}
            slot={slot}
            showAnswer={showAnswer}
            inFixMode={phase === "fix"}
          />
        ))}
      </div>

      {/* 隐藏的输入框 */}
      <input
        ref={inputRef}
        type="text"
        lang="en"
        autoComplete="off"
        autoCorrect="off"
        autoCapitalize="off"
        spellCheck={false}
        className="absolute inset-0 w-full h-full opacity-0 cursor-default"
        onKeyDown={onKeyDown}
        onBlur={onBlur}
        onFocus={onFocus}
        onCompositionStart={onCompositionStart}
        onCompositionEnd={onCompositionEnd}
        disabled={status !== "playing"}
      />

      {/* 操作按钮栏：按钮 + 快捷键提示 */}
      {phase === "question" && (
        <div className="flex justify-center items-center gap-2 mt-4 px-2">
          <button
            onClick={() => useGameStore.getState().toggleShowAnswer()}
            className="flex items-center gap-1.5 px-3 py-1.5 text-sm rounded-lg border border-gray-200 dark:border-gray-700
                       text-gray-500 hover:text-fuchsia-600 hover:border-fuchsia-300
                       dark:hover:text-fuchsia-400 dark:hover:border-fuchsia-700 transition-colors"
            title="显示/隐藏答案"
          >
            <kbd className="text-[10px] px-1 py-0.5 rounded bg-gray-100 dark:bg-gray-800 text-gray-400 font-mono">Ctrl+;</kbd>
            <span>提示</span>
          </button>
          <button
            onClick={() => window.dispatchEvent(new CustomEvent("play-tts"))}
            className="flex items-center gap-1.5 px-3 py-1.5 text-sm rounded-lg border border-gray-200 dark:border-gray-700
                       text-gray-500 hover:text-fuchsia-600 hover:border-fuchsia-300
                       dark:hover:text-fuchsia-400 dark:hover:border-fuchsia-700 transition-colors"
            title="播放发音"
          >
            <kbd className="text-[10px] px-1 py-0.5 rounded bg-gray-100 dark:bg-gray-800 text-gray-400 font-mono">Ctrl+'</kbd>
            <span>发音</span>
          </button>
          <button
            onClick={() => useGameStore.getState().pauseGame()}
            className="flex items-center gap-1.5 px-3 py-1.5 text-sm rounded-lg border border-gray-200 dark:border-gray-700
                       text-gray-500 hover:text-fuchsia-600 hover:border-fuchsia-300
                       dark:hover:text-fuchsia-400 dark:hover:border-fuchsia-700 transition-colors"
            title="暂停"
          >
            <kbd className="text-[10px] px-1 py-0.5 rounded bg-gray-100 dark:bg-gray-800 text-gray-400 font-mono">Esc</kbd>
            <span>暂停</span>
          </button>
        </div>
      )}

      {/* ====== Answer 阶段 ====== */}
      {phase === "answer" && statement && (
        <div className="mt-6 space-y-6">
          {/* 完整英文句子（大号展示） */}
          <div className="text-center">
            <p className="text-3xl md:text-4xl font-bold text-gray-800 dark:text-gray-100 leading-relaxed">
              {statement.english}
            </p>
            <button
              onClick={() => window.dispatchEvent(new CustomEvent("play-tts"))}
              className="inline-block ml-2 text-xl hover:scale-110 transition-transform"
              title="播放发音"
            >
              🔊
            </button>
          </div>

          {/* 音标 */}
          {statement.soundmark && (
            <div className="text-center">
              <p className="text-lg text-gray-500 font-mono">
                {statement.soundmark}
              </p>
            </div>
          )}

          {/* 中文翻译 */}
          <div className="text-center">
            <p className="text-xl text-gray-600 dark:text-gray-400">
              {statement.chinese}
            </p>
          </div>

          {/* 语法分析（可折叠） */}
          <div className="border border-gray-200 dark:border-gray-800 rounded-xl overflow-hidden">
            <button
              onClick={() => setShowGrammar(!showGrammar)}
              className="w-full flex items-center justify-between px-4 py-3 bg-gray-50 dark:bg-gray-900
                         hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
            >
              <span className="text-sm font-medium text-gray-600 dark:text-gray-400">
                📖 语法分析
              </span>
              <span className="text-gray-400 text-sm">
                {showGrammar ? "▲" : "▼"}
              </span>
            </button>
            {showGrammar && (
              <div className="p-4">
                <GrammarBreakdown
                  english={statement.english}
                  soundmark={statement.soundmark}
                  chinese={statement.chinese}
                  grammar={
                    statement.grammar as
                      | Array<{ tag?: string; text?: string; role?: string }>
                      | null
                  }
                />
              </div>
            )}
          </div>

          {/* 操作按钮 */}
          <div className="flex justify-center gap-3 flex-wrap">
            <button
              onClick={() => {
                useGameStore.getState().retryStatement();
                setShowMoreExamples(false);
                setTimeout(() => focusInput(), 100);
              }}
              className="flex items-center gap-2 px-6 py-3 border-2 border-gray-300 dark:border-gray-700
                         rounded-xl font-semibold hover:border-fuchsia-400 hover:text-fuchsia-600
                         transition-colors"
            >
              <span>🔄</span>
              <span>再来一次</span>
            </button>
            <button
              onClick={() => setShowMoreExamples(!showMoreExamples)}
              className="flex items-center gap-2 px-6 py-3 border-2 border-gray-300 dark:border-gray-700
                         rounded-xl font-semibold hover:border-purple-400 hover:text-purple-600
                         transition-colors"
            >
              <span>📚</span>
              <span>{showMoreExamples ? "收起例句" : "更多例句"}</span>
            </button>
            <button
              onClick={() => {
                const { nextStatement, status: gameStatus } = useGameStore.getState();
                setShowMoreExamples(false);
                if (gameStatus !== "completed") {
                  nextStatement();
                  setTimeout(() => focusInput(), 100);
                }
              }}
              className="flex items-center gap-2 px-8 py-3 bg-fuchsia-600 text-white rounded-xl
                         font-semibold hover:bg-fuchsia-700 transition-colors shadow-lg hover:shadow-xl
                         active:scale-95"
            >
              <span>下一题</span>
              <span>→</span>
            </button>
          </div>

          <p className="text-center text-xs text-gray-400">下一题: Ctrl+Enter | 发音: Ctrl+'</p>

          {/* 更多例句展开区域 */}
          {showMoreExamples && (
            <MoreExamples
              statementId={statement.id}
              onClose={() => setShowMoreExamples(false)}
            />
          )}
        </div>
      )}

      {/* Fix 模式的提交按钮 */}
      {phase === "fix" && (
        <div className="text-center mt-6">
          <button
            onClick={() => {
              const { submitAnswer: submit } = useGameStore.getState();
              submit();
              setTimeout(() => focusInput(), 100);
            }}
            className="px-8 py-3 bg-orange-500 text-white rounded-xl font-semibold
                       hover:bg-orange-600 transition-colors shadow-lg hover:shadow-xl
                       active:scale-95"
          >
            🔧 确认修复
          </button>
          <p className="text-xs text-gray-400 mt-2">或按 Enter</p>
        </div>
      )}
    </div>
  );
}
