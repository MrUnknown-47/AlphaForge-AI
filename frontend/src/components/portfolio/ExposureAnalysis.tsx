"use client";

import React, { useState } from "react";
import {
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  CartesianGrid
} from "recharts";

const allocationData = [
  { name: "AAPL", value: 24.5, color: "#00D4FF" },
  { name: "NVDA", value: 41.2, color: "#10B981" },
  { name: "MSFT", value: 18.5, color: "#F59E0B" },
  { name: "TSLA", value: 15.8, color: "#EF4444" }
];

const sectorData = [
  { name: "Technology", Long: 84.2, Short: 0, Net: 84.2 },
  { name: "Automotive", Long: 15.8, Short: 0, Net: 15.8 },
  { name: "Consumer", Long: 12.0, Short: -5.5, Net: 6.5 },
  { name: "Financials", Long: 5.0, Short: -8.0, Net: -3.0 }
];

const factorData = [
  { name: "Beta", Portfolio: 0.88, Benchmark: 1.00 },
  { name: "Momentum", Portfolio: 1.45, Benchmark: 0.80 },
  { name: "Value", Portfolio: 0.65, Benchmark: 0.95 },
  { name: "Size", Portfolio: 1.10, Benchmark: 0.75 },
  { name: "Quality", Portfolio: 1.35, Benchmark: 1.05 }
];

export const ExposureAnalysis: React.FC = () => {
  const [activeTab, setActiveTab] = useState<"ALLOCATION" | "SECTOR" | "FACTOR">("ALLOCATION");

  return (
    <div className="space-y-4">
      {/* Header Selector */}
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <div className="flex gap-2">
          {["ALLOCATION", "SECTOR", "FACTOR"].map((tab) => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab as any)}
              className={`px-2 py-1 text-[10px] font-bold rounded uppercase tracking-wider transition-colors ${
                activeTab === tab
                  ? "bg-accentCustom bg-opacity-25 text-accentCustom border border-accentCustom"
                  : "text-mutedCustom hover:text-white"
              }`}
            >
              {tab}
            </button>
          ))}
        </div>
      </div>

      <div className="h-64 w-full bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
        <ResponsiveContainer width="100%" height="100%">
          {activeTab === "ALLOCATION" ? (
            <PieChart>
              <Pie
                data={allocationData}
                cx="50%"
                cy="50%"
                innerRadius={60}
                outerRadius={80}
                paddingAngle={5}
                dataKey="value"
              >
                {allocationData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.color} />
                ))}
              </Pie>
              <Tooltip
                contentStyle={{
                  backgroundColor: "#111827",
                  borderColor: "#1F2937",
                  borderRadius: "4px",
                  fontSize: "10px",
                  color: "#FFFFFF"
                }}
              />
              <Legend verticalAlign="bottom" height={36} wrapperStyle={{ fontSize: "10px" }} />
            </PieChart>
          ) : activeTab === "SECTOR" ? (
            <BarChart data={sectorData}>
              <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
              <XAxis dataKey="name" stroke="#94A3B8" fontSize={9} />
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
              <Legend verticalAlign="top" height={36} wrapperStyle={{ fontSize: "10px" }} />
              <Bar dataKey="Long" fill="#10B981" name="Long %" />
              <Bar dataKey="Short" fill="#EF4444" name="Short %" />
              <Bar dataKey="Net" fill="#00D4FF" name="Net %" />
            </BarChart>
          ) : (
            <BarChart data={factorData}>
              <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
              <XAxis dataKey="name" stroke="#94A3B8" fontSize={9} />
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
              <Legend verticalAlign="top" height={36} wrapperStyle={{ fontSize: "10px" }} />
              <Bar dataKey="Portfolio" fill="#00D4FF" name="Portfolio Loading" />
              <Bar dataKey="Benchmark" fill="#1F2937" name="Benchmark Loading" />
            </BarChart>
          )}
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default ExposureAnalysis;
