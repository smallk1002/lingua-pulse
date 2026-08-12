// ============================================================
// LinguaPulse 前端核心类型定义
// ============================================================

// ---- 用户 & 认证 ----
export interface User {
  id: string;
  email: string;
  username: string;
  is_active: boolean;
  created_at: string;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
  user: User;
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface RegisterRequest {
  email: string;
  username: string;
  password: string;
  code: string;
}

// ---- 课程 ----
export interface CoursePack {
  id: string;
  title: string;
  description: string | null;
  cover_url: string | null;
  difficulty: string;
  is_public: boolean;
  creator_id: string | null;
  created_at: string;
  course_count: number;
  statement_count: number;
  last_active: string | null;
  last_course_id: string | null;
}

export interface Course {
  id: string;
  course_pack_id?: string;
  title: string;
  description: string | null;
  order: number;
  difficulty: string;
  created_at: string;
  statements: Statement[];
  progress?: UserProgress;
}

export interface Statement {
  id: string;
  order: number;
  chinese: string;
  english: string;
  soundmark?: string | null;
  grammar?: unknown;
  tts_audio_url?: string | null;
  course_id?: string;
}

// ---- 学习进度 ----
export interface UserProgress {
  course_id: string;
  statement_index: number;
  completed: boolean;
  xp_awarded: number;
  completed_at: string | null;
}

// ---- 游戏 ----
export type GameMode = "chinese_to_english" | "dictation";
export type Difficulty = "beginner" | "intermediate" | "advanced";
export type GamePhase = "question" | "fix" | "answer";
export type GameStatus = "idle" | "playing" | "paused" | "completed";

export interface WordSlot {
  id: number;
  target: string;
  userInput: string;
  status: "pending" | "active" | "correct" | "incorrect";
  start: number;
  end: number;
}

export interface GameResult {
  statement_id: string;
  quality: number;
  interval: number;
  ease_factor: number;
  repetitions: number;
}

export interface CourseCompleteResponse {
  completed: boolean;
  xp_awarded: number;
  next_course_id: string | null;
  next_course_title: string | null;
}

// ---- 会话 ----
export interface LearningSession {
  course_pack_id: string;
  course_id: string;
  mode: GameMode;
  difficulty: Difficulty;
  start_time: string;
  end_time?: string;
  statements_completed: number;
  xp_earned: number;
}

// ---- TTS ----
export interface TTSRequest {
  text: string;
  voice?: string;
}

export interface BatchTTSRequest {
  statement_ids: string[];
  voice?: string;
}

export interface BatchTTSResponse {
  audios: { statement_id: string; url: string }[];
}

// ---- 统计 ----
export interface StatsSummary {
  xp: number;
  level: number;
  streak: number;
  longest_streak: number;
  total_statements: number;
  total_duration: number;
  xp_to_next_level: number;
}

export interface LearningRecord {
  course_pack_title: string;
  course_title: string;
  statements_completed: number;
  date: string;
  duration_minutes: number;
}

// ---- 设置 ----
export interface UserSettings {
  game_mode: GameMode;
  difficulty: Difficulty;
  pronunciation: "american" | "british";
  auto_pronunciation: boolean;
  keyboard_sound: boolean;
  space_submit: boolean;
}

// ---- 快捷键 ----
export interface ShortcutMap {
  showAnswer: string;
  playSound: string;
  markMastered: string;
  pause: string;
}

export const DEFAULT_SHORTCUTS: ShortcutMap = {
  showAnswer: "ctrl+h",
  playSound: "ctrl+j",
  markMastered: "ctrl+m",
  pause: "escape",
};
