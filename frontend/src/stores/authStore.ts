// ============================================================
// Auth Store - 认证状态管理
// ============================================================

import { create } from "zustand";
import type { User } from "@/lib/types";
import { getMe, logout as apiLogout } from "@/lib/api";

interface AuthState {
  user: User | null;
  token: string | null;
  isLoading: boolean;
  isAuthenticated: boolean;

  setAuth: (user: User, token: string) => void;
  clearAuth: () => void;
  checkAuth: () => Promise<void>;
  logout: () => void;
}

export const useAuthStore = create<AuthState>((set, get) => ({
  user: null,
  token: null,
  isLoading: true,
  isAuthenticated: false,

  setAuth: (user, token) => {
    if (typeof window !== "undefined") {
      localStorage.setItem("access_token", token);
    }
    set({ user, token, isAuthenticated: true, isLoading: false });
  },

  clearAuth: () => {
    if (typeof window !== "undefined") {
      localStorage.removeItem("access_token");
    }
    set({ user: null, token: null, isAuthenticated: false, isLoading: false });
  },

  checkAuth: async () => {
    const token =
      typeof window !== "undefined"
        ? localStorage.getItem("access_token")
        : null;
    if (!token) {
      set({ isLoading: false });
      return;
    }
    try {
      const user = await getMe();
      set({
        user,
        token,
        isAuthenticated: true,
        isLoading: false,
      });
    } catch {
      // token 过期或无效
      if (typeof window !== "undefined") {
        localStorage.removeItem("access_token");
      }
      set({ isLoading: false });
    }
  },

  logout: () => {
    apiLogout();
    get().clearAuth();
  },
}));
