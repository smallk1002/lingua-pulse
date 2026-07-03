// ============================================================
// Navbar - 全局导航栏
// ============================================================

"use client";

import Link from "next/link";
import { useAuthStore } from "@/stores/authStore";

export function Navbar() {
  const { user, isAuthenticated, isLoading, logout } = useAuthStore();

  return (
    <nav className="sticky top-0 z-50 bg-white/80 dark:bg-gray-950/80 backdrop-blur border-b border-gray-200 dark:border-gray-800">
      <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
        {/* Logo */}
        <Link
          href="/"
          className="flex items-center gap-2 text-xl font-bold bg-gradient-to-r from-fuchsia-600 to-purple-600 bg-clip-text text-transparent"
        >
          <img src="/logo.png" alt="LinguaPulse" className="w-7 h-7 rounded-lg" />
          LinguaPulse
        </Link>

        {/* 右侧 */}
        <div className="flex items-center gap-4">
          {isLoading ? (
            <div className="w-20 h-8 bg-gray-200 dark:bg-gray-800 rounded animate-pulse" />
          ) : isAuthenticated && user ? (
            <>
              <Link
                href="/home"
                className="text-sm text-gray-600 dark:text-gray-400 hover:text-fuchsia-600 transition-colors"
              >
                学习主页
              </Link>
              <Link
                href="/settings"
                className="text-sm text-gray-600 dark:text-gray-400 hover:text-fuchsia-600 transition-colors"
              >
                设置
              </Link>
              <span className="text-sm text-gray-400">|</span>
              <span className="text-sm text-gray-700 dark:text-gray-300">
                {user.username}
              </span>
              <button
                onClick={logout}
                className="text-sm text-gray-400 hover:text-red-500 transition-colors"
              >
                退出
              </button>
            </>
          ) : (
            <>
              <Link
                href="/auth/login"
                className="text-sm text-gray-600 dark:text-gray-400 hover:text-fuchsia-600 transition-colors"
              >
                登录
              </Link>
              <Link
                href="/auth/register"
                className="px-4 py-1.5 bg-fuchsia-600 text-white text-sm rounded-lg hover:bg-fuchsia-700 transition-colors"
              >
                免费注册
              </Link>
            </>
          )}
        </div>
      </div>
    </nav>
  );
}
