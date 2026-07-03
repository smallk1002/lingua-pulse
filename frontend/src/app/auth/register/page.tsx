// ============================================================
// Register Page
// ============================================================

"use client";

import { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useAuthStore } from "@/stores/authStore";
import { register } from "@/lib/api";

export default function RegisterPage() {
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const router = useRouter();
  const { setAuth } = useAuthStore();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      const res = await register({ email, username, password });
      setAuth(res.user, res.access_token);
      router.push("/home");
    } catch (err: unknown) {
      const message = err instanceof Error ? err.message : "注册失败";
      setError(message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-md mx-auto px-4 py-20">
      <img
        src="/logo.png"
        alt="LinguaPulse"
        className="w-16 h-16 mx-auto mb-6 rounded-xl shadow-md"
      />
      <h1 className="text-2xl font-bold text-center mb-8">注册 LinguaPulse</h1>

      <form onSubmit={handleSubmit} className="space-y-4">
        {error && (
          <div className="p-3 rounded-lg bg-red-50 dark:bg-red-950 text-red-600 text-sm">
            {error}
          </div>
        )}

        <div>
          <label className="block text-sm font-medium mb-1">用户名</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
            minLength={3}
            className="w-full px-4 py-2 rounded-lg border border-gray-300 dark:border-gray-700
                       bg-white dark:bg-gray-900 focus:ring-2 focus:ring-fuchsia-500 focus:border-transparent"
            placeholder="你的昵称"
          />
        </div>

        <div>
          <label className="block text-sm font-medium mb-1">邮箱</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            className="w-full px-4 py-2 rounded-lg border border-gray-300 dark:border-gray-700
                       bg-white dark:bg-gray-900 focus:ring-2 focus:ring-fuchsia-500 focus:border-transparent"
            placeholder="your@email.com"
          />
        </div>

        <div>
          <label className="block text-sm font-medium mb-1">密码</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            minLength={6}
            className="w-full px-4 py-2 rounded-lg border border-gray-300 dark:border-gray-700
                       bg-white dark:bg-gray-900 focus:ring-2 focus:ring-fuchsia-500 focus:border-transparent"
            placeholder="至少 6 位"
          />
        </div>

        <button
          type="submit"
          disabled={loading}
          className="w-full py-3 bg-fuchsia-600 text-white rounded-xl font-semibold
                     hover:bg-fuchsia-700 transition-colors disabled:opacity-50"
        >
          {loading ? "注册中..." : "免费注册"}
        </button>

        <p className="text-center text-sm text-gray-500">
          已有账号？{" "}
          <Link href="/auth/login" className="text-fuchsia-600 hover:underline">
            登录
          </Link>
        </p>
      </form>
    </div>
  );
}
