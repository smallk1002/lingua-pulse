// ============================================================
// Download Page - 桌面客户端下载
// ============================================================

"use client";

import Link from "next/link";
import { useEffect, useState } from "react";

type Platform = "windows" | "macos" | "other";

const DOWNLOADS = {
  windows: {
    name: "Windows",
    desc: "适用于 Windows 10/11（64 位）",
    file: "/downloads/LinguaPulse_1.0.0_x64-setup.exe",
    icon: "🪟",
  },
  macos: {
    name: "macOS",
    desc: "适用于 Apple Silicon（M 系列芯片）",
    file: "/downloads/LinguaPulse_1.0.0_macOS.dmg",
    icon: "🍎",
  },
};

export default function DownloadPage() {
  const [platform, setPlatform] = useState<Platform>("other");

  useEffect(() => {
    const ua = navigator.userAgent.toLowerCase();
    if (ua.includes("win")) setPlatform("windows");
    else if (ua.includes("mac")) setPlatform("macos");
  }, []);

  const primary = platform === "windows" ? DOWNLOADS.windows : DOWNLOADS.macos;
  const secondary = platform === "windows" ? DOWNLOADS.macos : DOWNLOADS.windows;

  return (
    <div className="max-w-2xl mx-auto px-4 py-20">
      <img
        src="/logo.png"
        alt="LinguaPulse"
        className="w-20 h-20 mx-auto mb-6 rounded-2xl shadow-md"
      />
      <h1 className="text-3xl font-bold text-center mb-2">下载桌面客户端</h1>
      <p className="text-center text-gray-500 mb-10">
        独立窗口 · 专注学习 · 仅 3MB 极致轻量
      </p>

      {platform !== "other" && (
        <a
          href={primary.file}
          download
          className="block w-full text-center py-4 mb-4 bg-fuchsia-600 text-white
                     rounded-xl font-semibold text-lg hover:bg-fuchsia-700
                     transition-colors shadow-lg shadow-fuchsia-500/25"
        >
          {primary.icon} 下载 {primary.name} 版
          <span className="block text-xs font-normal opacity-80 mt-1">
            {primary.desc}（检测到你的系统）
          </span>
        </a>
      )}

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-10">
        {[DOWNLOADS.windows, DOWNLOADS.macos].map((item) => (
          <a
            key={item.name}
            href={item.file}
            download
            className="p-5 rounded-xl border border-gray-200 dark:border-gray-700
                       hover:border-fuchsia-400 dark:hover:border-fuchsia-500
                       transition-colors text-center"
          >
            <div className="text-3xl mb-2">{item.icon}</div>
            <div className="font-semibold">{item.name}</div>
            <div className="text-xs text-gray-500 mt-1">{item.desc}</div>
          </a>
        ))}
      </div>

      <div className="text-sm text-gray-500 space-y-2 bg-gray-50 dark:bg-gray-900 rounded-xl p-5">
        <p className="font-medium text-gray-700 dark:text-gray-300">安装说明</p>
        <p>Windows：双击安装包按提示完成安装即可</p>
        <p>
          macOS：打开 dmg 后将 LinguaPulse 拖入应用程序文件夹；如提示"无法验证开发者"，
          右键点击应用选择"打开"即可
        </p>
      </div>

      <p className="text-center text-sm text-gray-500 mt-8">
        <Link href="/auth/login" className="text-fuchsia-600 hover:underline">
          ← 返回登录
        </Link>
      </p>
    </div>
  );
}
