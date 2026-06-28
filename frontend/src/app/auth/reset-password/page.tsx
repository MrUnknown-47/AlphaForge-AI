"use client";

import React, { useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { authService } from "../../../services/auth";
import { Button } from "../../../components/ui/Button";

export default function ResetPasswordPage() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const token = searchParams.get("token") || "mock-token";

  const [password, setPassword] = useState("");
  const [success, setSuccess] = useState(false);
  const [error, setError] = useState("");

  const handleReset = async (e: React.FormEvent) => {
    e.preventDefault();
    if (password.length < 8) {
      setError("Password must be at least 8 characters");
      return;
    }
    try {
      await authService.confirmReset(token, password);
      setSuccess(true);
      setError("");
    } catch (err) {
      setError("Error resetting password. Token may have expired.");
    }
  };

  return (
    <div className="flex h-screen bg-terminal text-white overflow-hidden items-center justify-center">
      <div className="w-full max-w-sm bg-cardBg border border-borderCustom p-8 rounded-lg shadow-2xl space-y-6">
        <div>
          <h3 className="text-lg font-bold uppercase tracking-wider mb-2">New Password</h3>
          <p className="text-xs text-mutedCustom">Provide a new password for your account.</p>
        </div>

        {success ? (
          <div className="space-y-4">
            <div className="p-3 bg-successCustom bg-opacity-20 border border-successCustom rounded text-xs text-successCustom">
              Password updated successfully.
            </div>
            <Button variant="primary" className="w-full" onClick={() => router.push("/auth/login")}>
              RETURN TO LOGIN
            </Button>
          </div>
        ) : (
          <form onSubmit={handleReset} className="space-y-6">
            {error && (
              <div className="p-3 bg-dangerCustom bg-opacity-20 border border-dangerCustom rounded text-xs text-dangerCustom">
                {error}
              </div>
            )}
            <div className="text-xs font-semibold">
              <label className="block text-mutedCustom mb-2">NEW PASSWORD</label>
              <input
                type="password"
                className="w-full bg-secondaryBg border border-borderCustom rounded px-3 py-2 text-white focus:outline-none focus:border-accentCustom"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
            <Button type="submit" variant="primary" className="w-full">
              CONFIRM NEW PASSWORD
            </Button>
          </form>
        )}
      </div>
    </div>
  );
}
