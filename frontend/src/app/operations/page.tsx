"use client";

import React, { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { ProtectedRoute } from "../../components/auth/ProtectedRoute";
import { Badge } from "../../components/ui/Badge";
import { SearchBar } from "../../components/ui/SearchBar";
import { CommandPalette } from "../../components/ui/CommandPalette";
import { LoadingScreen } from "../../components/ui/LoadingScreen";
import { useAuthStore } from "../../store/authStore";
import { useOperationsStore } from "../../store/operationsStore";

// Widgets import
import CommandCenter from "../../components/operations/CommandCenter";
import InfrastructureMonitor from "../../components/operations/InfrastructureMonitor";
import TradingOperations from "../../components/operations/TradingOperations";
import MLOps from "../../components/operations/MLOps";
import SecurityOperations from "../../components/operations/SecurityOperations";
import IncidentCenter from "../../components/operations/IncidentCenter";
import AuditCenter from "../../components/operations/AuditCenter";
import ValidationCenter from "../../components/operations/ValidationCenter";
import CapitalProtection from "../../components/operations/CapitalProtection";
import OperationsTimeline from "../../components/operations/OperationsTimeline";
import InstitutionalScorecard from "../../components/operations/InstitutionalScorecard";
import ExecutiveControlTower from "../../components/operations/ExecutiveControlTower";

export default function OperationsPage() {
  const router = useRouter();
  const [loading, setLoading] = useState(true);
  const [cmdOpen, setCmdOpen] = useState(false);
  const [menuDropdownOpen, setMenuDropdownOpen] = useState(false);

  const { user, role, logout } = useAuthStore();
  const { brokerLatencyMs } = useOperationsStore();

  useEffect(() => {
    const timer = setTimeout(() => setLoading(false), 1000);
    return () => clearTimeout(timer);
  }, []);

  if (loading) {
    return <LoadingScreen message="Establishing secure operations telemetry websocket connections..." />;
  }

  const commands = [
    { category: "Navigation", label: "Go to Main Workspace", action: () => router.push("/") },
    { category: "Navigation", label: "Go to Portfolio Analytics", action: () => router.push("/portfolio") },
    { category: "Navigation", label: "Go to AI Agents Hub", action: () => router.push("/agents") }
  ];

  const handleLogout = () => {
    logout();
    router.push("/auth/login");
  };

  return (
    <ProtectedRoute>
      <div className="flex h-screen bg-terminal text-white overflow-hidden font-sans">
        <CommandPalette isOpen={cmdOpen} onClose={() => setCmdOpen(false)} options={commands} />

        {/* Sidebar Nav */}
        <aside className="w-64 bg-secondaryBg border-r border-borderCustom flex flex-col justify-between">
          <div>
            <div className="h-16 flex items-center px-6 border-b border-borderCustom">
              <span className="text-xl font-bold tracking-wider text-accentCustom cursor-pointer" onClick={() => router.push("/")}>
                ALPHAFORGE AI
              </span>
            </div>
            <nav className="mt-4 px-3 space-y-1">
              {[
                { name: "Operations Tower", icon: "🏢", path: "/operations" },
                { name: "Executive Terminal", icon: "📊", path: "/dashboard" },
                { name: "Live Trading", icon: "⚡", path: "/live-trading" },
                { name: "AI Agents", icon: "🤖", path: "/agents" }
              ].map((item) => (
                <button
                  key={item.name}
                  onClick={() => router.push(item.path)}
                  className={`w-full flex items-center px-4 py-2.5 rounded text-xs font-semibold uppercase tracking-wider transition-colors ${
                    item.path === "/operations"
                      ? "bg-accentCustom bg-opacity-25 text-accentCustom"
                      : "text-mutedCustom hover:text-white hover:bg-cardBg"
                  }`}
                >
                  <span className="mr-3 text-sm">{item.icon}</span>
                  {item.name}
                </button>
              ))}
            </nav>
          </div>
          <div className="p-4 border-t border-borderCustom text-[10px] text-mutedCustom flex justify-between uppercase">
            <span>Version 1.0.0-F12</span>
            <span className="text-successCustom">● Staging</span>
          </div>
        </aside>

        {/* Main Workspace */}
        <div className="flex-1 flex flex-col overflow-hidden">
          {/* Top Navbar */}
          <header className="h-16 bg-secondaryBg border-b border-borderCustom flex items-center justify-between px-6">
            <div className="flex items-center gap-4">
              <SearchBar placeholder="Press Ctrl+K or search NOC..." onClick={() => setCmdOpen(true)} readOnly />
            </div>
            <div className="flex items-center gap-4 text-xs font-semibold">
              <Badge variant="success">Broker: Alpaca Paper Online</Badge>
              <Badge variant="info">Market: Active</Badge>
              <div className="flex items-center gap-2">
                <span className="text-mutedCustom">Latency:</span>
                <span className="text-accentCustom">{brokerLatencyMs}ms</span>
              </div>

              {/* User Dropdown */}
              <div className="relative">
                <button
                  onClick={() => setMenuDropdownOpen(!menuDropdownOpen)}
                  className="flex items-center gap-2 focus:outline-none"
                >
                  <div className="w-8 h-8 rounded-full bg-accentCustom text-terminal flex items-center justify-center font-bold">
                    {user?.username ? user.username[0].toUpperCase() : "QS"}
                  </div>
                  <Badge variant="info">{role || "TRADER"}</Badge>
                </button>

                {menuDropdownOpen && (
                  <div className="absolute right-0 mt-2 w-48 bg-cardBg border border-borderCustom rounded shadow-2xl py-2 z-50 text-xs">
                    <button
                      onClick={() => {
                        setMenuDropdownOpen(false);
                        router.push("/profile");
                      }}
                      className="w-full text-left px-4 py-2 hover:bg-secondaryBg hover:bg-opacity-50 text-white"
                    >
                      User Profile
                    </button>
                    <button
                      onClick={() => {
                        setMenuDropdownOpen(false);
                        router.push("/security");
                      }}
                      className="w-full text-left px-4 py-2 hover:bg-secondaryBg hover:bg-opacity-50 text-white"
                    >
                      Security Center
                    </button>
                    <div className="border-t border-borderCustom my-1" />
                    <button
                      onClick={handleLogout}
                      className="w-full text-left px-4 py-2 hover:bg-secondaryBg hover:bg-opacity-50 text-dangerCustom font-bold"
                    >
                      Logout Session
                    </button>
                  </div>
                )}
              </div>
            </div>
          </header>

          {/* Scrollable workspace */}
          <main className="flex-1 overflow-y-auto p-6 space-y-6">
            <div>
              <h2 className="text-2xl font-bold uppercase tracking-wider text-white">Institutional Operations Center & Enterprise Control Tower</h2>
              <p className="text-xs text-mutedCustom mt-1">Real-time SRE/NOC and SOC system diagnostics.</p>
            </div>

            <div className="grid grid-cols-1 xl:grid-cols-12 gap-6">
              {/* Left Column (8 columns) */}
              <div className="xl:col-span-8 space-y-6">
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <CommandCenter />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <TradingOperations />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <IncidentCenter />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <AuditCenter />
                </div>
              </div>

              {/* Right Column (4 columns) */}
              <div className="xl:col-span-4 space-y-6">
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <InfrastructureMonitor />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <MLOps />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <SecurityOperations />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <ValidationCenter />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <CapitalProtection />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <OperationsTimeline />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <InstitutionalScorecard />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <ExecutiveControlTower />
                </div>
              </div>
            </div>
          </main>
        </div>
      </div>
    </ProtectedRoute>
  );
}
