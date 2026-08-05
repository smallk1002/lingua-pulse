// ============================================================
// Game Store - 游戏核心状态管理
// ============================================================

import { create } from "zustand";
import type {
  GameMode,
  Difficulty,
  GamePhase,
  GameStatus,
  Statement,
  WordSlot,
  GameResult,
  Course,
} from "@/lib/types";
import { saveProgress, checkAnswer, submitReview } from "@/lib/api";

interface GameState {
  // 游戏配置
  coursePackId: string | null;
  courseId: string | null;
  mode: GameMode;
  difficulty: Difficulty;
  voice: string;

  // 课程数据
  course: Course | null;
  statements: Statement[];
  visibleStatements: Statement[]; // 未被掌握的句子
  currentStatementIndex: number;
  totalStatements: number;

  // 游戏状态
  status: GameStatus;
  phase: GamePhase;

  // 当前句子
  wordSlots: WordSlot[];
  isComposing: boolean;
  isLastWord: boolean;
  showAnswer: boolean;

  // Fix 模式
  fixSlots: WordSlot[];
  fixIndex: number;
  fixCount: number;  // 当前句子的 Fix 次数

  // 结果
  results: GameResult[];
  xpEarned: number;
  combo: number;          // 连续全对次数
  showCombo: number | null; // 触发 combo 动画的值（短暂显示后清 null）
  errorsPerStatement: Map<string, number>;

  // 计时
  startTime: string | null;
  elapsedSeconds: number;

  // 错误通知
  syncError: string | null;

  // 进度保存去重
  _saveProgressSeq: number;

  // Actions
  initGame: (
    course: Course,
    coursePackId: string,
    mode: GameMode,
    difficulty: Difficulty
  ) => void;
  setMode: (mode: GameMode) => void;
  setDifficulty: (difficulty: Difficulty) => void;
  startGame: () => void;
  pauseGame: () => void;
  resumeGame: () => void;
  nextStatement: () => void;
  prevStatement: () => void;
  retryStatement: () => void;

  // 单词输入
  buildWordSlots: (sentence: string) => void;
  setWordSlots: (slots: WordSlot[]) => void;
  setComposing: (v: boolean) => void;
  setIsLastWord: (v: boolean) => void;
  toggleShowAnswer: () => void;

  // 提交
  submitAnswer: () => void;
  onFixCorrect: () => void;
  triggerCombo: (combo: number) => void;

  // 结算
  completeCourse: () => void;
  resetCourse: () => void;
  addResult: (result: GameResult) => void;

  // 辅助
  getCurrentStatement: () => Statement | null;
  getProgress: () => number;
  clearSyncError: () => void;
}

const getSavedMode = (): GameMode => {
  try { return (localStorage.getItem("gameMode") as GameMode) || "chinese_to_english"; }
  catch { return "chinese_to_english"; }
};
const getSavedDifficulty = (): Difficulty => {
  try { return (localStorage.getItem("gameDifficulty") as Difficulty) || "intermediate"; }
  catch { return "intermediate"; }
};

export const useGameStore = create<GameState>((set, get) => ({
  coursePackId: null,
  courseId: null,
  mode: getSavedMode(),
  difficulty: getSavedDifficulty(),
  voice: "en-US-JennyNeural",

  course: null,
  statements: [],
  visibleStatements: [],
  currentStatementIndex: 0,
  totalStatements: 0,

  status: "idle",
  phase: "question",

  wordSlots: [],
  isComposing: false,
  isLastWord: false,
  showAnswer: false,

  fixSlots: [],
  fixIndex: 0,
  fixCount: 0,

  results: [],
  xpEarned: 0,
  combo: 0,
  showCombo: null,
  errorsPerStatement: new Map(),

  startTime: null,
  elapsedSeconds: 0,

  syncError: null,
  _saveProgressSeq: 0,

  // ---- 初始化 ----
  initGame: (course, coursePackId, mode, difficulty) => {
    const visible = course.statements.filter(
      () => true /* MVP: 不过滤已掌握 */
    );
    // 断点续学：优先使用后端进度，其次 localStorage
    const savedIdx =
      course.progress?.statement_index ??
      (() => {
        try {
          const v = localStorage.getItem(`progress_${course.id}`);
          return v ? parseInt(v, 10) : null;
        } catch { return null; }
      })() ?? 0;

    // TTS 语音：从 localStorage 读取
    const savedVoice =
      (() => {
        try {
          return localStorage.getItem("ttsVoice");
        } catch { return null; }
      })() ?? "en-US-JennyNeural";

    set({
      course,
      coursePackId,
      courseId: course.id,
      mode,
      difficulty,
      voice: savedVoice,
      statements: course.statements,
      visibleStatements: visible,
      totalStatements: visible.length,
      currentStatementIndex: Math.min(savedIdx, visible.length - 1),
      status: "idle",
      phase: "question",
      results: [],
      xpEarned: 0,
      errorsPerStatement: new Map(),
      showAnswer: false,
      combo: 0,
      showCombo: null,
    });
  },

  setMode: (mode) => {
    try { localStorage.setItem("gameMode", mode); } catch {}
    set({ mode });
  },
  setDifficulty: (difficulty) => {
    try { localStorage.setItem("gameDifficulty", difficulty); } catch {}
    set({ difficulty });
  },

  startGame: () => {
    const state = get();
    const stmt = state.visibleStatements[state.currentStatementIndex];
    if (stmt) {
      get().buildWordSlots(stmt.english);
    }
    set({
      status: "playing",
      startTime: new Date().toISOString(),
      elapsedSeconds: 0,
    });
  },

  pauseGame: () => set({ status: "paused" }),
  resumeGame: () => set({ status: "playing" }),

  nextStatement: () => {
    const { currentStatementIndex, visibleStatements, courseId } = get();
    if (currentStatementIndex < visibleStatements.length - 1) {
      const nextIdx = currentStatementIndex + 1;
      const stmt = visibleStatements[nextIdx];
      get().buildWordSlots(stmt.english);
      set({
        currentStatementIndex: nextIdx,
        phase: "question",
        showAnswer: false,
      });

      // 保存进度：后端 + localStorage（带序号防竞态）
      if (courseId) {
        const seq = get()._saveProgressSeq + 1;
        set({ _saveProgressSeq: seq });

        saveProgress(courseId, nextIdx)
          .then(() => {
            // 只有序号最大的那次才写 localStorage，避免旧请求回退进度
            if (get()._saveProgressSeq === seq) {
              try {
                localStorage.setItem(`progress_${courseId}`, String(nextIdx));
              } catch { /* ignore */ }
            }
          })
          .catch((e) => {
            console.warn("[GameStore] saveProgress failed:", e);
          });
      }
    } else {
      // 全部完成
      set({ status: "completed" });
    }
  },

  prevStatement: () => {
    const { currentStatementIndex } = get();
    if (currentStatementIndex > 0) {
      set({ currentStatementIndex: currentStatementIndex - 1 });
    }
  },

  retryStatement: () => {
    const { visibleStatements, currentStatementIndex } = get();
    const stmt = visibleStatements[currentStatementIndex];
    if (stmt) {
      get().buildWordSlots(stmt.english);
      set({ phase: "question", showAnswer: false });
    }
  },

  // ---- 单词输入 ----
  buildWordSlots: (sentence: string) => {
    const words = sentence.split(" ");
    const slots: WordSlot[] = words.map((word, i) => ({
      id: i,
      target: word,
      userInput: "",
      status: i === 0 ? "active" : "pending",
      start: words.slice(0, i).join(" ").length + (i > 0 ? 1 : 0),
      end: words.slice(0, i + 1).join(" ").length,
    }));
    set({ wordSlots: slots, fixSlots: [], fixIndex: 0, fixCount: 0, isLastWord: words.length === 1 });
  },

  setWordSlots: (slots) => set({ wordSlots: slots }),
  setComposing: (v) => set({ isComposing: v }),
  setIsLastWord: (v) => set({ isLastWord: v }),
  toggleShowAnswer: () =>
    set((s) => ({ showAnswer: !s.showAnswer })),

  // ---- 提交 ----
  submitAnswer: () => {
    const { wordSlots, phase, results, errorsPerStatement, visibleStatements, currentStatementIndex, fixCount, difficulty } = get();
    const stmt = visibleStatements[currentStatementIndex];

    /** 上报答题结果到后端（fire-and-forget，不阻塞 UI） */
    const reportToServer = (userInput: string, fc: number, quality: number) => {
      // 1. 上报答题检查
      const token = typeof window !== "undefined" ? localStorage.getItem("access_token") : null;
      if (!token) return; // 未登录不报

      checkAnswer({
        statement_id: stmt.id,
        user_input: userInput,
        difficulty,
        fix_count: fc,
      }).catch((e) => {
        console.warn("[GameStore] checkAnswer failed:", e);
        set({ syncError: "答题记录上报失败，数据将在下次同步" });
      });

      // 2. 上报 SM-2 复习评分（quality >= 3 才需要）
      if (quality >= 3) {
        submitReview({ statement_id: stmt.id, quality }).catch((e) => {
          console.warn("[GameStore] submitReview failed:", e);
        });
      }
    };

    // 构建用户输入的完整字符串
    const buildUserInput = (slots: WordSlot[]): string =>
      slots.map((s) => s.userInput).join(" ");

    if (phase === "question") {
      // 检查每个单词是否正确
      const newSlots = wordSlots.map((slot) => ({
        ...slot,
        status:
          slot.userInput.toLowerCase().trim() === slot.target.toLowerCase()
            ? ("correct" as const)
            : ("incorrect" as const),
      }));

      const hasError = newSlots.some((s) => s.status === "incorrect");

      if (hasError) {
        // 进入 Fix 模式
        // 出错了，重置 combo
        set({ combo: 0 });
        const fixSlots = newSlots.filter((s) => s.status === "incorrect");
        // 重置错误单词的输入，第一个设为 active
        const resetFixSlots = fixSlots.map((s, i) => ({
          ...s,
          userInput: "",
          status: i === 0 ? ("active" as const) : ("incorrect" as const),
        }));
        // 为 fix 状态准备完整的 slots（用于显示）
        const currentErrors = errorsPerStatement.get(stmt.id) ?? 0;
        const newErrors = new Map(errorsPerStatement);
        newErrors.set(stmt.id, currentErrors + 1);
        set({
          wordSlots: newSlots,
          phase: "fix",
          fixSlots: resetFixSlots,
          fixIndex: 0,
          fixCount: fixCount + 1,
          errorsPerStatement: newErrors,
        });
      } else {
        // 全部正确 → Answer 阶段
        const quality = 5;
        const newCombo = get().combo + 1;
        const newResults = [
          ...results,
          { statement_id: stmt.id, quality, interval: 0, ease_factor: 2.5, repetitions: 0 },
        ];
        set({
          wordSlots: newSlots,
          phase: "answer",
          fixSlots: [],
          results: newResults,
          xpEarned: get().xpEarned + 10,
          combo: newCombo,
        });

        // 上报后端
        reportToServer(buildUserInput(newSlots), fixCount, quality);

        // 触发 combo 动画（延迟一下，等 answer 渲染完）
        setTimeout(() => get().triggerCombo(newCombo), 100);
      }
    } else if (phase === "fix") {
      // Fix 阶段再次提交
      const { fixSlots, wordSlots } = get();
      const allCorrect = fixSlots.every(
        (slot) =>
          slot.userInput.toLowerCase().trim() === slot.target.toLowerCase()
      );

      // 更新主 wordSlots 中的 fix 槽位
      const updatedSlots = wordSlots.map((s) => {
        const fixSlot = fixSlots.find((f) => f.id === s.id);
        if (fixSlot) {
          return {
            ...s,
            userInput: fixSlot.userInput,
            status:
              fixSlot.userInput.toLowerCase().trim() ===
              fixSlot.target.toLowerCase()
                ? ("correct" as const)
                : ("incorrect" as const),
          };
        }
        return s;
      });

      if (allCorrect) {
        // 修复后正确，combo 重置
        const quality = fixCount <= 1 ? 4 : fixCount <= 2 ? 3 : 2;
        const newResults = [
          ...results,
          { statement_id: stmt.id, quality, interval: 0, ease_factor: 2.5, repetitions: 0 },
        ];
        set({
          wordSlots: updatedSlots,
          phase: "answer",
          fixSlots: [],
          results: newResults,
          xpEarned: get().xpEarned + 5,
        });

        // 上报后端（fix 后的总计数）
        reportToServer(buildUserInput(updatedSlots), fixCount, quality);
      } else {
        // 还是有问题，保持在 fix 模式
        const stillWrong = fixSlots.filter(
          (slot) =>
            slot.userInput.toLowerCase().trim() !== slot.target.toLowerCase()
        );
        set({
          wordSlots: updatedSlots,
          fixSlots: stillWrong.map((s, i) => ({
            ...s,
            userInput: "",
            status: i === 0 ? ("active" as const) : ("incorrect" as const),
          })),
          fixCount: fixCount + 1,
        });
      }
    }
    // answer 阶段什么都不做，等用户点下一题
  },

  onFixCorrect: () => {
    // Fix 中某个单词被纠正后自动推进到下一个 fix 单词
    const { fixSlots, fixIndex } = get();
    if (fixIndex < fixSlots.length) {
      set({ fixIndex: fixIndex + 1 });
    }
  },

  triggerCombo: (combo) => {
    set({ showCombo: combo });
    // 2 秒后清除
    setTimeout(() => set({ showCombo: null }), 2000);
  },

  completeCourse: () => set({ status: "completed" }),
  resetCourse: () => {
    const { course, coursePackId, mode, difficulty } = get();
    if (course) {
      get().initGame(course, coursePackId!, mode, difficulty);
    }
  },

  addResult: (result) =>
    set((s) => ({ results: [...s.results, result] })),

  getCurrentStatement: () => {
    const { visibleStatements, currentStatementIndex } = get();
    return visibleStatements[currentStatementIndex] ?? null;
  },

  getProgress: () => {
    const { currentStatementIndex, totalStatements } = get();
    if (totalStatements === 0) return 0;
    return Math.round((currentStatementIndex / totalStatements) * 100);
  },

  clearSyncError: () => set({ syncError: null }),
}));
