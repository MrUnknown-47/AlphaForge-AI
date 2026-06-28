"use client";

import React, { useState } from "react";
import {
  ResponsiveContainer,
  ComposedChart,
  Line,
  Area,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  CartesianGrid
} from "recharts";

const rawData = [
  { name: "09:30", Portfolio: 1000000, SPY: 1000000, Drawdown: 0 },
  { name: "10:30", Portfolio: 1012000, SPY: 1005000, Drawdown: 0 },
  { name: "11:30", Portfolio: 1008000, SPY: 1002000, Drawdown: -0.39 },
  { name: "12:30", Portfolio: 1025000, SPY: 1010000, Drawdown: 0 },
  { name: "13:30", Portfolio: 1032000, SPY: 1008000, Drawdown: 0 },
  { name: "14:30", Portfolio: 1028000, SPY: 1012000, Drawdown: -0.38 },
  { name: "15:30", Portfolio: 1054231, SPY: 1015000, Drawdown: 0 }
];

export const EquityCurve = () => {
  const [range, setRange] = useState("1D");

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Equity & Drawdown Curve</h4>
        <div className="flex gap-1.5">
          {["1D", "1W", "1M", "ALL"].map((r) => (
            <button
              key={r}
              onClick={() => setRange(r)}
              className={`px-2 py-0.5 text-[10px] font-bold rounded uppercase tracking-wider border ${
                range === r
                  ? "bg-accentCustom text-terminal border-accentCustom"
                  : "bg-secondaryBg text-mutedCustom border-borderCustom hover:text-white"
              }`}
            >
              {r}
            </button>
          ))}
        </div>
      </div>

      <div className="h-64 w-full bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
        <ResponsiveContainer width="100%" height="100%">
          <ComposedChart data={rawData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
            <XAxis dataKey="name" stroke="#94A3B8" fontSize={10} />
            <YAxis yAxisId="left" stroke="#94A3B8" fontSize={10} domain={["auto", "auto"]} />
            <YAxis yAxisId="right" orientation="right" stroke="#EF4444" fontSize={10} domain={[-5, 0]} />
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
              yAxisId="left"
              type="monotone"
              dataKey="Portfolio"
              stroke="#00D4FF"
              strokeWidth={2}
              dot={false}
              activeDot={{ r: 4 }}
            />
            <Line
              yAxisId="left"
              type="monotone"
              dataKey="SPY"
              stroke="#94A3B8"
              strokeWidth={1}
              strokeDasharray="4 4"
              dot={false}
            />
            <Area
              yAxisId="right"
              type="monotone"
              dataKey="Drawdown"
              fill="#EF4444"
              stroke="none"
              fillOpacity={0.15}
            />
          </ComposedChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};
export default EquityCurve;
