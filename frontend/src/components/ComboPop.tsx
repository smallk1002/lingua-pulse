// ============================================================
// ComboPop - 连击激励反馈（浮动文字 + 音效）
// ============================================================

"use client";

import { useEffect, useRef } from "react";
import { useGameStore } from "@/stores/gameStore";

// --- 里程碑配置 ---
interface ComboMilestone {
  min: number;
  text: string;
  emoji: string;
  color: string;
  scale: number;
}

const MILESTONES: ComboMilestone[] = [
  { min: 3,  text: "不错！",  emoji: "👏", color: "text-green-500",  scale: 1.0 },
  { min: 5,  text: "很棒！",  emoji: "🔥", color: "text-blue-500",   scale: 1.1 },
  { min: 10, text: "完美！",  emoji: "✨", color: "text-purple-500", scale: 1.2 },
  { min: 15, text: "无敌！",  emoji: "💎", color: "text-amber-500",  scale: 1.3 },
  { min: 20, text: "大神！",  emoji: "👑", color: "text-rose-500",   scale: 1.4 },
];

function getMilestone(combo: number): ComboMilestone | null {
  for (let i = MILESTONES.length - 1; i >= 0; i--) {
    if (combo >= MILESTONES[i].min) return MILESTONES[i];
  }
  return null;
}

// --- Web Audio 音效 ---
function playComboSound(combo: number) {
  try {
    const ctx = new AudioContext();
    // 音高随 combo 递增
    const baseFreq = 400 + combo * 20;
    const frequencies = [baseFreq, baseFreq * 1.25, baseFreq * 1.5];

    frequencies.forEach((freq, i) => {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = "sine";
      osc.frequency.value = freq;
      gain.gain.setValueAtTime(0.3, ctx.currentTime + i * 0.08);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + i * 0.08 + 0.3);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(ctx.currentTime + i * 0.08);
      osc.stop(ctx.currentTime + i * 0.08 + 0.3);
    });

    // 自动关闭 context
    setTimeout(() => ctx.close(), 1000);
  } catch {
    // 静默失败
  }
}

// --- 组件 ---
export default function ComboPop() {
  const showCombo = useGameStore((s) => s.showCombo);
  const prevComboRef = useRef<number | null>(null);

  useEffect(() => {
    if (showCombo !== null && showCombo !== prevComboRef.current) {
      prevComboRef.current = showCombo;
      const ms = getMilestone(showCombo);
      if (ms) {
        playComboSound(showCombo);
      }
    }
  }, [showCombo]);

  const ms = showCombo ? getMilestone(showCombo) : null;
  if (!ms || showCombo === null) return null;

  return (
    <div className="fixed inset-0 z-40 pointer-events-none flex items-center justify-center">
      <div
        key={showCombo}
        className="flex flex-col items-center gap-1 animate-combo-pop"
        style={{ "--combo-scale": ms.scale } as React.CSSProperties}
      >
        <div className="text-5xl animate-bounce-in">{ms.emoji}</div>
        <div className={`text-4xl font-black drop-shadow-lg ${ms.color}`}>
          {ms.text}
        </div>
        <div className="text-sm text-gray-400 font-medium">
          连续 {showCombo} 题全对！
        </div>
      </div>
    </div>
  );
}
