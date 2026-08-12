// ============================================================
// LinguaPulse API 客户端
// ============================================================

import type {
  AuthResponse,
  LoginRequest,
  RegisterRequest,
  User,
  CoursePack,
  Course,
  CourseCompleteResponse,
  GameResult,
  StatsSummary,
  LearningRecord,
  UserSettings,
  BatchTTSResponse,
  LearningSession,
} from "./types";

const BASE_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

// ---- 通用请求方法 ----

function getToken(): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem("access_token");
}

async function request<T>(
  path: string,
  options: RequestInit = {}
): Promise<T> {
  const token = getToken();
  const headers: Record<string, string> = {
    "Content-Type": "application/json",
    ...(options.headers as Record<string, string>),
  };
  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }

  const res = await fetch(`${BASE_URL}${path}`, {
    ...options,
    headers,
  });

  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: res.statusText }));
    throw new Error(error.detail || `HTTP ${res.status}`);
  }

  return res.json();
}

// ---- Auth ----

export async function sendCode(email: string): Promise<{ message: string }> {
  return request<{ message: string }>("/api/auth/send-code", {
    method: "POST",
    body: JSON.stringify({ email }),
  });
}

export async function register(data: RegisterRequest): Promise<AuthResponse> {
  const res = await request<AuthResponse>("/api/auth/register", {
    method: "POST",
    body: JSON.stringify(data),
  });
  if (typeof window !== "undefined") {
    localStorage.setItem("access_token", res.access_token);
  }
  return res;
}

export async function login(data: LoginRequest): Promise<AuthResponse> {
  const res = await request<AuthResponse>("/api/auth/login", {
    method: "POST",
    body: JSON.stringify(data),
  });
  if (typeof window !== "undefined") {
    localStorage.setItem("access_token", res.access_token);
  }
  return res;
}

export function logout(): void {
  if (typeof window !== "undefined") {
    localStorage.removeItem("access_token");
  }
}

export async function getMe(): Promise<User> {
  return request<User>("/api/auth/me");
}

// ---- 课程 ----

export async function getCoursePacks(): Promise<CoursePack[]> {
  return request<CoursePack[]>("/api/course-packs");
}

export async function getMyCoursePacks(): Promise<CoursePack[]> {
  // MVP: "我的课程包" = 所有公开课程包（没有 enroll 概念）
  return getCoursePacks();
}

export async function getMarketCoursePacks(): Promise<CoursePack[]> {
  return getCoursePacks();
}

export async function getCoursePack(
  packId: string
): Promise<CoursePack & { courses: Course[] }> {
  return request(`/api/course-packs/${packId}`);
}

export async function getCourse(
  packId: string,
  courseId: string
): Promise<Course> {
  return request(`/api/course-packs/${packId}/courses/${courseId}`);
}

// ---- 进度 & 游戏 ----

export async function saveProgress(
  courseId: string,
  statementIndex: number
): Promise<{ statement_index: number }> {
  return request(`/api/progress/${courseId}`, {
    method: "PUT",
    body: JSON.stringify({ statement_index: statementIndex }),
  });
}

/** 提交答题结果到后端（检查正确性、发放 XP） */
export interface AnswerCheckResponse {
  correct: boolean;
  incorrect_words: number[];
  normalized_input: string;
  quality: number;
  xp_earned: number;
}

export async function checkAnswer(data: {
  statement_id: string;
  user_input: string;
  difficulty: string;
  fix_count: number;
}): Promise<AnswerCheckResponse> {
  return request<AnswerCheckResponse>("/api/game/check", {
    method: "POST",
    body: JSON.stringify(data),
  });
}

/** 提交 SM-2 复习评分（答题通过后调用） */
export interface ReviewSubmitResponse {
  id: string;
  statement_id: string;
  ease_factor: number;
  interval: number;
  repetitions: number;
  next_review_at: string;
  last_review_at: string | null;
  last_quality: number | null;
  total_reviews: number;
  total_errors: number;
}

export async function submitReview(data: {
  statement_id: string;
  quality: number;
}): Promise<ReviewSubmitResponse> {
  return request<ReviewSubmitResponse>("/api/review/submit", {
    method: "POST",
    body: JSON.stringify(data),
  });
}

export async function completeCourse(
  courseId: string,
  results: GameResult[],
  xpEarned: number = 0
): Promise<CourseCompleteResponse> {
  return request<CourseCompleteResponse>(
    `/api/progress/${courseId}/complete`,
    {
      method: "POST",
      body: JSON.stringify({ results, xp_earned: xpEarned }),
    }
  );
}

// ---- 会话 ----

export async function startSession(
  session: LearningSession
): Promise<LearningSession> {
  return request("/api/sessions", {
    method: "POST",
    body: JSON.stringify(session),
  });
}

export async function endSession(
  sessionId: string,
  data: { end_time: string; statements_completed: number; xp_earned: number }
): Promise<void> {
  return request(`/api/sessions/${sessionId}`, {
    method: "PATCH",
    body: JSON.stringify(data),
  });
}

// ---- TTS ----

export function getTtsUrl(text: string, voice = "en-US-JennyNeural", speed = "+15%"): string {
  return `${BASE_URL}/api/tts/synthesize?text=${encodeURIComponent(text)}&voice=${encodeURIComponent(voice)}&speed=${encodeURIComponent(speed)}`;
}

/**
 * 预加载 TTS 音频到浏览器 HTTP 缓存（fire-and-forget）。
 *
 * 服务端返回 MP3 时带 Cache-Control: max-age=3600，
 * 浏览器会缓存请求结果。后续 Audio 元素请求同一 URL
 * 直接从浏览器缓存秒开，无需再次请求服务器。
 *
 * 滑动窗口策略：
 *   - 首次进入课程时预加载前 5 个单词
 *   - 每进入新单词时预加载当前 + 后 4 个
 *   - 不占服务端磁盘，不占前端内存（浏览器管控）
 */
export function preloadTts(text: string, voice?: string, speed?: string): void {
  const url = getTtsUrl(text, voice, speed);
  // 直接用 fetch 触发下载 → 浏览器 HTTP 缓存持久化
  fetch(url).catch(() => {});
}

// ---- 统计 ----

export async function getStatsSummary(): Promise<StatsSummary> {
  return request<StatsSummary>("/api/stats/summary");
}

export async function reportSession(data: {
  duration: number;
  statements_count: number;
  course_id: string | null;
}): Promise<void> {
  return request("/api/stats/session", {
    method: "POST",
    body: JSON.stringify(data),
  });
}

export async function getRecentRecords(): Promise<LearningRecord[]> {
  return request<LearningRecord[]>("/api/dashboard/recent");
}

// ---- 更多例句 ----

export interface MoreExamplesResponse {
  examples: Array<{
    id: string;
    order: number;
    chinese: string;
    english: string;
    soundmark?: string | null;
    grammar?: unknown;
    tts_audio_url?: string | null;
    course_id?: string;
  }>;
}

export async function getMoreExamples(
  packId: string,
  courseId: string,
  statementId: string
): Promise<MoreExamplesResponse> {
  return request<MoreExamplesResponse>(
    `/api/course-packs/${packId}/courses/${courseId}/more-examples/${statementId}`
  );
}

// ---- 设置 ----

export async function getSettings(): Promise<UserSettings> {
  return request<UserSettings>("/api/settings");
}

export async function updateSettings(
  settings: Partial<UserSettings>
): Promise<UserSettings> {
  return request<UserSettings>("/api/settings", {
    method: "PATCH",
    body: JSON.stringify(settings),
  });
}
