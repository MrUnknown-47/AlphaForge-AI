"use client";

import React, { useState } from "react";
import { useRouter } from "next/navigation";
import { authService } from "../../../services/auth";
import { Button } from "../../../components/ui/Button";

export default function ForgotPasswordPage() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [success, setSuccess] = useState(false);
  const [error, setError] = useState("");

  const handleRequest = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!email.includes("@")) {
      setError("Valid email required");
      return;
    }
    try {
      await authService.resetPassword(email);
      setSuccess(true);
      setError("");
    } catch (err) {
      setError("Error sending password reset request");
    }
  };

  return (
    <div className="flex h-screen bg-terminal text-white overflow-hidden items-center justify-center">
      <div className="w-full max-w-sm bg-cardBg border border-borderCustom p-8 rounded-lg shadow-2xl space-y-6">
        <div>
          <h3 className="text-lg font-bold uppercase tracking-wider mb-2">Reset Password</h3>
          <p className="text-xs text-mutedCustom">Request a password recovery token link.</p>
        </div>

        {success ? (
          <div className="space-y-4">
            <div className="p-3 bg-successCustom bg-opacity-20 border border-successCustom rounded text-xs text-successCustom">
              Password reset link sent to your email address.
            </div>
            <Button variant="secondary" className="w-full" onClick={() => router.push("/auth/login")}>
              RETURN TO LOGIN
            </Button>
          </div>
        ) : (
          <form onSubmit={handleRequest} className="space-y-6">
            {error && (
              <div className="p-3 bg-dangerCustom bg-opacity-20 border border-dangerCustom rounded text-xs text-dangerCustom">
                {error}
              </div>
            )}
            <div className="text-xs font-semibold">
              <label className="block text-mutedCustom mb-2">EMAIL ADDRESS</label>
              <input
                type="text"
                className="w-full bg-secondaryBg border border-borderCustom rounded px-3 py-2 text-white focus:outline-none focus:border-accentCustom"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
            <Button type="submit" variant="primary" className="w-full">
              SEND RESET LINK
            </Button>
          </form>
        )}
      </div>
    </div>
  );
}
