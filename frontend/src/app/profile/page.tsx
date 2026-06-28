"use client";

import React from "react";
import { useAuthStore } from "../../store/authStore";
import { Card } from "../../components/ui/Card";
import { Badge } from "../../components/ui/Badge";
import { ProtectedRoute } from "../../components/auth/ProtectedRoute";

export default function ProfilePage() {
  const { user, role } = useAuthStore();

  return (
    <ProtectedRoute>
      <div className="min-h-screen bg-terminal text-white p-8">
        <div className="max-w-xl mx-auto space-y-6">
          <h2 className="text-2xl font-bold uppercase tracking-wider">User Account Profile</h2>
          
          <Card title="Identification Metrics">
            <div className="space-y-4 text-xs font-semibold text-mutedCustom">
              <div className="flex items-center gap-4 border-b border-borderCustom pb-4">
                <div className="w-16 h-16 rounded-full bg-accentCustom text-terminal flex items-center justify-center font-bold text-2xl">
                  {user?.username ? user.username[0].toUpperCase() : "U"}
                </div>
                <div>
                  <h3 className="text-sm font-bold text-white uppercase">{user?.username || "quant_user"}</h3>
                  <p className="text-[10px] mt-1">Institutional member since June 2026</p>
                </div>
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div>
                  <span className="block text-[10px] uppercase text-mutedCustom mb-1">EMAIL ADDRESS</span>
                  <span className="text-white">{user?.email || "trader@alphaforge.ai"}</span>
                </div>
                <div>
                  <span className="block text-[10px] uppercase text-mutedCustom mb-1">ROLE ASSIGNMENT</span>
                  <Badge variant="info">{role || "TRADER"}</Badge>
                </div>
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div>
                  <span className="block text-[10px] uppercase text-mutedCustom mb-1">BROKER CHANNEL</span>
                  <span className="text-white font-mono">ALPACA PAPER GATEWAY</span>
                </div>
                <div>
                  <span className="block text-[10px] uppercase text-mutedCustom mb-1">API ACCESS SCHEMAS</span>
                  <span className="text-successCustom">● READ / WRITE / EXECUTE</span>
                </div>
              </div>
            </div>
          </Card>
        </div>
      </div>
    </ProtectedRoute>
  );
}
