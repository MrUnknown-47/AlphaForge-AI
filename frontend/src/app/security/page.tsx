"use client";

import React, { useState } from "react";
import { Card } from "../../components/ui/Card";
import { Button } from "../../components/ui/Button";
import { Badge } from "../../components/ui/Badge";
import { ProtectedRoute } from "../../components/auth/ProtectedRoute";
import { useRouter } from "next/navigation";

export default function SecurityPage() {
  const router = useRouter();
  const [mfaEnabled, setMfaEnabled] = useState(true);

  // Active user sessions listing
  const activeSessions = [
    { ip: "127.0.0.1", device: "Desktop Core (macOS)", location: "Staging sandbox", last_active: "Active now" },
    { ip: "192.168.1.15", device: "AlphaTerminal (Chrome)", location: "Office Network", last_active: "2 hours ago" }
  ];

  const permissions = [
    { role: "TRADER", live_trade: "ALLOWED", audit_logs: "READ ONLY", risk_edit: "DENIED" },
    { role: "COMPLIANCE", live_trade: "READ ONLY", audit_logs: "FULL ACCESS", risk_edit: "ALLOWED" },
    { role: "RISK_MANAGER", live_trade: "DENIED", audit_logs: "READ ONLY", risk_edit: "FULL ACCESS" }
  ];

  const surveillanceAlerts = [
    { id: "surv_101", type: "Spoofing Alert", asset: "AAPL", desc: "Rapid limit order insertions and cancellations detected.", severity: "CRITICAL", timestamp: "5 mins ago" },
    { id: "surv_102", type: "Wash Trading Alert", asset: "NVDA", desc: "Self-crossing buy/sell executions matching same account.", severity: "CRITICAL", timestamp: "12 mins ago" }
  ];

  const complianceChecks = [
    { check: "SEC Rule 15c3-3 (Customer Protection)", status: "PASSED" },
    { check: "FINRA Order Audit Trail System (OATS)", status: "PASSED" },
    { check: "MiFID II Transaction Reporting", status: "PASSED" }
  ];

  const retentionPolicies = [
    { type: "Trade Execution logs", retention: "7 Years" },
    { type: "Audit trails logs", retention: "7 Years" },
    { type: "AI explainability records", retention: "5 Years" }
  ];

  const explainabilityRecords = [
    { id: "exp_901", decision: "Consensus BUY on AAPL", model: "SHAP/LIME Attribution", date: "June 27" },
    { id: "exp_902", decision: "Risk HEDGE put purchase", model: "Covariance stress test", date: "June 25" }
  ];

  return (
    <ProtectedRoute>
      <div className="min-h-screen bg-terminal text-white p-8 space-y-6 font-sans">
        <div className="flex justify-between items-center border-b border-borderCustom pb-4">
          <div>
            <h2 className="text-2xl font-bold uppercase tracking-wider">Institutional Security & Compliance Center</h2>
            <p className="text-xs text-mutedCustom mt-1">NOC/SOC Compliance policy, surveillance monitoring, and audit checks.</p>
          </div>
          <Button variant="secondary" size="sm" onClick={() => router.push("/")}>Back to Terminal</Button>
        </div>

        <div className="grid grid-cols-1 xl:grid-cols-12 gap-6">
          {/* Left Column (8 cols): Compliance, Policy, Surveillance, Auditing */}
          <div className="xl:col-span-8 space-y-6">
            
            {/* Audit Chain & Compliance Checks */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <Card title="Compliance Health Checks">
                <div className="space-y-3 text-xs font-semibold text-mutedCustom">
                  {complianceChecks.map((cc) => (
                    <div key={cc.check} className="flex justify-between border-b border-borderCustom pb-2 last:border-0 last:pb-0">
                      <span>{cc.check}</span>
                      <Badge variant="success">{cc.status}</Badge>
                    </div>
                  ))}
                </div>
              </Card>

              <Card title="Audit Retention Policies">
                <div className="space-y-3 text-xs font-semibold text-mutedCustom">
                  {retentionPolicies.map((rp) => (
                    <div key={rp.type} className="flex justify-between border-b border-borderCustom pb-2 last:border-0 last:pb-0">
                      <span>{rp.type}</span>
                      <span className="text-white font-mono">{rp.retention}</span>
                    </div>
                  ))}
                </div>
              </Card>
            </div>

            {/* Surveillance Alerts (Spoofing & Wash Trading) */}
            <Card title="Surveillance Alerts (Abusive Trading Detection)">
              <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
                <table className="w-full text-left text-xs border-collapse">
                  <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
                    <tr>
                      <th className="px-3 py-2.5">Alert ID</th>
                      <th className="px-3 py-2.5">Type</th>
                      <th className="px-3 py-2.5">Symbol</th>
                      <th className="px-3 py-2.5">Description</th>
                      <th className="px-3 py-2.5">Severity</th>
                      <th className="px-3 py-2.5 text-right">Age</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-borderCustom font-medium">
                    {surveillanceAlerts.map((sa) => (
                      <tr key={sa.id} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                        <td className="px-3 py-2.5 text-white font-mono">{sa.id}</td>
                        <td className="px-3 py-2.5 text-white font-semibold">{sa.type}</td>
                        <td className="px-3 py-2.5 text-accentCustom">{sa.asset}</td>
                        <td className="px-3 py-2.5 text-mutedCustom">{sa.desc}</td>
                        <td className="px-3 py-2.5">
                          <Badge variant="danger">{sa.severity}</Badge>
                        </td>
                        <td className="px-3 py-2.5 text-right text-mutedCustom font-mono">{sa.timestamp}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </Card>

            {/* Explainability Records */}
            <Card title="Explainability Records Logs">
              <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
                <table className="w-full text-left text-xs border-collapse">
                  <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
                    <tr>
                      <th className="px-3 py-2.5">Record ID</th>
                      <th className="px-3 py-2.5">Attributed Decision</th>
                      <th className="px-3 py-2.5">Explainability Model</th>
                      <th className="px-3 py-2.5 text-right">Date</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-borderCustom font-medium">
                    {explainabilityRecords.map((er) => (
                      <tr key={er.id} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                        <td className="px-3 py-2.5 text-white font-mono">{er.id}</td>
                        <td className="px-3 py-2.5 text-white font-semibold">{er.decision}</td>
                        <td className="px-3 py-2.5 text-accentCustom font-mono">{er.model}</td>
                        <td className="px-3 py-2.5 text-right text-mutedCustom font-mono">{er.date}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </Card>
          </div>

          {/* Right Column (4 cols): Security status, Permission Matrix */}
          <div className="xl:col-span-4 space-y-6">
            
            {/* MFA Status Card */}
            <Card title="Multi-Factor Auth (MFA)">
              <div className="space-y-4 text-xs">
                <p className="text-mutedCustom">Protects execution gateway routers from unauthorized order placement.</p>
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

            {/* Permission Matrix */}
            <Card title="Role Permission Matrix">
              <div className="space-y-3 text-xs font-semibold text-mutedCustom">
                {permissions.map((p) => (
                  <div key={p.role} className="border-b border-borderCustom pb-3 last:border-0 last:pb-0">
                    <span className="block text-white font-bold mb-1">{p.role}</span>
                    <div className="grid grid-cols-3 gap-2 text-[10px] uppercase">
                      <div>
                        <span className="block text-mutedCustom">Trade</span>
                        <span className="block text-accentCustom font-bold mt-0.5">{p.live_trade}</span>
                      </div>
                      <div>
                        <span className="block text-mutedCustom">Audit</span>
                        <span className="block text-accentCustom font-bold mt-0.5">{p.audit_logs}</span>
                      </div>
                      <div>
                        <span className="block text-mutedCustom">Risk</span>
                        <span className="block text-accentCustom font-bold mt-0.5">{p.risk_edit}</span>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </Card>

            {/* Sessions Management */}
            <Card title="Active Session management">
              <div className="overflow-hidden rounded border border-borderCustom bg-secondaryBg bg-opacity-25 divide-y divide-borderCustom text-xs">
                {activeSessions.map((session, idx) => (
                  <div key={idx} className="flex justify-between p-4 items-center">
                    <div>
                      <span className="block font-bold text-white uppercase">{session.device}</span>
                      <span className="block text-[10px] text-mutedCustom mt-1">IP: {session.ip}</span>
                    </div>
                    <div className="flex items-center gap-3">
                      <span className="text-mutedCustom">{session.last_active}</span>
                      <Button variant="ghost" size="sm" className="text-dangerCustom">Term</Button>
                    </div>
                  </div>
                ))}
              </div>
            </Card>
          </div>
        </div>
      </div>
    </ProtectedRoute>
  );
}
