// ============================================================
// Settings Page
// ============================================================

"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import { useAuthStore } from "@/stores/authStore";

function getLsBool(key: string, defaultVal: boolean): boolean {
  if (typeof window === "undefined") return defaultVal;
  const v = localStorage.getItem(key);
  return v !== null ? v !== "false" : defaultVal;
}

function getLsNumber(key: string, defaultVal: number): number {
  if (typeof window === "undefined") return defaultVal;
  const v = localStorage.getItem(key);
  return v !== null ? parseInt(v, 10) || defaultVal : defaultVal;
}

function setLs(key: string, value: string) {
  if (typeof window !== "undefined") {
    localStorage.setItem(key, value);
  }
}

export default function SettingsPage() {
  const { isAuthenticated, isLoading, user, logout } = useAuthStore();
  const router = useRouter();

  useEffect(() => {
    if (!isLoading && !isAuthenticated) {
      router.replace("/");
    }
  }, [isLoading, isAuthenticated, router]);

  if (isLoading || !isAuthenticated) {
    return (
      <div className="flex items-center justify-center min-h-[80vh]">
        <div className="animate-pulse text-fuchsia-600 text-lg">加载中...</div>
      </div>
    );
  }

  return (
    <div className="max-w-2xl mx-auto px-4 py-12">
      <Link
        href="/home"
        className="text-sm text-gray-400 hover:text-fuchsia-600 transition-colors mb-6 inline-block"
      >
        ← 返回主页
      </Link>

      <h1 className="text-2xl font-bold mb-8">设置</h1>

      {/* 账号信息 */}
      <section className="mb-10">
        <h2 className="text-lg font-semibold mb-4">账号</h2>
        <div className="p-4 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-800 space-y-2">
          <div className="flex justify-between">
            <span className="text-gray-500">用户名</span>
            <span className="font-medium">{user?.username}</span>
          </div>
          <div className="flex justify-between">
            <span className="text-gray-500">邮箱</span>
            <span className="font-medium">{user?.email}</span>
          </div>
          <div className="flex justify-between">
            <span className="text-gray-500">注册时间</span>
            <span className="font-medium">
              {user?.created_at
                ? new Date(user.created_at).toLocaleDateString("zh-CN")
                : "-"}
            </span>
          </div>
        </div>
      </section>

      {/* 声音设置 */}
      <section className="mb-10">
        <h2 className="text-lg font-semibold mb-4">声音</h2>
        <div className="space-y-3">
          <SettingToggle
            label="键盘打字音效"
            desc="按下键盘时播放打字声音"
            localStorageKey="keyboardSoundEnabled"
            defaultEnabled={true}
          />
          <PlayCountPicker
            label="听写播放次数"
            desc="听写模式下，每题自动播放几次发音"
            localStorageKey="dictationPlayCount"
            defaultValue={2}
          />
          <VoicePicker
            label="TTS 朗读语音"
            desc="选择朗读发音的声音"
            localStorageKey="ttsVoice"
            defaultValue="en-US-JennyNeural"
          />
        </div>
      </section>

      {/* 学习偏好 */}
      <section className="mb-10">
        <h2 className="text-lg font-semibold mb-4">学习偏好</h2>
        <div className="p-4 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-800">
          <p className="text-sm text-gray-500">
            默认模式和难度可在"开始学习"页面选择
          </p>
        </div>
      </section>

      {/* 退出 */}
      <section>
        <button
          onClick={logout}
          className="w-full py-3 border-2 border-red-200 dark:border-red-800 text-red-500
                     rounded-xl font-semibold hover:bg-red-50 dark:hover:bg-red-950 transition-colors"
        >
          退出登录
        </button>
      </section>
    </div>
  );
}

function SettingToggle({
  label,
  desc,
  localStorageKey,
  defaultEnabled,
}: {
  label: string;
  desc: string;
  localStorageKey: string;
  defaultEnabled: boolean;
}) {
  const [enabled, setEnabled] = useState(() => getLsBool(localStorageKey, defaultEnabled));

  const toggle = () => {
    const next = !enabled;
    setEnabled(next);
    setLs(localStorageKey, String(next));
  };

  return (
    <div className="flex items-center justify-between p-4 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-800">
      <div>
        <div className="font-medium">{label}</div>
        <div className="text-xs text-gray-500">{desc}</div>
      </div>
      <button
        onClick={toggle}
        className={`w-12 h-6 rounded-full transition-colors relative
          ${enabled ? "bg-fuchsia-600" : "bg-gray-300 dark:bg-gray-700"}`}
      >
        <div
          className={`absolute top-0.5 w-5 h-5 bg-white rounded-full shadow transition-all
            ${enabled ? "left-[26px]" : "left-0.5"}`}
        />
      </button>
    </div>
  );
}

function PlayCountPicker({
  label,
  desc,
  localStorageKey,
  defaultValue,
}: {
  label: string;
  desc: string;
  localStorageKey: string;
  defaultValue: number;
}) {
  const [count, setCount] = useState(() => getLsNumber(localStorageKey, defaultValue));

  const options = [1, 2, 3];

  const pick = (n: number) => {
    setCount(n);
    setLs(localStorageKey, String(n));
  };

  return (
    <div className="flex items-center justify-between p-4 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-800">
      <div>
        <div className="font-medium">{label}</div>
        <div className="text-xs text-gray-500">{desc}</div>
      </div>
      <div className="flex items-center gap-1 bg-gray-200 dark:bg-gray-800 rounded-lg p-0.5">
        {options.map((n) => (
          <button
            key={n}
            onClick={() => pick(n)}
            className={`w-9 h-8 rounded-md text-sm font-medium transition-all
              ${count === n
                ? "bg-white dark:bg-gray-700 text-fuchsia-600 shadow-sm"
                : "text-gray-500 hover:text-gray-700 dark:hover:text-gray-300"
              }`}
          >
            {n}次
          </button>
        ))}
      </div>
    </div>
  );
}

const TTS_VOICES = [
  { id: "en-US-JennyNeural",   label: "Jenny (美式·女)",   accent: "🇺🇸" },
  { id: "en-US-GuyNeural",     label: "Guy (美式·男)",     accent: "🇺🇸" },
  { id: "en-US-AriaNeural",    label: "Aria (美式·女)",    accent: "🇺🇸" },
  { id: "en-US-DavisNeural",   label: "Davis (美式·男)",   accent: "🇺🇸" },
  { id: "en-GB-SoniaNeural",   label: "Sonia (英式·女)",   accent: "🇬🇧" },
  { id: "en-GB-RyanNeural",    label: "Ryan (英式·男)",    accent: "🇬🇧" },
];

function VoicePicker({
  label,
  desc,
  localStorageKey,
  defaultValue,
}: {
  label: string;
  desc: string;
  localStorageKey: string;
  defaultValue: string;
}) {
  const [voice, setVoice] = useState(() => {
    if (typeof window === "undefined") return defaultValue;
    return localStorage.getItem(localStorageKey) || defaultValue;
  });

  const pick = (id: string) => {
    setVoice(id);
    setLs(localStorageKey, id);
  };

  return (
    <div className="p-4 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-800 space-y-2">
      <div>
        <div className="font-medium">{label}</div>
        <div className="text-xs text-gray-500">{desc}</div>
      </div>
      <div className="grid grid-cols-2 gap-1.5">
        {TTS_VOICES.map((v) => (
          <button
            key={v.id}
            onClick={() => pick(v.id)}
            className={`text-left px-3 py-2 rounded-lg text-sm transition-all border
              ${voice === v.id
                ? "border-fuchsia-400 bg-fuchsia-50 dark:bg-fuchsia-950/30 text-fuchsia-700 dark:text-fuchsia-300"
                : "border-transparent bg-white dark:bg-gray-800 hover:border-gray-300 dark:hover:border-gray-600 text-gray-700 dark:text-gray-300"
              }`}
          >
            <span className="mr-1">{v.accent}</span>
            {v.label}
          </button>
        ))}
      </div>
    </div>
  );
}
