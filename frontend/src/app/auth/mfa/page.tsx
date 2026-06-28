"use client";

import React, { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { authService } from "../../../services/auth";
import { Button } from "../../../components/ui/Button";

export default function MfaPage() {
  const router = useRouter();
  const [code, setCode] = useState("");
  const [timer, setTimer] = useState(60);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState(false);

  useEffect(() => {
    if (timer <= 0) return;
    const interval = setInterval(() => setTimer((t) => t - 1), 1000);
    return () => clearInterval(interval);
  }, [timer]);

  const handleVerify = async (e: React.FormEvent) => {
    e.preventDefault();
    if (code.length < 6) {
      setError("Valid 6-digit MFA OTP code required");
      return;
    }
    try {
      await authService.verifyMfa(code);
      setSuccess(true);
      setError("");
      setTimeout(() => router.push("/"), 1000);
    } catch (err) {
      setError("Incorrect or expired OTP verification code");
    }
  };

  return (
    <div className="flex h-screen bg-terminal text-white overflow-hidden items-center justify-center">
      <div className="w-full max-w-sm bg-cardBg border border-borderCustom p-8 rounded-lg shadow-2xl space-y-6">
        <div>
          <h3 className="text-lg font-bold uppercase tracking-wider mb-2">MFA Authentication</h3>
          <p className="text-xs text-mutedCustom">Provide the 6-digit OTP verification code from Google Authenticator.</p>
        </div>

        {success ? (
          <div className="p-3 bg-successCustom bg-opacity-20 border border-successCustom rounded text-xs text-successCustom">
            Verification successful. Redirecting to workspace...
          </div>
        ) : (
          <form onSubmit={handleVerify} className="space-y-6">
            {error && (
              <div className="p-3 bg-dangerCustom bg-opacity-20 border border-dangerCustom rounded text-xs text-dangerCustom">
                {error}
              </div>
            )}
            <div className="text-xs font-semibold">
              <label className="block text-mutedCustom mb-2">OTP SECURITY CODE</label>
              <input
                type="text"
                maxLength={6}
                placeholder="000000"
                className="w-full bg-secondaryBg border border-borderCustom rounded px-3 py-2 text-center text-lg tracking-widest text-white focus:outline-none focus:border-accentCustom"
                value={code}
                onChange={(e) => setCode(e.target.value)}
              />
            </div>
            
            <div className="flex justify-between items-center text-[10px] uppercase font-semibold text-mutedCustom">
              {timer > 0 ? (
                <span>Resend OTP code in {timer}s</span>
              ) : (
                <button
                  type="button"
                  onClick={() => setTimer(60)}
                  className="text-accentCustom hover:underline"
                >
                  Resend code
                </button>
              )}
            </div>

            <Button type="submit" variant="primary" className="w-full">
              VERIFY AND SIGN IN
            </Button>
          </form>
        )}
      </div>
    </div>
  );
}
