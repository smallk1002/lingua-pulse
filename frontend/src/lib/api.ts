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

export async function completeCourse(
  courseId: string,
  results: GameResult[]
): Promise<CourseCompleteResponse> {
  return request<CourseCompleteResponse>(
    `/api/progress/${courseId}/complete`,
    {
      method: "POST",
      body: JSON.stringify({ results }),
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

export function getTtsUrl(text: string, voice = "en-US-JennyNeural"): string {
  return `${BASE_URL}/api/tts/synthesize?text=${encodeURIComponent(text)}&voice=${encodeURIComponent(voice)}`;
}

export async function batchTTS(
  statementIds: string[]
): Promise<BatchTTSResponse> {
  return request<BatchTTSResponse>("/api/tts/batch", {
    method: "POST",
    body: JSON.stringify({ statement_ids: statementIds }),
  });
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
