// ============================================================
// MoreExamples - 更多例句展示组件
// ============================================================

"use client";

import { useState } from "react";
import { useQuery } from "@tanstack/react-query";
import { getMoreExamples } from "@/lib/api";
import { useGameStore } from "@/stores/gameStore";

interface MoreExamplesProps {
  statementId: string;
  onClose: () => void;
}

export function MoreExamples({ statementId, onClose }: MoreExamplesProps) {
  const coursePackId = useGameStore((s) => s.coursePackId);
  const courseId = useGameStore((s) => s.courseId);

  const { data, isLoading } = useQuery({
    queryKey: ["more-examples", coursePackId, courseId, statementId],
    queryFn: () => getMoreExamples(coursePackId!, courseId!, statementId),
    enabled: !!coursePackId && !!courseId,
  });

  if (isLoading) {
    return (
      <div className="mt-6 p-6 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-800">
        <div className="text-center text-gray-500">加载中...</div>
      </div>
    );
  }

  if (!data || data.examples.length === 0) {
    return (
      <div className="mt-6 p-6 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-800">
        <div className="text-center text-gray-500">暂无更多例句</div>
        <button
          onClick={onClose}
          className="w-full mt-4 py-2 text-sm text-gray-500 hover:text-fuchsia-600 transition-colors"
        >
          关闭
        </button>
      </div>
    );
  }

  return (
    <div className="mt-6 p-6 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-800">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-bold">更多例句</h3>
        <button
          onClick={onClose}
          className="text-gray-400 hover:text-gray-600 transition-colors"
        >
          ✕
        </button>
      </div>

      <div className="space-y-4">
        {data.examples.map((example) => (
          <div
            key={example.id}
            className="p-4 rounded-lg bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700
                       hover:border-fuchsia-300 dark:hover:border-fuchsia-700 transition-colors"
          >
            <div className="text-lg font-semibold text-gray-800 dark:text-gray-100 mb-1">
              {example.english}
            </div>
            <div className="text-sm text-gray-500">{example.chinese}</div>
            {example.soundmark && (
              <div className="text-xs text-gray-400 font-mono mt-1">
                {example.soundmark}
              </div>
            )}
            <button
              onClick={() => {
                // TODO: 实现跳转到该例句的练习
                // 需要找到该例句所在的课程并跳转
              }}
              className="mt-3 px-4 py-1.5 text-sm bg-fuchsia-600 text-white rounded-lg
                         hover:bg-fuchsia-700 transition-colors"
            >
              练习这句
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
