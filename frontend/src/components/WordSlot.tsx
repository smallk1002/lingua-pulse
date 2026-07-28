// ============================================================
// WordSlot - 单个单词槽渲染
// ============================================================

"use client";

import { memo } from "react";
import { motion } from "framer-motion";
import type { WordSlot as WordSlotType } from "@/lib/types";

interface WordSlotProps {
  slot: WordSlotType;
  showAnswer?: boolean;
  inFixMode?: boolean;
}

const statusStyles: Record<
  WordSlotType["status"],
  { textColor: string; borderColor: string; dash?: boolean }
> = {
  pending: { textColor: "text-gray-400", borderColor: "border-gray-500", dash: true },
  active: { textColor: "text-fuchsia-600", borderColor: "border-fuchsia-600" },
  correct: { textColor: "text-green-500", borderColor: "border-green-500" },
  incorrect: {
    textColor: "text-red-500",
    borderColor: "border-red-500",
  },
};

export const WordSlot = memo(function WordSlot({
  slot,
  showAnswer,
  inFixMode,
}: WordSlotProps) {
  const style = statusStyles[slot.status];
  const isIncorrect = slot.status === "incorrect";

  // 显示的文本
  const displayText =
    slot.status === "active" || slot.status === "incorrect"
      ? slot.userInput || (inFixMode ? "" : "")
      : slot.status === "correct"
        ? slot.userInput || slot.target
        : "";

  // 宽度提示（初级模式）
  const minWidth = `${Math.max(slot.target.length, 2)}ch`;

  const content = (
    <div
      className={`
        relative inline-flex items-center justify-center
        min-w-[2em] px-1 py-0.5 mx-0.5
        text-lg font-mono font-semibold
        border-b-2 transition-colors duration-150
        ${style.textColor} ${style.borderColor}
        ${slot.status === "active" ? "animate-pulse" : ""}
        ${style.dash ? "border-dashed" : "border-solid"}
      `}
      style={{ minWidth }}
    >
      {/* 显示内容 */}
      {slot.status === "active" ? (
        <>
          <span>{slot.userInput}</span>
          <span className="inline-block w-[2px] h-[1.2em] bg-fuchsia-600 ml-0.5 animate-pulse" />
        </>
      ) : slot.status === "incorrect" ? (
        <span>{slot.userInput || "\u00A0"}</span>
      ) : slot.status === "correct" ? (
        <span>{displayText}</span>
      ) : (
        // pending
        <span className="opacity-30">{showAnswer ? slot.target : "\u00A0\u00A0"}</span>
      )}

      {/* Fix 模式：显示正确答案 */}
      {showAnswer && slot.status === "incorrect" && (
        <span className="absolute -bottom-6 left-1/2 -translate-x-1/2 text-xs text-red-400 whitespace-nowrap">
          → {slot.target}
        </span>
      )}
    </div>
  );

  if (isIncorrect) {
    return (
      <motion.span
        animate={{ x: [0, -4, 4, -4, 4, 0] }}
        transition={{ duration: 0.4 }}
      >
        {content}
      </motion.span>
    );
  }

  return content;
});
