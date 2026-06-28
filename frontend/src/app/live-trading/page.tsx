"use client";

import React, { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { ProtectedRoute } from "../../components/auth/ProtectedRoute";
import { Badge } from "../../components/ui/Badge";
import { SearchBar } from "../../components/ui/SearchBar";
import { CommandPalette } from "../../components/ui/CommandPalette";
import { LoadingScreen } from "../../components/ui/LoadingScreen";
import { useAuthStore } from "../../store/authStore";
import { usePortfolioStore } from "../../store/portfolioStore";
import { useOperationsStore } from "../../store/operationsStore";
import { useTradingStore } from "../../store/tradingStore";

// Widgets import
import MarketWatch from "../../components/live_trading/MarketWatch";
import TradingChart from "../../components/live_trading/TradingChart";
import SignalPanel from "../../components/live_trading/SignalPanel";
import OrderTicket from "../../components/live_trading/OrderTicket";
import PositionMonitor from "../../components/live_trading/PositionMonitor";
import RiskMonitor from "../../components/live_trading/RiskMonitor";
import ExecutionMonitor from "../../components/live_trading/ExecutionMonitor";
import BrokerPanel from "../../components/live_trading/BrokerPanel";
import TradeExplainer from "../../components/live_trading/TradeExplainer";
import AlertsPanel from "../../components/live_trading/AlertsPanel";

export default function LiveTradingPage() {
  const router = useRouter();
  const [loading, setLoading] = useState(true);
  const [cmdOpen, setCmdOpen] = useState(false);
  const [selectedTicker, setSelectedTicker] = useState("AAPL");
  const [menuDropdownOpen, setMenuDropdownOpen] = useState(false);
  const [alertMsg, setAlertMsg] = useState("");

  const { user, role, logout } = useAuthStore();
  const { brokerLatencyMs } = useOperationsStore();
  const { addOrder } = useTradingStore();

  useEffect(() => {
    const timer = setTimeout(() => setLoading(false), 1000);
    return () => clearTimeout(timer);
  }, []);

  // Keyboard shortcut listeners: B = Buy, S = Sell, ESC = Cancel
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "b" || e.key === "B") {
        setAlertMsg(`HOTKEY TRIGGERED: Initiated Buy execution ticket for ${selectedTicker}`);
      } else if (e.key === "s" || e.key === "S") {
        setAlertMsg(`HOTKEY TRIGGERED: Initiated Sell execution ticket for ${selectedTicker}`);
      } else if (e.key === "Escape") {
        setAlertMsg("");
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [selectedTicker]);

  if (loading) {
    return <LoadingScreen message="Initializing real-time execution pipelines..." />;
  }

  const commands = [
    { category: "Navigation", label: "Go to Main Dashboard", action: () => router.push("/dashboard") },
    { category: "Security", label: "Open Security configuration", action: () => router.push("/security") },
    { category: "Profile", label: "Open User settings", action: () => router.push("/profile") }
  ];

  const handleOrderPlace = (side: "BUY" | "SELL", qty: number, price: number) => {
    addOrder({
      id: `ord_${Math.floor(Math.random() * 10000)}`,
      ticker: selectedTicker,
      side: side,
      quantity: qty,
      price: price,
      type: "LIMIT",
      status: "FILLED",
      timestamp: new Date().toISOString()
    });
    setAlertMsg(`Success: Placed ${side} order for ${qty} shares of ${selectedTicker} @ $${price}`);
  };

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
                { name: "Live Trading", icon: "⚡", path: "/live-trading" },
                { name: "Executive Terminal", icon: "📊", path: "/dashboard" },
                { name: "Profile", icon: "👤", path: "/profile" },
                { name: "Security Center", icon: "🛡️", path: "/security" }
              ].map((item) => (
                <button
                  key={item.name}
                  onClick={() => router.push(item.path)}
                  className={`w-full flex items-center px-4 py-2.5 rounded text-xs font-semibold uppercase tracking-wider transition-colors ${
                    item.path === "/live-trading"
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
            <span>Version 1.0.0-F4</span>
            <span className="text-successCustom">● Staging</span>
          </div>
        </aside>

        {/* Main Workspace */}
        <div className="flex-1 flex flex-col overflow-hidden">
          {/* Top Navbar */}
          <header className="h-16 bg-secondaryBg border-b border-borderCustom flex items-center justify-between px-6">
            <div className="flex items-center gap-4">
              <SearchBar placeholder="Press Ctrl+K or search workspace..." onClick={() => setCmdOpen(true)} readOnly />
            </div>
            <div className="flex items-center gap-4 text-xs font-semibold">
              <Badge variant="success">Broker: Alpaca Paper Online</Badge>
              <Badge variant="info">Market: Active</Badge>
              <div className="flex items-center gap-2">
                <span className="text-mutedCustom">Latency:</span>
                <span className="text-accentCustom">{brokerLatencyMs}ms</span>
              </div>

              {/* User Menu */}
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

          {/* Main workspace panels */}
          <main className="flex-1 overflow-y-auto p-6 space-y-6">
            {alertMsg && (
              <div className="p-3 bg-accentCustom bg-opacity-25 border border-accentCustom text-accentCustom text-xs rounded font-semibold uppercase flex justify-between items-center">
                <span>{alertMsg}</span>
                <button onClick={() => setAlertMsg("")} className="font-bold">✕</button>
              </div>
            )}

            <div className="grid grid-cols-1 xl:grid-cols-12 gap-6">
              {/* Left Column (8 cols): Watching lists, charts, explainability */}
              <div className="xl:col-span-8 space-y-6">
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <MarketWatch onSelectTicker={setSelectedTicker} />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <TradingChart ticker={selectedTicker} />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <PositionMonitor onClosePosition={(tick) => setAlertMsg(`Closed position for ${tick}`)} />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <ExecutionMonitor />
                </div>
              </div>

              {/* Right Column (4 cols): Order execution controls, diagnostic panels */}
              <div className="xl:col-span-4 space-y-6">
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <OrderTicket ticker={selectedTicker} onPlaceOrder={handleOrderPlace} />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <SignalPanel ticker={selectedTicker} />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <TradeExplainer ticker={selectedTicker} />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <RiskMonitor />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <BrokerPanel />
                </div>
                <div className="bg-cardBg border border-borderCustom rounded p-5 shadow-lg">
                  <AlertsPanel />
                </div>
              </div>
            </div>
          </main>
        </div>
      </div>
    </ProtectedRoute>
  );
}
