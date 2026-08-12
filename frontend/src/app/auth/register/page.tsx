// ============================================================
// Register Page
// ============================================================

"use client";

import { useEffect, useRef, useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useAuthStore } from "@/stores/authStore";
import { register, sendCode } from "@/lib/api";

export default function RegisterPage() {
  const [email, setEmail] = useState("");
  const [code, setCode] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [notice, setNotice] = useState("");
  const [loading, setLoading] = useState(false);
  const [sending, setSending] = useState(false);
  const [countdown, setCountdown] = useState(0);
  const timerRef = useRef<NodeJS.Timeout | null>(null);
  const router = useRouter();
  const { setAuth } = useAuthStore();

  useEffect(() => {
    return () => {
      if (timerRef.current) clearInterval(timerRef.current);
    };
  }, []);

  const startCountdown = () => {
    setCountdown(60);
    timerRef.current = setInterval(() => {
      setCountdown((prev) => {
        if (prev <= 1 && timerRef.current) clearInterval(timerRef.current);
        return prev - 1;
      });
    }, 1000);
  };

  const handleSendCode = async () => {
    if (!email || sending || countdown > 0) return;
    setError("");
    setNotice("");
    setSending(true);
    try {
      const res = await sendCode(email);
      startCountdown();
      setNotice(res.message);
    } catch (err: unknown) {
      const message = err instanceof Error ? err.message : "发送失败";
      setError(message);
    } finally {
      setSending(false);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setNotice("");
    setLoading(true);
    try {
      const res = await register({ email, username, password, code });
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
        {notice && (
          <div className="p-3 rounded-lg bg-green-50 dark:bg-green-950 text-green-600 text-sm">
            {notice}
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
          <label className="block text-sm font-medium mb-1">邮箱验证码</label>
          <div className="flex gap-2">
            <input
              type="text"
              value={code}
              onChange={(e) => setCode(e.target.value.replace(/\D/g, "").slice(0, 6))}
              required
              maxLength={6}
              inputMode="numeric"
              className="flex-1 px-4 py-2 rounded-lg border border-gray-300 dark:border-gray-700
                         bg-white dark:bg-gray-900 focus:ring-2 focus:ring-fuchsia-500 focus:border-transparent"
              placeholder="6 位验证码"
            />
            <button
              type="button"
              onClick={handleSendCode}
              disabled={sending || countdown > 0 || !email}
              className="px-4 py-2 rounded-lg text-sm font-medium whitespace-nowrap
                         bg-fuchsia-100 dark:bg-fuchsia-950 text-fuchsia-700 dark:text-fuchsia-300
                         hover:bg-fuchsia-200 dark:hover:bg-fuchsia-900 transition-colors
                         disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {sending ? "发送中..." : countdown > 0 ? `${countdown}s 后重发` : "发送验证码"}
            </button>
          </div>
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

        <p className="text-center text-sm text-gray-400">
          <Link href="/download" className="hover:text-fuchsia-600 transition-colors">
            ⬇ 下载桌面客户端
          </Link>
        </p>
      </form>
    </div>
  );
}
