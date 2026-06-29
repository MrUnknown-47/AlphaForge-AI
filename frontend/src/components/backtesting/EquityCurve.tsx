"use client";

import React, { useState } from "react";
import {
  ResponsiveContainer,
  LineChart,
  Line,
  AreaChart,
  Area,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Legend
} from "recharts";

const rawData = [
  { name: "Month 1", Strategy: 1000000, Benchmark: 1000000, drawdown: 0 },
  { name: "Month 2", Strategy: 1050000, Benchmark: 1010000, drawdown: 0 },
  { name: "Month 3", Strategy: 1025000, Benchmark: 1005000, drawdown: -2.38 },
  { name: "Month 4", Strategy: 1140000, Benchmark: 1032000, drawdown: 0 },
  { name: "Month 5", Strategy: 1185423, Benchmark: 1045000, drawdown: 0 }
];

const histogramData = [
  { bin: "-2% to -1%", frequency: 5 },
  { bin: "-1% to 0%", frequency: 18 },
  { bin: "0% to 1%", frequency: 32 },
  { bin: "1% to 2%", frequency: 24 },
  { bin: "2% to 3%", frequency: 12 },
  { bin: "3%+", frequency: 4 }
];

export const EquityCurve: React.FC = () => {
  const [activeTab, setActiveTab] = useState<"EQUITY" | "DRAWDOWN" | "HISTOGRAM">("EQUITY");

  return (
    <div className="space-y-4">
      {/* Tab select Header */}
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <div className="flex gap-2">
          {["EQUITY", "DRAWDOWN", "HISTOGRAM"].map((tab) => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab as any)}
              className={`px-3 py-1 text-xs font-bold uppercase tracking-wider rounded transition-colors ${
                activeTab === tab
                  ? "bg-accentCustom bg-opacity-25 text-accentCustom border border-accentCustom"
                  : "text-mutedCustom hover:text-white"
              }`}
            >
              {tab} Curve / Plot
            </button>
          ))}
        </div>
      </div>

      <div className="h-64 w-full bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
        <ResponsiveContainer width="100%" height="100%">
          {activeTab === "EQUITY" ? (
            <LineChart data={rawData}>
              <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
              <XAxis dataKey="name" stroke="#94A3B8" fontSize={9} />
              <YAxis stroke="#94A3B8" fontSize={9} domain={["auto", "auto"]} />
              <Tooltip
                contentStyle={{
                  backgroundColor: "#111827",
                  borderColor: "#1F2937",
                  borderRadius: "4px",
                  fontSize: "10px",
                  color: "#FFFFFF"
                }}
              />
              <Legend verticalAlign="top" height={36} wrapperStyle={{ fontSize: "10px" }} />
              <Line
                type="monotone"
                dataKey="Strategy"
                name="AlphaForge Strategy"
                stroke="#00D4FF"
                strokeWidth={2}
                dot={false}
              />
              <Line
                type="monotone"
                dataKey="Benchmark"
                name="SPY Index"
                stroke="#94A3B8"
                strokeWidth={1.5}
                strokeDasharray="4 4"
                dot={false}
              />
            </LineChart>
          ) : activeTab === "DRAWDOWN" ? (
            <AreaChart data={rawData}>
              <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
              <XAxis dataKey="name" stroke="#94A3B8" fontSize={9} />
              <YAxis stroke="#94A3B8" fontSize={9} domain={[-5, 0]} />
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
                dataKey="drawdown"
                name="Drawdown Depth %"
                stroke="#EF4444"
                fill="#EF4444"
                fillOpacity={0.15}
              />
            </AreaChart>
          ) : (
            <BarChart data={histogramData}>
              <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
              <XAxis dataKey="bin" stroke="#94A3B8" fontSize={9} />
              <YAxis stroke="#94A3B8" fontSize={9} />
              <Tooltip
                contentStyle={{
                  backgroundColor: "#111827",
                  borderColor: "#1F2937",
                  borderRadius: "4px",
                  fontSize: "10px",
                  color: "#FFFFFF"
                }}
              />
              <Bar dataKey="frequency" fill="#10B981" name="Return Frequency" />
            </BarChart>
          )}
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default EquityCurve;
