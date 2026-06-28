"use client";

import React, { useEffect, useState } from "react";
import { useAuthStore } from "../store/authStore";
import { authService } from "../services/auth";
import { LoadingScreen } from "../components/ui/LoadingScreen";

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  const { login, logout, accessToken, refreshToken } = useAuthStore();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const initAuth = async () => {
      try {
        if (!accessToken && refreshToken) {
          // Attempt token refresh on session boot
          const data = await authService.refresh();
          if (data && data.access_token) {
            login(data.access_token, data.refresh_token, "TRADER", {
              username: "quant_trader",
              email: "trader@alphaforge.ai"
            });
          }
        }
      } catch (err) {
        logout();
      } finally {
        setLoading(false);
      }
    };
    initAuth();
  }, [accessToken, refreshToken, login, logout]);

  if (loading) {
    return <LoadingScreen message="Resolving user session token..." />;
  }

  return <>{children}</>;
};
export default AuthProvider;
