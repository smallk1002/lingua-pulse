// ============================================================
// Game Page - 游戏答题页
// ============================================================

"use client";

import { useEffect, useState, useCallback, useRef, Suspense } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import Link from "next/link";
import { useAuthStore } from "@/stores/authStore";
import { useGameStore } from "@/stores/gameStore";
import { reportSession } from "@/lib/api";
import { useKeyboard } from "@/hooks/useKeyboard";
import { usePlayTipSound } from "@/hooks/useTypingSound";
import { useQuery } from "@tanstack/react-query";
import { getCourse, getTtsUrl, completeCourse, saveProgress } from "@/lib/api";
import { QuestionInput } from "@/components/QuestionInput";
import ComboPop from "@/components/ComboPop";
import type { GameMode, Difficulty } from "@/lib/types";

export default function GamePageWrapper() {
  return (
    <Suspense
      fallback={
        <div className="flex items-center justify-center min-h-[80vh]">
          <div className="animate-pulse text-fuchsia-600 text-lg">加载游戏...</div>
        </div>
      }
    >
      <GamePage />
    </Suspense>
  );
}

function GamePage() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const { isAuthenticated, isLoading: authLoading } = useAuthStore();

  const coursePackId = searchParams.get("coursePackId") ?? "";
  const courseId = searchParams.get("courseId") ?? "";
  const urlMode = searchParams.get("mode") as GameMode | null;
  const urlDifficulty = searchParams.get("difficulty") as Difficulty | null;

  const {
    status,
    phase,
    currentStatementIndex,
    totalStatements,
    statements,
    results,
    mode,
    xpEarned,
    combo,
    course,
    initGame,
    startGame,
    pauseGame,
    resumeGame,
    resetCourse,
    getCurrentStatement,
    getProgress,
    setMode,
  } = useGameStore();

  const { playRightSound, playErrorSound } = usePlayTipSound();
  useKeyboard();

  const [isSubmitting, setIsSubmitting] = useState(false);
  const [pausedOverlay, setPausedOverlay] = useState(false);
  const ttsAudioRef = useRef<HTMLAudioElement | null>(null);
  const activeAudiosRef = useRef<Set<HTMLAudioElement>>(new Set());

  // 停止所有正在播放的 TTS
  const stopAllTTS = useCallback(() => {
    if (ttsAudioRef.current) {
      ttsAudioRef.current.pause();
      ttsAudioRef.current.currentTime = 0;
    }
    activeAudiosRef.current.forEach((a) => {
      a.pause();
      a.currentTime = 0;
    });
    activeAudiosRef.current.clear();
  }, []);

  // Auth check
  useEffect(() => {
    if (!authLoading && !isAuthenticated) {
      router.replace("/auth/login");
    }
  }, [authLoading, isAuthenticated, router]);

  // Load course data
  const { data: courseData, isLoading: courseLoading, error } = useQuery({
    queryKey: ["course", coursePackId, courseId],
    queryFn: () => getCourse(coursePackId, courseId),
    enabled: !!courseId && isAuthenticated,
  });

  // Init game when course loaded
  useEffect(() => {
    if (courseData) {
      const initMode = urlMode ?? mode;
      const initDifficulty = urlDifficulty ?? "intermediate";
      initGame(courseData, coursePackId, initMode, initDifficulty);
      if (urlMode) setMode(urlMode);
    }
  }, [courseData]);

  // Auto-start game
  useEffect(() => {
    if (status === "idle" && statements.length > 0) {
      startGame();
    }
  }, [status, statements, startGame]);

  // 课程完成时上报学习会话（驱动课程包排序 & 统计时长）
  useEffect(() => {
    if (status === "completed") {
      const state = useGameStore.getState();
      reportSession({
        duration: state.elapsedSeconds || 0,
        statements_count: state.results.length,
        course_id: state.courseId,
      }).catch(() => {});
    }
  }, [status]);

  // 学习时长计时器（每秒 tick）
  useEffect(() => {
    if (status !== "playing") return;
    const interval = setInterval(() => {
      useGameStore.setState((s) => ({
        elapsedSeconds: (s.elapsedSeconds || 0) + 1,
      }));
    }, 1000);
    return () => clearInterval(interval);
  }, [status]);

  // Phase change effects (sounds)
  const prevPhaseRef = useRef(phase);
  useEffect(() => {
    if (prevPhaseRef.current === "question" && phase === "fix") {
      playErrorSound();
    } else if (prevPhaseRef.current === "fix" && phase === "answer") {
      playRightSound();
    } else if (prevPhaseRef.current === "question" && phase === "answer") {
      playRightSound();
    }
    prevPhaseRef.current = phase;
  }, [phase, playRightSound, playErrorSound]);

  // TTS playback (支持多播)
  const getVoice = useCallback(() => {
    try {
      return localStorage.getItem("ttsVoice") || "en-US-JennyNeural";
    } catch {
      return "en-US-JennyNeural";
    }
  }, []);

  const playTTS = useCallback(() => {
    stopAllTTS();
    const stmt = getCurrentStatement();
    if (!stmt) return;
    const url = getTtsUrl(stmt.english, getVoice());
    if (!ttsAudioRef.current) {
      ttsAudioRef.current = new Audio();
    }
    ttsAudioRef.current.src = url;
    ttsAudioRef.current.play().catch(() => {});
  }, [getCurrentStatement, getVoice, stopAllTTS]);

  // 播放 N 次 TTS，间隔 800ms
  const playTTSMulti = useCallback(() => {
    let playCount = 1;
    if (mode === "dictation") {
      const raw = localStorage.getItem("dictationPlayCount");
      playCount = raw ? Math.max(1, Math.min(3, parseInt(raw, 10) || 1)) : 2;
    }

    let times = 0;
    const voice = getVoice();
    const playOnce = () => {
      if (times >= playCount) return;
      times++;
      const stmt = getCurrentStatement();
      if (!stmt) return;
      const url = getTtsUrl(stmt.english, voice);
      const a = new Audio(url);
      a.play().catch(() => {});
      a.onended = () => {
        if (times < playCount) {
          setTimeout(playOnce, 600);
        }
      };
      // 兜底：2s 后下一轮
      setTimeout(() => {
        if (times < playCount && a.paused) playOnce();
      }, 2500);
    };
    playOnce();
  }, [mode, getCurrentStatement, getVoice]);

  // 自动播放：进入新题目时朗读发音
  const prevStmtIndexRef = useRef(currentStatementIndex);
  const hasAutoPlayed = useRef(false);
  useEffect(() => {
    if (status !== "playing") {
      hasAutoPlayed.current = false;
      return;
    }

    const isFirstMount = !hasAutoPlayed.current;
    const isNewStatement = prevStmtIndexRef.current !== currentStatementIndex;

    if (isFirstMount || isNewStatement) {
      hasAutoPlayed.current = true;
      prevStmtIndexRef.current = currentStatementIndex;
      // 立刻停止上一题的 TTS，避免延迟
      stopAllTTS();
      const timer = setTimeout(() => {
        // 直接从 store 读，避免依赖 playTTS/playTTSMulti 导致 effect 重入清 timer
        const state = useGameStore.getState();
        const stmt = state.visibleStatements[state.currentStatementIndex];
        if (!stmt) return;

        const voice =
          (() => {
            try { return localStorage.getItem("ttsVoice") || "en-US-JennyNeural"; }
            catch { return "en-US-JennyNeural"; }
          })();

        if (state.mode === "dictation") {
          const raw = localStorage.getItem("dictationPlayCount");
          const playCount = raw ? Math.max(1, Math.min(3, parseInt(raw, 10) || 1)) : 2;
          let times = 0;
          const playOnce = () => {
            if (times >= playCount) return;
            times++;
            const a = new Audio(getTtsUrl(stmt.english, voice));
            activeAudiosRef.current.add(a);
            a.play().catch(() => {});
            a.onended = () => {
              activeAudiosRef.current.delete(a);
              if (times < playCount) setTimeout(playOnce, 600);
            };
            setTimeout(() => { if (times < playCount && a.paused) playOnce(); }, 2500);
          };
          playOnce();
        } else {
          const url = getTtsUrl(stmt.english, voice);
          if (!ttsAudioRef.current) {
            ttsAudioRef.current = new Audio();
          }
          ttsAudioRef.current.src = url;
          ttsAudioRef.current.play().catch(() => {});
        }
      }, 400);
      return () => clearTimeout(timer);
    }
  }, [currentStatementIndex, status, mode, stopAllTTS]);

  // Listen for global play-tts event
  useEffect(() => {
    const handler = () => playTTS();
    window.addEventListener("play-tts", handler);
    return () => window.removeEventListener("play-tts", handler);
  }, [playTTS]);

  // 离开页面时保存进度
  useEffect(() => {
    const saveCurrentProgress = () => {
      const { courseId, currentStatementIndex: idx } = useGameStore.getState();
      if (courseId) {
        // 同步到后端
        saveProgress(courseId, idx).catch(() => {});
        // 保存到 localStorage
        try {
          localStorage.setItem(`progress_${courseId}`, String(idx));
        } catch { /* ignore */ }
      }
    };
    window.addEventListener("beforeunload", saveCurrentProgress);
    window.addEventListener("pagehide", saveCurrentProgress);
    return () => {
      saveCurrentProgress(); // 组件卸载时也保存
      window.removeEventListener("beforeunload", saveCurrentProgress);
      window.removeEventListener("pagehide", saveCurrentProgress);
    };
  }, []);

  // Submit results when course complete
  const handleComplete = useCallback(async () => {
    if (isSubmitting) return;
    setIsSubmitting(true);
    try {
      const res = await completeCourse(courseId, results);
      useGameStore.setState({
        xpEarned: (useGameStore.getState().xpEarned || 0) + (res.xp_awarded || 0),
      });
    } catch {
      // 即使提交失败也显示结算页
    } finally {
      setIsSubmitting(false);
    }
  }, [courseId, results, isSubmitting]);

  useEffect(() => {
    if (status === "completed") {
      handleComplete();
    }
  }, [status, handleComplete]);

  // Loading state
  if (authLoading || courseLoading) {
    return (
      <div className="flex items-center justify-center min-h-[80vh]">
        <div className="animate-pulse text-fuchsia-600 text-lg">加载课程...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="max-w-2xl mx-auto px-4 py-20 text-center">
        <p className="text-red-500 mb-4">加载课程失败</p>
        <Link href="/home" className="text-fuchsia-600 hover:underline">
          返回主页
        </Link>
      </div>
    );
  }

  if (!courseData) return null;

  const progress = getProgress();
  const statement = getCurrentStatement();

  // ---- 暂停遮罩 ----
  if (pausedOverlay || status === "paused") {
    return (
      <div className="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex items-center justify-center">
        <div className="bg-white dark:bg-gray-900 rounded-2xl p-10 text-center shadow-2xl max-w-sm mx-4">
          <div className="text-6xl mb-4">⏸️</div>
          <h2 className="text-2xl font-bold mb-2">已暂停</h2>
          <p className="text-gray-500 mb-6">休息一下，随时继续</p>
          <div className="flex gap-3 justify-center">
            <button
              onClick={() => {
                resumeGame();
                setPausedOverlay(false);
              }}
              className="px-6 py-2 bg-fuchsia-600 text-white rounded-xl font-semibold
                         hover:bg-fuchsia-700 transition-colors"
            >
              继续学习
            </button>
            <Link
              href="/home"
              className="px-6 py-2 border border-gray-300 dark:border-gray-700 rounded-xl
                         hover:border-fuchsia-300 transition-colors"
            >
              退出
            </Link>
          </div>
        </div>
      </div>
    );
  }

  // ---- 完成结算 ----
  if (status === "completed") {
    return (
      <div className="max-w-2xl mx-auto px-4 py-16 text-center">
        <div className="text-6xl mb-6">🎉</div>
        <h1 className="text-3xl font-bold mb-2">课程完成！</h1>
        <p className="text-gray-500 mb-8">
          你完成了 {courseData.title} 的全部 {totalStatements} 道题
        </p>

        <div className="grid grid-cols-2 gap-4 max-w-xs mx-auto mb-10">
          <div className="p-4 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-800">
            <div className="text-2xl font-bold text-fuchsia-600">+{xpEarned}</div>
            <div className="text-xs text-gray-400">获得 XP</div>
          </div>
          <div className="p-4 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-800">
            <div className="text-2xl font-bold text-green-500">
              {results.filter((r) => r.quality >= 4).length}/{results.length}
            </div>
            <div className="text-xs text-gray-400">一次通过</div>
          </div>
        </div>

        <div className="flex gap-3 justify-center">
          <button
            onClick={() => {
              resetCourse();
              startGame();
            }}
            className="px-8 py-3 bg-fuchsia-600 text-white rounded-xl font-semibold
                       hover:bg-fuchsia-700 transition-colors"
          >
            🔄 再来一次
          </button>
          <Link
            href="/home"
            className="px-8 py-3 border border-gray-300 dark:border-gray-700 rounded-xl
                       font-semibold hover:border-fuchsia-300 transition-colors"
          >
            返回主页
          </Link>
        </div>
      </div>
    );
  }

  // ---- 游戏界面 ----
  return (
    <div className="max-w-4xl mx-auto px-4 py-4">
      {/* 顶部工具栏 */}
      <div className="flex items-center justify-between mb-4 text-sm">
        <Link
          href={`/start?coursePackId=${coursePackId}`}
          className="text-gray-400 hover:text-fuchsia-600 transition-colors"
        >
          ← 选课
        </Link>

        <div className="flex items-center gap-2">
          {/* 模式切换 */}
          <button
            onClick={() => {
              const next = mode === "chinese_to_english" ? "dictation" : "chinese_to_english";
              setMode(next);
            }}
            className="text-gray-400 hover:text-fuchsia-600 transition-colors text-xs px-2 py-1 rounded
                       border border-gray-200 dark:border-gray-700"
            title="切换练习模式"
          >
            {mode === "chinese_to_english" ? "🇨🇳→🇬🇧 中译英" : "🎧 听写"}
          </button>
          <span className="font-medium">{courseData.title}</span>
          <span className="text-gray-400 ml-1">
            ({currentStatementIndex + 1}/{totalStatements})
          </span>
          {combo >= 2 && (
            <span className="ml-2 px-1.5 py-0.5 bg-amber-100 dark:bg-amber-900/40 text-amber-700 dark:text-amber-300 text-xs rounded font-bold">
              🔥×{combo}
            </span>
          )}
        </div>

        <div className="flex items-center gap-3">
          <button
            onClick={() => setPausedOverlay(true)}
            className="text-gray-400 hover:text-fuchsia-600 transition-colors"
          >
            ⏸ 暂停
          </button>
          <button
            onClick={() => {
              if (confirm("确定要重置当前课程进度吗？")) {
                resetCourse();
                startGame();
              }
            }}
            className="text-gray-400 hover:text-red-500 transition-colors"
          >
            ↺ 重置
          </button>
        </div>
      </div>

      {/* 进度条 */}
      <div className="w-full h-1.5 bg-gray-200 dark:bg-gray-800 rounded-full mb-8 overflow-hidden">
        <div
          className="h-full bg-gradient-to-r from-fuchsia-500 to-purple-500 rounded-full transition-all duration-300"
          style={{ width: `${progress}%` }}
        />
      </div>

      {/* 核心输入区 */}
      <QuestionInput />

      {/* 发音按钮（浮动） */}
      {mode === "chinese_to_english" && (
        <button
          onClick={playTTS}
          className="fixed bottom-6 right-6 w-12 h-12 bg-fuchsia-600 text-white
                     rounded-full shadow-lg hover:bg-fuchsia-700 transition-colors
                     flex items-center justify-center text-xl active:scale-95"
          title="播放发音 (Ctrl+J)"
        >
          🔊
        </button>
      )}
      <ComboPop />
    </div>
  );
}
