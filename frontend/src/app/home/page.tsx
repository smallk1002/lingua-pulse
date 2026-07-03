// ============================================================
// Home Page - 学习主页（需登录）
// ============================================================

"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import { useAuthStore } from "@/stores/authStore";
import { useQuery } from "@tanstack/react-query";
import { getStatsSummary, getMyCoursePacks } from "@/lib/api";
import type { GameMode, Difficulty } from "@/lib/types";

const getSavedMode = (): GameMode => {
  try { return (localStorage.getItem("gameMode") as GameMode) || "chinese_to_english"; }
  catch { return "chinese_to_english"; }
};
const getSavedDifficulty = (): Difficulty => {
  try { return (localStorage.getItem("gameDifficulty") as Difficulty) || "intermediate"; }
  catch { return "intermediate"; }
};

export default function HomePage() {
  const { user, isAuthenticated, isLoading: authLoading } = useAuthStore();
  const router = useRouter();

  useEffect(() => {
    if (!authLoading && !isAuthenticated) {
      router.replace("/");
    }
  }, [authLoading, isAuthenticated, router]);

  const { data: stats, isLoading: statsLoading } = useQuery({
    queryKey: ["stats"],
    queryFn: getStatsSummary,
    enabled: isAuthenticated,
  });

  const { data: coursePacks, isLoading: coursesLoading } = useQuery({
    queryKey: ["myCoursePacks"],
    queryFn: getMyCoursePacks,
    enabled: isAuthenticated,
  });

  if (authLoading || !isAuthenticated || !user) {
    return (
      <div className="flex items-center justify-center min-h-[80vh]">
        <div className="animate-pulse text-fuchsia-600 text-lg">加载中...</div>
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      {/* 欢迎行 */}
      <div className="mb-8 flex items-center gap-4">
        <img
          src="/logo.png"
          alt="LinguaPulse"
          className="w-14 h-14 rounded-xl shadow-md"
        />
        <div>
          <h1 className="text-2xl font-bold">
            你好，{user.username} 👋
          </h1>
          <p className="text-gray-500 mt-1">
            已经学习了 {stats?.total_statements ?? 0} 个句子
          </p>
        </div>
      </div>

      {/* 统计卡片 */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-10">
        <StatCard icon="🔥" label="连续学习" value={`${stats?.streak ?? 0} 天`} />
        <StatCard icon="📝" label="已学句子" value={`${stats?.total_statements ?? 0} 句`} />
        <StatCard icon="⭐" label="总经验值" value={`${stats?.xp ?? 0} XP`} />
        <StatCard icon="⏱️" label="学习时长" value={`${((stats?.total_duration ?? 0) / 3600).toFixed(1)}h`} />
      </div>

      {/* 我的课程包 */}
      <section className="mb-10">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-xl font-bold">我的课程包</h2>
          <Link
            href="/courses"
            className="text-sm text-fuchsia-600 hover:underline"
          >
            查看全部 →
          </Link>
        </div>

        {coursesLoading ? (
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
            {[1, 2, 3].map((i) => (
              <div
                key={i}
                className="h-32 rounded-xl bg-gray-100 dark:bg-gray-800 animate-pulse"
              />
            ))}
          </div>
        ) : !coursePacks || coursePacks.length === 0 ? (
          <div className="text-center py-12 text-gray-400">
            <p className="text-4xl mb-3">📚</p>
            <p>还没有加入任何课程包</p>
            <Link
              href="/courses"
              className="text-fuchsia-600 hover:underline text-sm mt-2 inline-block"
            >
              去课程商场看看 →
            </Link>
          </div>
        ) : (
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
            {coursePacks.map((pack) => (
              <div
                key={pack.id}
                className={`p-5 rounded-xl border hover:shadow-md transition-all
                  ${pack.last_course_id
                    ? "border-fuchsia-300 dark:border-fuchsia-800 bg-fuchsia-50 dark:bg-fuchsia-950"
                    : "border-gray-200 dark:border-gray-800"
                  } hover:border-fuchsia-400 dark:hover:border-fuchsia-600`}
              >
                <Link
                  href={`/start?coursePackId=${pack.id}`}
                  className="block group"
                >
                  <h3 className="font-semibold group-hover:text-fuchsia-600 transition-colors">
                    {pack.title}
                  </h3>
                  <p className="text-sm text-gray-500 mt-1 line-clamp-2">
                    {pack.description}
                  </p>
                </Link>
                <div className="flex items-center justify-between mt-3">
                  {pack.last_course_id ? (
                    <Link
                      href={`/game?coursePackId=${pack.id}&courseId=${pack.last_course_id}&mode=${getSavedMode()}&difficulty=${getSavedDifficulty()}`}
                      className="px-2.5 py-0.5 bg-fuchsia-600 text-white text-xs rounded-full font-medium
                                 hover:bg-fuchsia-700 transition-colors"
                    >
                      ▶ 继续学习
                    </Link>
                  ) : (
                    <span />
                  )}
                  <span className="text-xs text-gray-400">
                    {pack.course_count} 节课 · {pack.difficulty}
                  </span>
                </div>
              </div>
            ))}
          </div>
        )}
      </section>

      {/* 快速开始 */}
      <div className="text-center py-8">
        <Link
          href="/start"
          className="inline-block px-10 py-4 bg-fuchsia-600 text-white rounded-2xl
                     font-semibold text-lg hover:bg-fuchsia-700 transition-colors
                     shadow-lg hover:shadow-xl active:scale-95"
        >
          🚀 开始学习
        </Link>
      </div>
    </div>
  );
}

function StatCard({
  icon,
  label,
  value,
}: {
  icon: string;
  label: string;
  value: string;
}) {
  return (
    <div className="p-4 rounded-xl border border-gray-200 dark:border-gray-800
                    hover:border-fuchsia-200 dark:hover:border-fuchsia-800 transition-colors">
      <div className="text-2xl mb-1">{icon}</div>
      <div className="text-lg font-bold">{value}</div>
      <div className="text-xs text-gray-400">{label}</div>
    </div>
  );
}
