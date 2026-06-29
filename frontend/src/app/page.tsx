"use client";

import React, { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { Button } from "../components/ui/Button";
import { Card } from "../components/ui/Card";
import { MetricCard } from "../components/ui/MetricCard";
import { DataGrid } from "../components/ui/DataGrid";
import { Badge } from "../components/ui/Badge";
import { Alert } from "../components/ui/Alert";
import { SearchBar } from "../components/ui/SearchBar";
import { CommandPalette } from "../components/ui/CommandPalette";
import { LoadingScreen } from "../components/ui/LoadingScreen";
import { usePortfolioStore } from "../store/portfolioStore";
import { useOperationsStore } from "../store/operationsStore";
import { useTradingStore } from "../store/tradingStore";
import { useAuthStore } from "../store/authStore";
import { ProtectedRoute } from "../components/auth/ProtectedRoute";

export default function Home() {
  const router = useRouter();
  const [loading, setLoading] = useState(true);
  const [activeMenu, setActiveMenu] = useState("Dashboard");
  const [cmdOpen, setCmdOpen] = useState(false);
  const [confirmOpen, setConfirmOpen] = useState(false);
  const [confirmMessage, setConfirmMessage] = useState("");
  const [menuDropdownOpen, setMenuDropdownOpen] = useState(false);

  const { portfolioValue, cash, exposurePct, dailyReturn, positions } = usePortfolioStore();
  const { uptimePct, brokerLatencyMs, activeAlerts } = useOperationsStore();
  const { orders, addOrder } = useTradingStore();
  const { user, role, logout } = useAuthStore();

  useEffect(() => {
    const timer = setTimeout(() => setLoading(false), 1000);
    return () => clearTimeout(timer);
  }, []);

  if (loading) {
    return <LoadingScreen message="Initializing AlphaForge Terminal UI..." />;
  }

  const menuItems = [
    { name: "Dashboard", icon: "📊" },
    { name: "Live Trading", icon: "⚡" },
    { name: "Portfolio", icon: "💼" },
    { name: "AI Copilot", icon: "🤖" },
    { name: "Backtesting", icon: "🧪" },
    { name: "Validation", icon: "🔬" },
    { name: "Operations", icon: "⚙️" },
    { name: "Security", icon: "🛡️" },
  ];

  const commands = [
    { category: "Trading", label: "Place Buy Order - AAPL", action: () => {
        setConfirmMessage("Confirm BUY order of 10 shares of AAPL?");
        setConfirmOpen(true);
      }
    },
    { category: "Navigation", label: "Go to Live Trading Screen", action: () => setActiveMenu("Live Trading") },
    { category: "Operations", label: "Check API Health Stats", action: () => setActiveMenu("Operations") },
    { category: "Security", label: "Verify masked secrets keys", action: () => setActiveMenu("Security") }
  ];

  const handleConfirmedOrder = () => {
    addOrder({
      id: `ord_${Math.floor(Math.random() * 10000)}`,
      ticker: "AAPL",
      side: "BUY",
      quantity: 10,
      price: 182.50,
      type: "MARKET",
      status: "FILLED",
      timestamp: new Date().toISOString()
    });
    setConfirmOpen(false);
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
              {menuItems.map((item) => (
                <button
                  key={item.name}
                  onClick={() => {
                    if (item.name === "Dashboard") {
                      setActiveMenu("Dashboard");
                    } else if (item.name === "Live Trading") {
                      router.push("/live-trading");
                    } else if (item.name === "Portfolio") {
                      router.push("/portfolio");
                    } else if (item.name === "AI Copilot") {
                      router.push("/copilot");
                    } else if (item.name === "Backtesting") {
                      router.push("/backtesting");
                    } else if (item.name === "Validation") {
                      router.push("/operations");
                    } else if (item.name === "Operations") {
                      router.push("/operations");
                    } else if (item.name === "Security") {
                      router.push("/security");
                    }
                  }}
                  className={`w-full flex items-center px-4 py-2.5 rounded text-xs font-semibold uppercase tracking-wider transition-colors ${
                    activeMenu === item.name
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
            <span>Version 1.0.0-F2</span>
            <span className="text-successCustom">● Staging</span>
          </div>
        </aside>

        {/* Main Workspace */}
        <div className="flex-1 flex flex-col overflow-hidden">
          {/* Top bar navbar */}
          <header className="h-16 bg-secondaryBg border-b border-borderCustom flex items-center justify-between px-6">
            <div className="flex items-center gap-4">
              <SearchBar placeholder="Press Ctrl+K or search here..." onClick={() => setCmdOpen(true)} readOnly />
            </div>
            <div className="flex items-center gap-4 text-xs font-semibold">
              <Badge variant="success">Broker: Alpaca Paper Online</Badge>
              <Badge variant="info">Market: Active</Badge>
              <div className="flex items-center gap-2">
                <span className="text-mutedCustom">Latency:</span>
                <span className="text-accentCustom">{brokerLatencyMs}ms</span>
              </div>
              
              {/* User profile actions dropdown */}
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

          {/* Content body container */}
          <main className="flex-1 overflow-y-auto p-6 bg-terminal">
            <h2 className="text-2xl font-bold text-white mb-6 uppercase tracking-wider">{activeMenu} Workspace</h2>

            {activeMenu === "Dashboard" && (
              <div className="space-y-6">
                {/* Metrics row */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                  <MetricCard label="Portfolio Equity" value={`$${portfolioValue.toLocaleString()}`} delta={0.24} />
                  <MetricCard label="Available Cash" value={`$${cash.toLocaleString()}`} />
                  <MetricCard label="Portfolio Exposure" value={`${(exposurePct * 100).toFixed(1)}%`} />
                  <MetricCard label="Daily Return" value={`${dailyReturn.toFixed(2)}%`} delta={dailyReturn} />
                </div>

                {/* Warnings display */}
                {activeAlerts.length > 0 && (
                  <Alert variant="warning" title="Active Operations Warnings" description={activeAlerts.join(", ")} />
                )}

                {/* Positions and orders grid */}
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                  <Card title="Active Holdings" subtitle="Open portfolio assets reconciled against broker.">
                    <DataGrid
                      items={positions}
                      columns={[
                        { key: "ticker", header: "Ticker" },
                        { key: "quantity", header: "Quantity" },
                        { key: "entry_price", header: "Entry Price", render: (val) => `$${val.toFixed(2)}` },
                        { key: "market_value", header: "Market Value", render: (val) => `$${val.toLocaleString()}` },
                        { key: "unrealized_pnl", header: "Unrealized PnL", render: (val) => (
                            <span className={val >= 0 ? "text-successCustom" : "text-dangerCustom"}>
                              ${val.toFixed(2)}
                            </span>
                          )
                        }
                      ]}
                    />
                  </Card>

                  <Card title="Recent Orders" subtitle="Limit and market executions routed to broker.">
                    <DataGrid
                      items={orders}
                      columns={[
                        { key: "id", header: "Order ID" },
                        { key: "ticker", header: "Ticker" },
                        { key: "side", header: "Side", render: (val) => (
                            <span className={val === "BUY" ? "text-successCustom" : "text-dangerCustom"}>{val}</span>
                          )
                        },
                        { key: "quantity", header: "Qty" },
                        { key: "price", header: "Price", render: (val) => val ? `$${val.toFixed(2)}` : "MARKET" },
                        { key: "status", header: "Status", render: (val) => <Badge variant={val === "FILLED" ? "success" : "warning"}>{val}</Badge> }
                      ]}
                    />
                  </Card>
                </div>
              </div>
            )}

            {activeMenu !== "Dashboard" && (
              <Card title={`${activeMenu} telemetry and logs`} subtitle="Real-time dashboard mapping live REST API models inputs.">
                <div className="py-12 text-center text-mutedCustom font-medium border border-dashed border-borderCustom rounded">
                  Connected to AlphaForge gateway. Load module components to view stats.
                </div>
              </Card>
            )}
          </main>
        </div>

        {/* Confirmation Modal */}
        {confirmOpen && (
          <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-75 p-4">
            <div className="w-full max-w-sm rounded bg-cardBg border border-borderCustom p-6 shadow-2xl">
              <h4 className="text-sm font-bold text-white mb-4 uppercase tracking-wider">Confirm Action</h4>
              <p className="text-xs text-mutedCustom mb-6">{confirmMessage}</p>
              <div className="flex justify-end gap-3">
                <Button variant="secondary" size="sm" onClick={() => setConfirmOpen(false)}>Cancel</Button>
                <Button variant="primary" size="sm" onClick={handleConfirmedOrder}>Confirm</Button>
              </div>
            </div>
          </div>
        )}
      </div>
    </ProtectedRoute>
  );
}