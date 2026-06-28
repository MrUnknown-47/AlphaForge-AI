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
import PortfolioSummary from "../../components/portfolio/PortfolioSummary";
import EquityAnalytics from "../../components/portfolio/EquityAnalytics";
import HoldingsAnalysis from "../../components/portfolio/HoldingsAnalysis";
import ExposureAnalysis from "../../components/portfolio/ExposureAnalysis";
import RiskAnalytics from "../../components/portfolio/RiskAnalytics";
import DrawdownAnalysis from "../../components/portfolio/DrawdownAnalysis";
import PerformanceAttribution from "../../components/portfolio/PerformanceAttribution";
import CorrelationMatrix from "../../components/portfolio/CorrelationMatrix";
import MonteCarloPanel from "../../components/portfolio/MonteCarloPanel";
import OptimizerPanel from "../../components/portfolio/OptimizerPanel";
import AIPortfolioManager from "../../components/portfolio/AIPortfolioManager";
import PortfolioActivity from "../../components/portfolio/PortfolioActivity";

export default function PortfolioPage() {
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
    return <LoadingScreen message="Aggregating BlackRock Aladdin parameters..." />;
  }

  const commands = [
    { category: "Navigation", label: "Go to Main Workspace", action: () => router.push("/") },
    { category: "Navigation", label: "Go to Executive Dashboard", action: () => router.push("/dashboard") },
    { category: "Security", label: "Open Security options", action: () => router.push("/security") }
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
                { name: "Portfolio Hub", icon: "💼", path: "/portfolio" },
                { name: "Executive Terminal", icon: "📊", path: "/dashboard" },
                { name: "Live Trading", icon: "⚡", path: "/live-trading" },
                { name: "Security Center", icon: "🛡️", path: "/security" }
              ].map((item) => (
                <button
                  key={item.name}
                  onClick={() => router.push(item.path)}
                  className={`w-full flex items-center px-4 py-2.5 rounded text-xs font-semibold uppercase tracking-wider transition-colors ${
                    item.path === "/portfolio"
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
            <span>Version 1.0.0-F5</span>
            <span className="text-successCustom">● Staging</span>
          </div>
        </aside>

        {/* Main Workspace */}
        <div className="flex-1 flex flex-col overflow-hidden">
          {/* Top Navbar */}
          <header className="h-16 bg-secondaryBg border-b border-borderCustom flex items-center justify-between px-6">
            <div className="flex items-center gap-4">
              <SearchBar placeholder="Press Ctrl+K or search portfolio..." onClick={() => setCmdOpen(true)} readOnly />
            </div>
            <div className="flex items-center gap-4 text-xs font-semibold">
              <Badge variant="success">Broker: Alpaca Paper Online</Badge>
              <Badge variant="info">Market: Active</Badge>
              <div className="flex items-center gap-2">
                <span className="text-mutedCustom">Latency:</span>
                <span className="text-accentCustom">{brokerLatencyMs}ms</span>
              </div>

              {/* User dropdown */}
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
              <h2 className="text-2xl font-bold uppercase tracking-wider text-white">Portfolio Risk & Analytics Workspace</h2>
              <p className="text-xs text-mutedCustom mt-1">Cross-sectional factor and volatility covariance metrics.</p>
            </div>

            <PortfolioSummary />

            <div className="grid grid-cols-1 xl:grid-cols-12 gap-6">
              {/* Left Side (8 columns) */}
              <div className="xl:col-span-8 space-y-6">
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <EquityAnalytics />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <HoldingsAnalysis />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <PerformanceAttribution />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <MonteCarloPanel />
                </div>
              </div>

              {/* Right Side (4 columns) */}
              <div className="xl:col-span-4 space-y-6">
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <ExposureAnalysis />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <RiskAnalytics />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <DrawdownAnalysis />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <CorrelationMatrix />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <OptimizerPanel />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <AIPortfolioManager />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <PortfolioActivity />
                </div>
              </div>
            </div>
          </main>
        </div>
      </div>
    </ProtectedRoute>
  );
}
