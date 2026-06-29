"use client";

import React, { useState } from "react";
import { useTradingStore } from "../../store/tradingStore";
import {
  ResponsiveContainer,
  AreaChart,
  Area,
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";

interface TradingChartProps {
  ticker: string;
}

const mockPriceData = [
  { name: "09:30", price: 180.00, vwap: 180.20 },
  { name: "10:00", price: 181.50, vwap: 181.10 },
  { name: "10:30", price: 182.10, vwap: 181.80 },
  { name: "11:00", price: 181.20, vwap: 181.70 },
  { name: "11:30", price: 182.50, vwap: 182.10 },
  { name: "12:00", price: 183.10, vwap: 182.60 },
  { name: "12:30", price: 182.80, vwap: 182.70 },
  { name: "13:00", price: 183.60, vwap: 183.10 }
];

export const TradingChart: React.FC<TradingChartProps> = ({ ticker }) => {
  const [activeTab, setActiveTab] = useState<"PRICE" | "PNL">("PRICE");
  const { pnl } = useTradingStore();

  return (
    <div className="space-y-4">
      {/* Tab Selectors */}
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <div className="flex gap-2">
          <button
            onClick={() => setActiveTab("PRICE")}
            className={`px-3 py-1 text-xs font-bold uppercase tracking-wider rounded transition-colors ${
              activeTab === "PRICE"
                ? "bg-accentCustom bg-opacity-25 text-accentCustom border border-accentCustom"
                : "text-mutedCustom hover:text-white"
            }`}
          >
            {ticker} Price Chart
          </button>
          <button
            onClick={() => setActiveTab("PNL")}
            className={`px-3 py-1 text-xs font-bold uppercase tracking-wider rounded transition-colors ${
              activeTab === "PNL"
                ? "bg-accentCustom bg-opacity-25 text-accentCustom border border-accentCustom"
                : "text-mutedCustom hover:text-white"
            }`}
          >
            Realtime PnL & Equity Curve
          </button>
        </div>
      </div>

      {activeTab === "PRICE" ? (
        <div className="space-y-4">
          <div className="h-64 w-full bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={mockPriceData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
                <XAxis dataKey="name" stroke="#94A3B8" fontSize={10} />
                <YAxis stroke="#94A3B8" fontSize={10} domain={["auto", "auto"]} />
                <Tooltip
                  contentStyle={{
                    backgroundColor: "#111827",
                    borderColor: "#1F2937",
                    borderRadius: "4px",
                    fontSize: "10px",
                    color: "#FFFFFF"
                  }}
                />
                <Line
                  type="monotone"
                  dataKey="price"
                  name={`${ticker} Price`}
                  stroke="#00D4FF"
                  strokeWidth={2}
                  dot={false}
                />
                <Line
                  type="monotone"
                  dataKey="vwap"
                  name="VWAP"
                  stroke="#F59E0B"
                  strokeWidth={1}
                  strokeDasharray="3 3"
                  dot={false}
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
      ) : (
        /* SECTION 4: REALTIME PNL PANEL */
        <div className="space-y-4">
          {/* PnL Stats Header */}
          <div className="grid grid-cols-4 gap-4 bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 text-xs font-semibold">
            <div>
              <span className="text-mutedCustom block uppercase tracking-wider text-[10px]">Daily PnL</span>
              <span className={`text-base font-bold font-mono ${pnl.daily_pnl >= 0 ? "text-successCustom" : "text-dangerCustom"}`}>
                ${pnl.daily_pnl.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
              </span>
            </div>
            <div>
              <span className="text-mutedCustom block uppercase tracking-wider text-[10px]">Realized PnL</span>
              <span className="text-base font-bold text-white font-mono">
                ${pnl.realized_pnl.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
              </span>
            </div>
            <div>
              <span className="text-mutedCustom block uppercase tracking-wider text-[10px]">Unrealized PnL</span>
              <span className={`text-base font-bold font-mono ${pnl.unrealized_pnl >= 0 ? "text-successCustom" : "text-dangerCustom"}`}>
                ${pnl.unrealized_pnl.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
              </span>
            </div>
            <div>
              <span className="text-mutedCustom block uppercase tracking-wider text-[10px]">Portfolio Equity</span>
              <span className="text-base font-bold text-accentCustom font-mono">
                ${pnl.portfolio_equity.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
              </span>
            </div>
          </div>

          {/* Intraday Equity Curve Area Chart */}
          <div className="h-64 w-full bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={pnl.equity_curve}>
                <defs>
                  <linearGradient id="colorEquity" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#10B981" stopOpacity={0.4}/>
                    <stop offset="95%" stopColor="#10B981" stopOpacity={0}/>
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
                <XAxis dataKey="time" stroke="#94A3B8" fontSize={10} />
                <YAxis stroke="#94A3B8" fontSize={10} domain={["auto", "auto"]} />
                <Tooltip
                  contentStyle={{
                    backgroundColor: "#111827",
                    borderColor: "#1F2937",
                    borderRadius: "4px",
                    fontSize: "10px",
                    color: "#FFFFFF"
                  }}
                />
                <Area
                  type="monotone"
                  dataKey="value"
                  name="Equity ($)"
                  stroke="#10B981"
                  fillOpacity={1}
                  fill="url(#colorEquity)"
                  strokeWidth={2}
                />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>
      )}
    </div>
  );
};

export default TradingChart;
