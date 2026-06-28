"use client";

import React, { useState } from "react";
import { useRouter } from "next/navigation";
import { authService } from "../../../services/auth";
import { Button } from "../../../components/ui/Button";

export default function RegisterPage() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleRegister = async (e: React.FormEvent) => {
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
      await authService.register(email, username, password);
      router.push("/auth/login");
    } catch (err) {
      setError("User creation or validation failed");
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
          <h2 className="text-2xl font-bold mb-4 uppercase tracking-wider">Account Creation</h2>
          <p className="text-xs text-mutedCustom leading-relaxed">
            Register your email address to enable access to backtests and validation sandboxes.
          </p>
        </div>
        <div className="text-[10px] text-mutedCustom flex justify-between uppercase">
          <span>Security Policy: Active</span>
          <span>Access: RBAC Gated</span>
        </div>
      </div>

      {/* Right panel */}
      <div className="w-1/2 flex items-center justify-center p-12 bg-terminal">
        <form onSubmit={handleRegister} className="w-full max-w-sm space-y-6">
          <div>
            <h3 className="text-lg font-bold uppercase tracking-wider mb-2">Create Account</h3>
            <p className="text-xs text-mutedCustom">Provide credentials to register a new user.</p>
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
              <label className="block text-mutedCustom mb-2">USERNAME</label>
              <input
                type="text"
                className="w-full bg-secondaryBg border border-borderCustom rounded px-3 py-2 text-white focus:outline-none focus:border-accentCustom"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
            </div>
            <div>
              <label className="block text-mutedCustom mb-2">PASSWORD (MIN 8 CHARS)</label>
              <input
                type="password"
                className="w-full bg-secondaryBg border border-borderCustom rounded px-3 py-2 text-white focus:outline-none focus:border-accentCustom"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
          </div>

          <Button type="submit" variant="primary" className="w-full">
            REGISTER
          </Button>

          <p className="text-center text-xs text-mutedCustom">
            Already have an account?{" "}
            <button
              type="button"
              onClick={() => router.push("/auth/login")}
              className="text-accentCustom hover:underline"
            >
              Login here
            </button>
          </p>
        </form>
      </div>
    </div>
  );
}
