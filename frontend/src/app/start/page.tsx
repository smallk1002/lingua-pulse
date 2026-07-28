// ============================================================
// Start Page - 选课 + 开始学习
// ============================================================

"use client";

import { useState, useEffect, Suspense } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import Link from "next/link";
import { useAuthStore } from "@/stores/authStore";
import { useQuery } from "@tanstack/react-query";
import { getCoursePack, getMyCoursePacks } from "@/lib/api";
import type { GameMode, Difficulty } from "@/lib/types";

// ============================================================
// Constants
// ============================================================

const MODES: { value: GameMode; label: string; desc: string; icon: string }[] = [
  {
    value: "chinese_to_english",
    label: "中译英",
    desc: "看中文输入英文",
    icon: "🇨🇳→🇬🇧",
  },
  {
    value: "dictation",
    label: "听写",
    desc: "听发音写单词",
    icon: "🎧",
  },
];

const DIFFICULTIES: {
  value: Difficulty;
  label: string;
  desc: string;
  borderColor: string;
  bgColor: string;
}[] = [
  {
    value: "beginner",
    label: "初级",
    desc: "提示较完整",
    borderColor: "border-green-400",
    bgColor: "bg-green-50 dark:bg-green-900/20",
  },
  {
    value: "intermediate",
    label: "中级",
    desc: "仅保留首尾",
    borderColor: "border-yellow-400",
    bgColor: "bg-yellow-50 dark:bg-yellow-900/20",
  },
  {
    value: "advanced",
    label: "高级",
    desc: "完全隐藏",
    borderColor: "border-red-400",
    bgColor: "bg-red-50 dark:bg-red-900/20",
  },
];

// ============================================================
// Helpers
// ============================================================

function getDifficultyLevel(difficulty: string, courseFile?: string): Difficulty {
  if (difficulty === "beginner" || difficulty === "intermediate" || difficulty === "advanced") {
    return difficulty;
  }
  // fallback by file path
  if (courseFile?.includes("nce3") || courseFile?.includes("nce4")) return "advanced";
  if (courseFile?.includes("nce2")) return "intermediate";
  return "beginner";
}

function getSavedMode(): GameMode {
  try {
    const v = localStorage.getItem("gameMode");
    if (v === "chinese_to_english" || v === "dictation") return v;
    return "chinese_to_english";
  } catch {
    return "chinese_to_english";
  }
}

function getSavedDifficulty(): Difficulty {
  try {
    const v = localStorage.getItem("gameDifficulty");
    if (v === "beginner" || v === "intermediate" || v === "advanced") return v;
    return "intermediate";
  } catch {
    return "intermediate";
  }
}

function saveMode(m: GameMode) {
  try { localStorage.setItem("gameMode", m); } catch { /* ignore */ }
}

function saveDifficulty(d: Difficulty) {
  try { localStorage.setItem("gameDifficulty", d); } catch { /* ignore */ }
}

// ============================================================
// Component
// ============================================================

function StartPageInner() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const { isAuthenticated } = useAuthStore();

  const coursePackId = searchParams.get("coursePackId");

  // ---- Course Pack Data ----
  const { data: coursePack, isLoading: packLoading } = useQuery({
    queryKey: ["coursePack", coursePackId],
    queryFn: () => getCoursePack(coursePackId!),
    enabled: !!coursePackId,
  });

  // ---- All Course Packs (when no coursePackId) ----
  const { data: allPacks } = useQuery({
    queryKey: ["allCoursePacks"],
    queryFn: getMyCoursePacks,
    enabled: !coursePackId,
  });

  // ---- State ----
  const [mode, setMode] = useState<GameMode>(getSavedMode());
  const [difficulty, setDifficulty] = useState<Difficulty>(getSavedDifficulty());
  const [selectedCourseId, setSelectedCourseId] = useState<string | null>(null);
  const presetCourseId = searchParams.get("courseId");

  // Set initial selected course: last_course_id > first course
  useEffect(() => {
    if (coursePack && !selectedCourseId) {
      const lastId = coursePack.last_course_id;
      const courseIds = new Set(coursePack.courses?.map((c) => c.id) ?? []);
      if (lastId && courseIds.has(lastId)) {
        setSelectedCourseId(lastId);
      } else {
        setSelectedCourseId(coursePack.courses?.[0]?.id ?? null);
      }
    }
  }, [coursePack]);

  // Use preset from URL if available
  useEffect(() => {
    if (presetCourseId) {
      setSelectedCourseId(presetCourseId);
    }
  }, [presetCourseId]);

  // ---- Handlers ----
  const handleStart = (courseId: string) => {
    if (!coursePackId) return;
    saveMode(mode);
    saveDifficulty(difficulty);
    router.push(
      `/game?coursePackId=${coursePackId}&courseId=${courseId}&mode=${mode}&difficulty=${difficulty}`
    );
  };

  // ============================================================
  // No coursePackId: Show Course Pack List
  // ============================================================
  if (!coursePackId) {
    return (
      <div className="max-w-2xl mx-auto px-4 py-10">
        <Link
          href="/home"
          className="text-sm text-gray-400 hover:text-fuchsia-600 transition-colors mb-6 inline-block"
        >
          ← 返回课程列表
        </Link>
        <h1 className="text-2xl font-bold mb-6">选择课程包</h1>

        {!allPacks ? (
          <div className="text-center py-12 text-gray-400">加载中...</div>
        ) : allPacks.length === 0 ? (
          <div className="text-center py-12 text-gray-400">
            <p className="text-4xl mb-3">📚</p>
            <p>暂无可用的课程包</p>
          </div>
        ) : (
          <div className="grid gap-3">
            {allPacks.map((pack) => (
              <Link
                key={pack.id}
                href={`/start?coursePackId=${pack.id}`}
                className="flex items-center justify-between p-4 rounded-xl border border-gray-200
                           dark:border-gray-700 hover:border-fuchsia-400 hover:shadow-md
                           transition-all bg-white dark:bg-gray-900"
              >
                <div>
                  <span className="font-semibold text-base">{pack.title}</span>
                  <div className="text-xs text-gray-400 mt-1">
                    {pack.course_count} 课 · {pack.statement_count} 句
                  </div>
                </div>
                <div className="flex items-center gap-2">
                  {pack.last_course_id && (
                    <span className="px-2 py-0.5 bg-fuchsia-100 dark:bg-fuchsia-900/30 text-fuchsia-700 dark:text-fuchsia-300 text-xs rounded-full">
                      学习中
                    </span>
                  )}
                  <span className="text-gray-300 text-lg">→</span>
                </div>
              </Link>
            ))}
          </div>
        )}
      </div>
    );
  }

  // ============================================================
  // With coursePackId: Mode/Difficulty + Course Grid
  // ============================================================
  if (packLoading || !coursePack) {
    return (
      <div className="flex items-center justify-center min-h-[50vh]">
        <div className="animate-pulse text-fuchsia-600 text-lg">加载课程...</div>
      </div>
    );
  }

  const courses = coursePack.courses ?? [];
  const lastCourseId = coursePack.last_course_id;
  const effectiveCourseId = selectedCourseId || courses[0]?.id;

  return (
    <div className="max-w-2xl mx-auto px-4 py-8">
      {/* Back */}
      <Link
        href="/courses"
        className="text-sm text-gray-400 hover:text-fuchsia-600 transition-colors mb-4 inline-block"
      >
        ← 返回课程列表
      </Link>

      <h1 className="text-2xl font-bold mb-1">{coursePack.title}</h1>
      <p className="text-sm text-gray-400 mb-6">
        {coursePack.course_count ?? courses.length} 课 ·{" "}
        {coursePack.statement_count ?? 0} 句
      </p>

      {/* ---- Mode Selector ---- */}
      <section className="mb-5">
        <h2 className="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">
          练习模式
        </h2>
        <div className="grid grid-cols-2 gap-3">
          {MODES.map((m) => (
            <button
              key={m.value}
              onClick={() => {
                setMode(m.value);
                saveMode(m.value);
              }}
              className={`p-4 rounded-xl border-2 text-left transition-all ${
                mode === m.value
                  ? "border-fuchsia-400 bg-fuchsia-50 dark:bg-fuchsia-900/20 shadow-sm"
                  : "border-gray-200 dark:border-gray-700 hover:border-fuchsia-300"
              }`}
            >
              <div className="text-lg mb-1">{m.icon}</div>
              <div className="font-semibold text-sm">{m.label}</div>
              <div className="text-xs text-gray-400 mt-0.5">{m.desc}</div>
            </button>
          ))}
        </div>
      </section>

      {/* ---- Difficulty Selector ---- */}
      <section className="mb-6">
        <h2 className="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">
          难度
        </h2>
        <div className="flex gap-2">
          {DIFFICULTIES.map((d) => (
            <button
              key={d.value}
              onClick={() => {
                setDifficulty(d.value);
                saveDifficulty(d.value);
              }}
              className={`flex-1 py-2.5 px-3 rounded-xl border-2 text-sm font-medium transition-all ${
                difficulty === d.value
                  ? `${d.borderColor} ${d.bgColor} shadow-sm`
                  : "border-gray-200 dark:border-gray-700 hover:border-gray-300"
              }`}
            >
              {d.label}
              <div className="text-xs font-normal text-gray-400 mt-0.5">{d.desc}</div>
            </button>
          ))}
        </div>
      </section>

      {/* ---- Course Grid ---- */}
      <section className="mb-8">
        <h2 className="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">
          选择课程
        </h2>
        {courses.length === 0 ? (
          <p className="text-gray-400 text-sm">暂无课程数据</p>
        ) : (
          <div className="grid grid-cols-5 sm:grid-cols-6 md:grid-cols-8 gap-2">
            {courses.map((course) => {
              const isLastLearned = course.id === lastCourseId;
              const isSelected = course.id === effectiveCourseId;

              return (
                <button
                  key={course.id}
                  onClick={() => setSelectedCourseId(course.id)}
                  className={`relative aspect-square rounded-xl border-2 flex flex-col items-center justify-center
                    text-xs font-semibold transition-all
                    ${
                      isSelected
                        ? "border-fuchsia-400 bg-fuchsia-50 dark:bg-fuchsia-900/20 shadow-sm"
                        : "border-gray-200 dark:border-gray-700 hover:border-fuchsia-300"
                    }
                  `}
                  title={course.title ?? `第${course.order}课`}
                >
                  {isLastLearned && (
                    <span className="absolute -top-1 -right-1 w-3 h-3 bg-fuchsia-500 rounded-full border-2 border-white dark:border-gray-950" />
                  )}
                  <span className="text-lg">📖</span>
                  <span className="mt-1">{course.order}</span>
                </button>
              );
            })}
          </div>
        )}
      </section>

      {/* ---- Action Buttons ---- */}
      <div className="flex gap-3">
        {/* 继续学习（优先） */}
        {lastCourseId && (
          <button
            onClick={() => handleStart(lastCourseId)}
            className="flex-1 py-3.5 bg-fuchsia-600 text-white rounded-xl font-semibold
                       hover:bg-fuchsia-700 transition-colors shadow-lg active:scale-[0.98]"
          >
            ▶ 继续学习
            {(() => {
              const c = courses.find((x) => x.id === lastCourseId);
              return c ? `：第${c.order}课` : "";
            })()}
          </button>
        )}

        {/* 开始选中的课 */}
        {effectiveCourseId && effectiveCourseId !== lastCourseId && (
          <button
            onClick={() => handleStart(effectiveCourseId)}
            className="flex-1 py-3.5 border-2 border-fuchsia-400 text-fuchsia-600
                       rounded-xl font-semibold hover:bg-fuchsia-50 dark:hover:bg-fuchsia-900/20
                       transition-colors active:scale-[0.98]"
          >
            🚀 开始第{courses.find((c) => c.id === effectiveCourseId)?.order ?? "?"}课
          </button>
        )}
      </div>
    </div>
  );
}

// ============================================================
// Wrapper with Suspense
// ============================================================

export default function StartPage() {
  return (
    <Suspense
      fallback={
        <div className="flex items-center justify-center min-h-[80vh]">
          <div className="animate-pulse text-fuchsia-600 text-lg">加载中...</div>
        </div>
      }
    >
      <StartPageInner />
    </Suspense>
  );
}
