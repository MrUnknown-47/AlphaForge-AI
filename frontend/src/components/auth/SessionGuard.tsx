"use client";

import React, { useEffect } from "react";
import { useAuthStore } from "../../store/authStore";

export const SessionGuard = ({ children }: { children: React.ReactNode }) => {
  const { logout, isAuthenticated } = useAuthStore();

  useEffect(() => {
    if (!isAuthenticated) return;

    let timeoutId: NodeJS.Timeout;
    const resetTimer = () => {
      clearTimeout(timeoutId);
      // Auto logout after 15 minutes of inactivity (matching ACCESS_TOKEN_EXPIRY)
      timeoutId = setTimeout(() => {
        logout();
      }, 15 * 60 * 1000);
    };

    window.addEventListener("mousemove", resetTimer);
    window.addEventListener("keypress", resetTimer);
    resetTimer();

    return () => {
      window.removeEventListener("mousemove", resetTimer);
      window.removeEventListener("keypress", resetTimer);
      clearTimeout(timeoutId);
    };
  }, [isAuthenticated, logout]);

  return <>{children}</>;
};
export default SessionGuard;
