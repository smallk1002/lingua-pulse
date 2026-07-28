// ============================================================
// GrammarBreakdown - 语法分析色块视图
// 逐词展示音标、语法角色(S/V/O/A)、中文释义，色块标注
// ============================================================

"use client";

import { speakWord } from "@/lib/speech";

interface WordAnalysis {
  text: string;
  soundmark?: string;
  tag?: string;      // 词性标签（旧格式兼容）
  role?: string;     // 语法角色: S/V/O/A/Lv/C
  phonetic?: string;  // Earthworm 格式音标
  chinese?: string;   // 逐词中文释义
}

// 语法角色 → 中文标签
const ROLE_LABELS: Record<string, string> = {
  S: "主",
  V: "谓",
  O: "宾",
  A: "状",
  Lv: "系动",
  C: "补",
  P: "表",
  OC: "宾补",
  Adv: "副",
  Adj: "形",
  Conj: "连",
  Neg: "否定",
  Art: "冠",
  Aux: "助动",
  Det: "限定",
  Int: "感叹",
};

// 角色色板
const ROLE_COLORS: Record<string, { bg: string; border: string; text: string }> = {
  S:   { bg: "bg-orange-50 dark:bg-orange-950/30",  border: "border-orange-300 dark:border-orange-700", text: "text-orange-700 dark:text-orange-300" },
  V:   { bg: "bg-pink-50 dark:bg-pink-950/30",       border: "border-pink-300 dark:border-pink-700",       text: "text-pink-700 dark:text-pink-300" },
  O:   { bg: "bg-blue-50 dark:bg-blue-950/30",       border: "border-blue-300 dark:border-blue-700",       text: "text-blue-700 dark:text-blue-300" },
  A:   { bg: "bg-violet-50 dark:bg-violet-950/30",   border: "border-violet-300 dark:border-violet-700",   text: "text-violet-700 dark:text-violet-300" },
  Lv:  { bg: "bg-cyan-50 dark:bg-cyan-950/30",       border: "border-cyan-300 dark:border-cyan-700",       text: "text-cyan-700 dark:text-cyan-300" },
  C:   { bg: "bg-green-50 dark:bg-green-950/30",     border: "border-green-300 dark:border-green-700",     text: "text-green-700 dark:text-green-300" },
  P:   { bg: "bg-amber-50 dark:bg-amber-950/30",     border: "border-amber-300 dark:border-amber-700",     text: "text-amber-700 dark:text-amber-300" },
  OC:  { bg: "bg-lime-50 dark:bg-lime-950/30",       border: "border-lime-300 dark:border-lime-700",       text: "text-lime-700 dark:text-lime-300" },
  Adv: { bg: "bg-sky-50 dark:bg-sky-950/30",         border: "border-sky-300 dark:border-sky-700",         text: "text-sky-700 dark:text-sky-300" },
  Adj: { bg: "bg-rose-50 dark:bg-rose-950/30",       border: "border-rose-300 dark:border-rose-700",       text: "text-rose-700 dark:text-rose-300" },
  Conj:{ bg: "bg-teal-50 dark:bg-teal-950/30",        border: "border-teal-300 dark:border-teal-700",       text: "text-teal-700 dark:text-teal-300" },
  Neg: { bg: "bg-red-50 dark:bg-red-950/30",         border: "border-red-300 dark:border-red-700",         text: "text-red-700 dark:text-red-300" },
  Art: { bg: "bg-indigo-50 dark:bg-indigo-950/30",   border: "border-indigo-300 dark:border-indigo-700",   text: "text-indigo-700 dark:text-indigo-300" },
  Aux: { bg: "bg-fuchsia-50 dark:bg-fuchsia-950/30", border: "border-fuchsia-300 dark:border-fuchsia-700", text: "text-fuchsia-700 dark:text-fuchsia-300" },
  Det: { bg: "bg-emerald-50 dark:bg-emerald-950/30", border: "border-emerald-300 dark:border-emerald-700", text: "text-emerald-700 dark:text-emerald-300" },
  Int: { bg: "bg-yellow-50 dark:bg-yellow-950/30",   border: "border-yellow-300 dark:border-yellow-700",   text: "text-yellow-700 dark:text-yellow-300" },
};

const TAG_COLORS: Record<string, { bg: string; border: string; text: string }> = {
  "代词":   { bg: "bg-orange-50 dark:bg-orange-950/30",  border: "border-orange-300 dark:border-orange-700", text: "text-orange-700 dark:text-orange-300" },
  "动词":   { bg: "bg-pink-50 dark:bg-pink-950/30",       border: "border-pink-300 dark:border-pink-700",       text: "text-pink-700 dark:text-pink-300" },
  "名词":   { bg: "bg-blue-50 dark:bg-blue-950/30",       border: "border-blue-300 dark:border-blue-700",       text: "text-blue-700 dark:text-blue-300" },
  "限定词": { bg: "bg-cyan-50 dark:bg-cyan-950/30",       border: "border-cyan-300 dark:border-cyan-700",       text: "text-cyan-700 dark:text-cyan-300" },
  "介词":   { bg: "bg-amber-50 dark:bg-amber-950/30",     border: "border-amber-300 dark:border-amber-700",     text: "text-amber-700 dark:text-amber-300" },
  "副词":   { bg: "bg-lime-50 dark:bg-lime-950/30",       border: "border-lime-300 dark:border-lime-700",       text: "text-lime-700 dark:text-lime-300" },
  "形容词": { bg: "bg-violet-50 dark:bg-violet-950/30",   border: "border-violet-300 dark:border-violet-700",   text: "text-violet-700 dark:text-violet-300" },
  "连词":   { bg: "bg-rose-50 dark:bg-rose-950/30",       border: "border-rose-300 dark:border-rose-700",       text: "text-rose-700 dark:text-rose-300" },
};

const DEFAULT_COLORS = [
  { bg: "bg-orange-50 dark:bg-orange-950/20",  border: "border-orange-200 dark:border-orange-800", text: "text-orange-600 dark:text-orange-300" },
  { bg: "bg-pink-50 dark:bg-pink-950/20",       border: "border-pink-200 dark:border-pink-800",       text: "text-pink-600 dark:text-pink-300" },
  { bg: "bg-blue-50 dark:bg-blue-950/20",       border: "border-blue-200 dark:border-blue-800",       text: "text-blue-600 dark:text-blue-300" },
  { bg: "bg-green-50 dark:bg-green-950/20",     border: "border-green-200 dark:border-green-800",     text: "text-green-600 dark:text-green-300" },
  { bg: "bg-purple-50 dark:bg-purple-950/20",   border: "border-purple-200 dark:border-purple-800",   text: "text-purple-600 dark:text-purple-300" },
];

interface GrammarBreakdownProps {
  english: string;
  soundmark?: string | null;
  chinese: string;
  grammar?: Array<{
    tag?: string;
    text?: string;
    role?: string;
    phonetic?: string;
    chinese?: string;
  }> | null;
}

/** 从 soundmark 字符串中提取各单词音标 */
function extractPerWordSoundmarks(soundmark: string, wordCount: number): string[] {
  const matches = soundmark.match(/\/[^/]+\//g);
  if (matches && matches.length === wordCount) {
    return matches;
  }
  const parts = soundmark.split(/\s+/).filter(Boolean);
  return parts.length === wordCount ? parts : [];
}

/** 解析 grammar 数据为逐词分析数组 */
function parseGrammar(
  english: string,
  grammar?: Array<{ tag?: string; text?: string; role?: string; phonetic?: string; chinese?: string }> | null
): WordAnalysis[] {
  if (grammar && Array.isArray(grammar) && grammar.length > 0) {
    return grammar.map((g) => ({
      text: g.text || "",
      tag: g.tag,
      role: g.role,
      soundmark: g.phonetic ? g.phonetic.replace(/^\//, "").replace(/\/$/, "").replace(/ \//g, "·").replace(/\//g, "") : undefined,
      chinese: g.chinese,
    }));
  }
  const words = english.split(/\s+/);
  return words.map((w) => ({ text: w }));
}

export function GrammarBreakdown({ english, soundmark, chinese, grammar }: GrammarBreakdownProps) {
  const words = english.split(/\s+/).filter(Boolean);
  const analyses = parseGrammar(english, grammar);
  const perWordSoundmarks = soundmark ? extractPerWordSoundmarks(soundmark, words.length) : [];

  // 合并：grammar 数据优先，soundmark 回退
  const items: WordAnalysis[] = analyses.map((a, i) => ({
    ...a,
    soundmark: a.soundmark || (perWordSoundmarks[i]?.replace(/^\//, "").replace(/\/$/, "") || undefined),
  }));

  // 如果 grammar 数据不足，补齐
  while (items.length < words.length) {
    items.push({
      text: words[items.length],
      soundmark: perWordSoundmarks[items.length]?.replace(/^\//, "").replace(/\/$/, ""),
    });
  }

  return (
    <div className="mt-4 space-y-4">
      {/* 逐词色块 */}
      <div className="flex flex-wrap items-center justify-center gap-2">
        {items.map((item, i) => {
          const roleLabel = item.role ? ROLE_LABELS[item.role] : null;

          // 颜色优先级：role > tag > 默认循环
          let colors = DEFAULT_COLORS[i % DEFAULT_COLORS.length];
          if (item.role && ROLE_COLORS[item.role]) {
            colors = ROLE_COLORS[item.role];
          } else if (item.tag && TAG_COLORS[item.tag]) {
            colors = TAG_COLORS[item.tag];
          }

          return (
            <button
              key={i}
              type="button"
              onClick={() => speakWord(item.text)}
              title={`点击发音: ${item.text}`}
              className={`flex flex-col items-center px-3 py-2 rounded-xl border min-w-[3em] cursor-pointer transition-all duration-150 hover:scale-105 hover:shadow-md active:scale-95 group ${colors.bg} ${colors.border}`}
            >
              {/* 音标 */}
              {item.soundmark && (
                <span className="text-[10px] text-gray-400 font-mono mb-0.5">
                  /{item.soundmark}/
                </span>
              )}

              {/* 英文单词 */}
              <span className={`text-lg font-bold ${colors.text} group-hover:underline`}>
                {item.text}
              </span>

              {/* 词性标签（兼容旧数据） */}
              {item.tag && !item.role && (
                <span className="text-[10px] text-gray-500 mt-0.5 bg-white/60 dark:bg-white/10 px-1.5 py-px rounded-full">
                  {item.tag}
                </span>
              )}

              {/* 中文释义 */}
              {item.chinese && (
                <span className="text-[10px] text-gray-500 mt-0.5">
                  {item.chinese}
                </span>
              )}
            </button>
          );
        })}
      </div>

      {/* S V A O 结构条 */}
      {items.some((i) => i.role) && (
        <div className="flex flex-wrap items-center justify-center gap-2">
          {items.map((item, i) => {
            const label = item.role ? ROLE_LABELS[item.role] || item.role : null;
            const colors = item.role && ROLE_COLORS[item.role]
              ? ROLE_COLORS[item.role]
              : DEFAULT_COLORS[i % DEFAULT_COLORS.length];

            return (
              <div
                key={i}
                className={`text-xs font-medium px-2 py-0.5 rounded ${colors.bg} ${colors.text} border ${colors.border}`}
              >
                {label || "—"}
              </div>
            );
          })}
        </div>
      )}

      {/* 中文翻译 */}
      <div className="text-center">
        <p className="text-base text-gray-600 dark:text-gray-400 flex items-center justify-center gap-1">
          <span className="text-gray-300 text-xs">中文</span>
          {chinese}
          <span
            className="text-gray-300 text-xs ml-1 cursor-pointer hover:text-fuchsia-500"
            title="编辑翻译"
          >
            ✏️
          </span>
        </p>
      </div>
    </div>
  );
}
