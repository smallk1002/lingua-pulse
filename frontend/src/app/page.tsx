// ============================================================
// Landing Page - 未登录首页
// ============================================================

"use client";

import Link from "next/link";
import { useAuthStore } from "@/stores/authStore";
import { useEffect } from "react";
import { useRouter } from "next/navigation";

export default function LandingPage() {
  const { isAuthenticated, isLoading } = useAuthStore();
  const router = useRouter();

  useEffect(() => {
    if (!isLoading && isAuthenticated) {
      router.replace("/home");
    }
  }, [isLoading, isAuthenticated, router]);

  if (isLoading) {
    return (
      <div className="flex items-center justify-center min-h-[80vh]">
        <div className="animate-pulse text-fuchsia-600 text-lg">加载中...</div>
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto px-4">
      {/* Hero */}
      <section className="py-20 md:py-32 text-center">
        <img
          src="/logo.png"
          alt="LinguaPulse"
          className="w-24 h-24 mx-auto mb-8 rounded-2xl shadow-lg"
        />
        <h1 className="text-4xl md:text-6xl font-bold mb-6 leading-tight">
          让英语学习
          <br />
          <span className="bg-gradient-to-r from-fuchsia-600 to-purple-600 bg-clip-text text-transparent">
            像心跳一样自然
          </span>
        </h1>
        <p className="text-lg md:text-xl text-gray-500 dark:text-gray-400 mb-10 max-w-2xl mx-auto">
          逐词打字 · 科学记忆 · 游戏化学习。
          通过 SM-2 间隔重复算法，在遗忘临界点精准复习，真正掌握英语表达。
        </p>
        <div className="flex gap-4 justify-center">
          <Link
            href="/courses"
            className="px-8 py-3 bg-fuchsia-600 text-white rounded-xl font-semibold
                       text-lg hover:bg-fuchsia-700 transition-colors shadow-lg hover:shadow-xl"
          >
            免费体验
          </Link>
          <Link
            href="#features"
            className="px-8 py-3 border-2 border-gray-300 dark:border-gray-700 rounded-xl
                       font-semibold text-lg hover:border-fuchsia-400 transition-colors"
          >
            了解更多
          </Link>
        </div>
      </section>

      {/* 三大特色 */}
      <section id="features" className="py-16">
        <h2 className="text-3xl font-bold text-center mb-12">
          为什么选择 LinguaPulse？
        </h2>
        <div className="grid md:grid-cols-3 gap-8">
          <div className="p-6 rounded-2xl border border-gray-200 dark:border-gray-800 hover:border-fuchsia-300 dark:hover:border-fuchsia-700 transition-colors">
            <div className="text-4xl mb-4">⌨️</div>
            <h3 className="text-xl font-bold mb-2">逐词打字</h3>
            <p className="text-gray-500 dark:text-gray-400">
              不再是选择题！逐词拼写英文句子，从被动识别变为主动输出，真正学会用英语表达。
            </p>
          </div>
          <div className="p-6 rounded-2xl border border-gray-200 dark:border-gray-800 hover:border-fuchsia-300 dark:hover:border-fuchsia-700 transition-colors">
            <div className="text-4xl mb-4">🧠</div>
            <h3 className="text-xl font-bold mb-2">SM-2 间隔重复</h3>
            <p className="text-gray-500 dark:text-gray-400">
              基于科学记忆算法，在你即将遗忘的临界点自动安排复习。记得越牢，复习间隔越长。
            </p>
          </div>
          <div className="p-6 rounded-2xl border border-gray-200 dark:border-gray-800 hover:border-fuchsia-300 dark:hover:border-fuchsia-700 transition-colors">
            <div className="text-4xl mb-4">🎮</div>
            <h3 className="text-xl font-bold mb-2">双模式练习</h3>
            <p className="text-gray-500 dark:text-gray-400">
              中译英模式 + 听写模式，从不同维度训练英语能力。XP/等级/连胜，像游戏一样上瘾。
            </p>
          </div>
        </div>
      </section>

      {/* 底部 CTA */}
      <section className="py-20 text-center">
        <div className="max-w-md mx-auto p-8 rounded-2xl bg-gradient-to-br from-fuchsia-50 to-purple-50 dark:from-fuchsia-950 dark:to-purple-950 border border-fuchsia-200 dark:border-fuchsia-800">
          <h3 className="text-2xl font-bold mb-4">准备好开始了吗？</h3>
          <p className="text-gray-500 dark:text-gray-400 mb-6">
            无需注册，即刻体验。喜欢再注册，进度不会丢。
          </p>
          <Link
            href="/courses"
            className="inline-block px-8 py-3 bg-fuchsia-600 text-white rounded-xl
                       font-semibold hover:bg-fuchsia-700 transition-colors"
          >
            🚀 免费体验
          </Link>
        </div>
      </section>
    </div>
  );
}
