// ============================================================
// Start Page - 选择模式和难度
// ============================================================

"use client";

import { useState, useEffect, Suspense } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import Link from "next/link";
import { useAuthStore } from "@/stores/authStore";
import { useQuery } from "@tanstack/react-query";
import { getCoursePack } from "@/lib/api";
import type { GameMode, Difficulty } from "@/lib/types";

const MODES: { key: GameMode; icon: string; label: string; desc: string }[] = [
  {
    key: "chinese_to_english",
    icon: "🇨🇳→🇬🇧",
    label: "中译英",
    desc: "看中文提示，输入英文句子",
  },
  {
    key: "dictation",
    icon: "🎧",
    label: "听写",
    desc: "听发音，输入英文句子",
  },
];

const DIFFICULTIES: { key: Difficulty; icon: string; label: string; desc: string }[] = [
  {
    key: "beginner",
    icon: "🌱",
    label: "初级",
    desc: "显示单词宽度提示，3 次错误自动显示答案",
  },
  {
    key: "intermediate",
    icon: "🔥",
    label: "中级",
    desc: "无宽度提示，答错进入 Fix 修复模式",
  },
  {
    key: "advanced",
    icon: "💀",
    label: "高级",
    desc: "无任何提示，每题限时 30s，超时计错",
  },
];

const getSavedMode = (): GameMode => {
  try { return (localStorage.getItem("gameMode") as GameMode) || "chinese_to_english"; }
  catch { return "chinese_to_english"; }
};
const getSavedDifficulty = (): Difficulty => {
  try { return (localStorage.getItem("gameDifficulty") as Difficulty) || "intermediate"; }
  catch { return "intermediate"; }
};

export default function StartPageWrapper() {
  return (
    <Suspense
      fallback={
        <div className="flex items-center justify-center min-h-[80vh]">
          <div className="animate-pulse text-fuchsia-600 text-lg">加载中...</div>
        </div>
      }
    >
      <StartPage />
    </Suspense>
  );
}

function StartPage() {
  const { isAuthenticated, isLoading: authLoading } = useAuthStore();
  const router = useRouter();
  const searchParams = useSearchParams();

  const coursePackId = searchParams.get("coursePackId");
  const preselectedCourseId = searchParams.get("courseId");

  const [mode, setMode] = useState<GameMode>(getSavedMode());
  const [difficulty, setDifficulty] = useState<Difficulty>(getSavedDifficulty());
  const [selectedCourseId, setSelectedCourseId] = useState<string | null>(
    preselectedCourseId
  );
  const [showDialog, setShowDialog] = useState(false);

  useEffect(() => {
    if (!authLoading && !isAuthenticated) {
      router.replace("/auth/login");
    }
  }, [authLoading, isAuthenticated, router]);

  const { data: coursePack, isLoading } = useQuery({
    queryKey: ["coursePack", coursePackId],
    queryFn: () => getCoursePack(coursePackId!),
    enabled: !!coursePackId && isAuthenticated,
  });

  if (authLoading || !isAuthenticated) {
    return (
      <div className="flex items-center justify-center min-h-[80vh]">
        <div className="animate-pulse text-fuchsia-600 text-lg">加载中...</div>
      </div>
    );
  }

  const handleStart = () => {
    if (!coursePackId) return;
    const cid = selectedCourseId ?? coursePack?.courses?.[0]?.id;
    if (!cid) return;
    router.push(
      `/game?coursePackId=${coursePackId}&courseId=${cid}&mode=${mode}&difficulty=${difficulty}`
    );
  };

  const handleContinue = () => {
    if (!coursePackId || !coursePack) return;
    const cid = coursePack.last_course_id ?? coursePack.courses?.[0]?.id;
    if (!cid) return;
    router.push(
      `/game?coursePackId=${coursePackId}&courseId=${cid}&mode=${mode}&difficulty=${difficulty}`
    );
  };

  return (
    <div className="max-w-2xl mx-auto px-4 py-12">
      <Link
        href="/home"
        className="text-sm text-gray-400 hover:text-fuchsia-600 transition-colors mb-6 inline-block"
      >
        ← 返回主页
      </Link>

      <h1 className="text-2xl font-bold mb-8">开始学习</h1>

      {/* 课程包信息 */}
      {coursePackId && (
        <div className="mb-8 p-4 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-800">
          {isLoading ? (
            <div className="h-6 w-48 bg-gray-200 dark:bg-gray-700 rounded animate-pulse" />
          ) : (
            <>
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm text-gray-500">课程包</p>
                  <p className="font-semibold">{coursePack?.title ?? "加载中..."}</p>
                </div>
                <button
                  onClick={handleContinue}
                  disabled={!coursePack?.courses?.length}
                  className="px-4 py-2 bg-fuchsia-600 text-white rounded-xl text-sm font-semibold
                             hover:bg-fuchsia-700 transition-colors shadow-sm
                             disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  ▶ 继续学习
                </button>
              </div>

              {/* 课程选择 */}
              {coursePack?.courses && coursePack.courses.length > 0 && (
                <div className="mt-3">
                  <p className="text-sm text-gray-500 mb-2">选择课时</p>
                  <div className="grid grid-cols-3 gap-2">
                    {coursePack.courses.map((c) => (
                      <button
                        key={c.id}
                        onClick={() => setSelectedCourseId(c.id)}
                        className={`p-2 rounded-lg text-sm text-left border transition-colors
                          ${
                            selectedCourseId === c.id ||
                            (!selectedCourseId && c.id === coursePack.courses[0].id)
                              ? "border-fuchsia-500 bg-fuchsia-50 dark:bg-fuchsia-950 text-fuchsia-700"
                              : "border-gray-200 dark:border-gray-700 hover:border-fuchsia-300"
                          }`}
                      >
                        {c.title}
                      </button>
                    ))}
                  </div>
                </div>
              )}
            </>
          )}
        </div>
      )}

      {/* 开始按钮 → 弹出模式/难度选择 */}
      <div className="text-center">
        <button
          onClick={() => setShowDialog(true)}
          className="px-12 py-4 bg-fuchsia-600 text-white rounded-2xl
                     font-semibold text-lg hover:bg-fuchsia-700 transition-colors
                     shadow-lg hover:shadow-xl active:scale-95"
        >
          🚀 开始学习
        </button>
        <p className="text-xs text-gray-400 mt-2">或按 Enter</p>
      </div>

      {/* 弹窗：选择模式 & 难度 */}
      {showDialog && (
        <div className="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-white dark:bg-gray-900 rounded-2xl shadow-2xl max-w-lg w-full p-6 max-h-[90vh] overflow-y-auto">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-lg font-bold">选择模式 & 难度</h2>
              <button
                onClick={() => setShowDialog(false)}
                className="text-gray-400 hover:text-gray-600 transition-colors text-2xl leading-none"
              >
                ×
              </button>
            </div>

            {/* 模式 */}
            <div className="mb-6">
              <p className="text-sm text-gray-500 mb-3">练习模式</p>
              <div className="grid grid-cols-2 gap-3">
                {MODES.map((m) => (
                  <button
                    key={m.key}
                    onClick={() => setMode(m.key)}
                    className={`p-4 rounded-xl border-2 text-left transition-all
                      ${
                        mode === m.key
                          ? "border-fuchsia-500 bg-fuchsia-50 dark:bg-fuchsia-950 shadow-md"
                          : "border-gray-200 dark:border-gray-700 hover:border-fuchsia-300"
                      }`}
                  >
                    <div className="text-xl mb-1">{m.icon}</div>
                    <div className="font-bold text-sm">{m.label}</div>
                    <div className="text-xs text-gray-500 mt-0.5">{m.desc}</div>
                  </button>
                ))}
              </div>
            </div>

            {/* 难度 */}
            <div className="mb-6">
              <p className="text-sm text-gray-500 mb-3">难度级别</p>
              <div className="grid grid-cols-3 gap-3">
                {DIFFICULTIES.map((d) => (
                  <button
                    key={d.key}
                    onClick={() => setDifficulty(d.key)}
                    className={`p-3 rounded-xl border-2 text-center transition-all
                      ${
                        difficulty === d.key
                          ? "border-fuchsia-500 bg-fuchsia-50 dark:bg-fuchsia-950 shadow-md"
                          : "border-gray-200 dark:border-gray-700 hover:border-fuchsia-300"
                      }`}
                  >
                    <div className="text-xl mb-1">{d.icon}</div>
                    <div className="font-bold text-xs">{d.label}</div>
                    <div className="text-[10px] text-gray-500 mt-0.5">{d.desc}</div>
                  </button>
                ))}
              </div>
            </div>

            <button
              onClick={() => {
                try { localStorage.setItem("gameMode", mode); } catch {}
                try { localStorage.setItem("gameDifficulty", difficulty); } catch {}
                setShowDialog(false);
                handleStart();
              }}
              className="w-full py-3 bg-fuchsia-600 text-white rounded-xl font-semibold
                         hover:bg-fuchsia-700 transition-colors"
            >
              确认并开始
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
