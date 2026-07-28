// ============================================================
// Courses Page - 课程商场
// ============================================================

"use client";

import Link from "next/link";
import { useQuery } from "@tanstack/react-query";
import { getMarketCoursePacks } from "@/lib/api";

export default function CoursesPage() {
  const { data: coursePacks, isLoading } = useQuery({
    queryKey: ["marketCoursePacks"],
    queryFn: getMarketCoursePacks,
  });

  const handleJoin = async (packId: string) => {
    window.location.href = `/start?coursePackId=${packId}`;
  };

  return (
    <div className="max-w-6xl mx-auto px-4 py-12">
      <Link
        href="/"
        className="text-sm text-gray-400 hover:text-fuchsia-600 transition-colors mb-6 inline-block"
      >
        ← 返回首页
      </Link>

      <h1 className="text-2xl font-bold mb-8">课程商场</h1>

      {isLoading ? (
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {[1, 2, 3, 4, 5, 6].map((i) => (
            <div
              key={i}
              className="h-48 rounded-xl bg-gray-100 dark:bg-gray-800 animate-pulse"
            />
          ))}
        </div>
      ) : !coursePacks || coursePacks.length === 0 ? (
        <div className="text-center py-20 text-gray-400">
          <p className="text-4xl mb-3">📚</p>
          <p>暂无可用的课程包</p>
        </div>
      ) : (
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {coursePacks.map((pack) => (
            <div
              key={pack.id}
              className="p-6 rounded-xl border border-gray-200 dark:border-gray-800
                         hover:border-fuchsia-300 dark:hover:border-fuchsia-700
                         hover:shadow-md transition-all"
            >
              <div className="flex items-start justify-between mb-3">
                <h3 className="font-bold text-lg">{pack.title}</h3>
                <span className="text-xs px-2 py-0.5 rounded-full bg-fuchsia-100 dark:bg-fuchsia-900 text-fuchsia-700 capitalize">
                  {pack.difficulty}
                </span>
              </div>
              <p className="text-sm text-gray-500 line-clamp-2 mb-4">
                {pack.description}
              </p>
              <div className="flex items-center justify-between">
                <span className="text-xs text-gray-400">
                  {pack.course_count} 节课 · {pack.statement_count} 句
                </span>
                <div className="flex gap-2">
                  <button
                    onClick={() => handleJoin(pack.id)}
                    className="px-3 py-1.5 text-xs border border-fuchsia-300 text-fuchsia-600
                               rounded-lg hover:bg-fuchsia-50 dark:hover:bg-fuchsia-950 transition-colors"
                  >
                    加入
                  </button>
                  <Link
                    href={`/start?coursePackId=${pack.id}`}
                    className="px-3 py-1.5 text-xs bg-fuchsia-600 text-white rounded-lg
                               hover:bg-fuchsia-700 transition-colors"
                  >
                    开始学习
                  </Link>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
