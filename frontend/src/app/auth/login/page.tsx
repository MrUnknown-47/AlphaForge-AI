"use client";

import React, { useState } from "react";
import { useRouter } from "next/navigation";
import { useAuthStore } from "../../../store/authStore";
import { authService } from "../../../services/auth";
import { Button } from "../../../components/ui/Button";

export default function LoginPage() {
  const router = useRouter();
  const { login } = useAuthStore();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!email.includes("@")) {
      setError("Valid email required");
      return;
    }
    if (password.length < 8) {
      setError("Password must be at least 8 characters");
      return;
    }
    try {
      const res = await authService.login(email, password);
      login(res.access_token, res.refresh_token, "TRADER", {
        username: "quant_trader",
        email: email
      });
      router.push("/");
    } catch (err) {
      setError("Invalid credentials or authentication failure");
    }
  };

  return (
    <div className="flex h-screen bg-terminal text-white overflow-hidden">
      {/* Left panel */}
      <div className="w-1/2 bg-secondaryBg flex flex-col justify-between p-12 border-r border-borderCustom">
        <div>
          <span className="text-xl font-bold tracking-wider text-accentCustom">ALPHAFORGE AI</span>
        </div>
        <div className="max-w-md">
          <h2 className="text-2xl font-bold mb-4 uppercase tracking-wider">Institutional Trading Portal</h2>
          <p className="text-xs text-mutedCustom leading-relaxed">
            Verify real-time machine learning prediction models, track portfolios, and audit risk parameters.
          </p>
        </div>
        <div className="text-[10px] text-mutedCustom flex justify-between uppercase">
          <span>Broker Status: Alpaca Paper Online</span>
          <span>Market: Active</span>
        </div>
      </div>

      {/* Right panel */}
      <div className="w-1/2 flex items-center justify-center p-12 bg-terminal">
        <form onSubmit={handleLogin} className="w-full max-w-sm space-y-6">
          <div>
            <h3 className="text-lg font-bold uppercase tracking-wider mb-2">Secure Login</h3>
            <p className="text-xs text-mutedCustom">Provide credentials to retrieve JWT session token.</p>
          </div>

          {error && (
            <div className="p-3 bg-dangerCustom bg-opacity-20 border border-dangerCustom rounded text-xs text-dangerCustom">
              {error}
            </div>
          )}

          <div className="space-y-4 text-xs font-semibold">
            <div>
              <label className="block text-mutedCustom mb-2">EMAIL ADDRESS</label>
              <input
                type="text"
                className="w-full bg-secondaryBg border border-borderCustom rounded px-3 py-2 text-white focus:outline-none focus:border-accentCustom"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
            <div>
              <div className="flex justify-between mb-2">
                <label className="text-mutedCustom">PASSWORD</label>
                <button
                  type="button"
                  onClick={() => router.push("/auth/forgot-password")}
                  className="text-accentCustom hover:underline"
                >
                  Forgot password?
                </button>
              </div>
              <input
                type="password"
                className="w-full bg-secondaryBg border border-borderCustom rounded px-3 py-2 text-white focus:outline-none focus:border-accentCustom"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
          </div>

          <div className="flex items-center justify-between text-xs">
            <label className="flex items-center gap-2 text-mutedCustom">
              <input type="checkbox" className="rounded bg-secondaryBg border-borderCustom" />
              Remember this device
            </label>
          </div>

          <Button type="submit" variant="primary" className="w-full">
            LOGIN
          </Button>

          <p className="text-center text-xs text-mutedCustom">
            Don't have an account?{" "}
            <button
              type="button"
              onClick={() => router.push("/auth/register")}
              className="text-accentCustom hover:underline"
            >
              Register here
            </button>
          </p>
        </form>
      </div>
    </div>
  );
}
