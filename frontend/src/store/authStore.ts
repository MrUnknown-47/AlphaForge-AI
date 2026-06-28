import { create } from "zustand";

interface User {
  username: string;
  email: string;
}

interface AuthState {
  user: User | null;
  role: string | null;
  accessToken: string | null;
  refreshToken: string | null;
  isAuthenticated: boolean;
  login: (accessToken: string, refreshToken: string, role: string, user: User) => void;
  logout: () => void;
  refresh: (accessToken: string, refreshToken: string) => void;
  updateUser: (user: Partial<User>) => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  role: null,
  accessToken: null,
  refreshToken: null,
  isAuthenticated: false,
  login: (accessToken, refreshToken, role, user) => set({ accessToken, refreshToken, role, user, isAuthenticated: true }),
  logout: () => set({ accessToken: null, refreshToken: null, role: null, user: null, isAuthenticated: false }),
  refresh: (accessToken, refreshToken) => set({ accessToken, refreshToken }),
  updateUser: (updatedUser) => set((state) => ({
    user: state.user ? { ...state.user, ...updatedUser } : null
  })),
}));
