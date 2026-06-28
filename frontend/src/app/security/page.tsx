"use client";

import React, { useState } from "react";
import { Card } from "../../components/ui/Card";
import { Button } from "../../components/ui/Button";
import { Badge } from "../../components/ui/Badge";
import { ProtectedRoute } from "../../components/auth/ProtectedRoute";

export default function SecurityPage() {
  const [mfaEnabled, setMfaEnabled] = useState(true);

  // Active user sessions listing
  const activeSessions = [
    { ip: "127.0.0.1", device: "Desktop Core (macOS)", location: "Staging sandbox", last_active: "Active now" },
    { ip: "192.168.1.15", device: "AlphaTerminal (Chrome)", location: "Office Network", last_active: "2 hours ago" }
  ];

  return (
    <ProtectedRoute>
      <div className="min-h-screen bg-terminal text-white p-8">
        <div className="max-w-3xl mx-auto space-y-6">
          <h2 className="text-2xl font-bold uppercase tracking-wider">Security Command Center</h2>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <Card title="Multi-Factor Auth (MFA)">
              <div className="space-y-4 text-xs">
                <p className="text-mutedCustom">Two-factor validation protects executions from unauthorized API routing.</p>
                <div className="flex items-center justify-between">
                  <span className="font-semibold">MFA Status:</span>
                  <Badge variant={mfaEnabled ? "success" : "danger"}>
                    {mfaEnabled ? "ENABLED" : "DISABLED"}
                  </Badge>
                </div>
                <Button variant="secondary" size="sm" onClick={() => setMfaEnabled(!mfaEnabled)}>
                  {mfaEnabled ? "DISABLE MFA" : "ENABLE MFA"}
                </Button>
              </div>
            </Card>

            <Card title="JWT Token Configurations">
              <div className="space-y-3 text-xs font-semibold text-mutedCustom">
                <div className="flex justify-between border-b border-borderCustom pb-2">
                  <span>Access Token Expiry:</span>
                  <span className="text-white">15 minutes</span>
                </div>
                <div className="flex justify-between border-b border-borderCustom pb-2">
                  <span>Refresh Session Expiry:</span>
                  <span className="text-white">7 days</span>
                </div>
                <div className="flex justify-between">
                  <span>Session inactivity timeout:</span>
                  <span className="text-white">15 minutes</span>
                </div>
              </div>
            </Card>
          </div>

          <Card title="Active Authenticated Sessions" subtitle="Remote devices currently signed into this profile.">
            <div className="overflow-hidden rounded border border-borderCustom bg-secondaryBg bg-opacity-25 divide-y divide-borderCustom text-xs">
              {activeSessions.map((session, idx) => (
                <div key={idx} className="flex justify-between p-4 items-center">
                  <div>
                    <span className="block font-bold text-white uppercase">{session.device}</span>
                    <span className="block text-[10px] text-mutedCustom mt-1">IP: {session.ip} | Location: {session.location}</span>
                  </div>
                  <div className="flex items-center gap-3">
                    <span className="text-mutedCustom">{session.last_active}</span>
                    <Button variant="ghost" size="sm" className="text-dangerCustom">Term</Button>
                  </div>
                </div>
              ))}
            </div>
            <div className="mt-4 flex justify-end">
              <Button variant="danger" size="sm">LOGOUT ALL OTHER DEVICES</Button>
            </div>
          </Card>
        </div>
      </div>
    </ProtectedRoute>
  );
}
