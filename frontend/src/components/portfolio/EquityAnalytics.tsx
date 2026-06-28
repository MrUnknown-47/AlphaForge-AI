"use client";

import React, { useState } from "react";
import {
  ResponsiveContainer,
  ComposedChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Legend
} from "recharts";

const data = [
  { name: "Jan", Portfolio: 1000000, SPY: 1000000, Alpha: 0 },
  { name: "Feb", Portfolio: 1020000, SPY: 1010000, Alpha: 1.0 },
  { name: "Mar", Portfolio: 1015000, SPY: 1005000, Alpha: 0.99 },
  { name: "Apr", Portfolio: 1038000, SPY: 1018000, Alpha: 1.96 },
  { name: "May", Portfolio: 1054231, SPY: 1025000, Alpha: 2.85 }
];

export const EquityAnalytics = () => {
  const [showBenchmark, setShowBenchmark] = useState(true);

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Equity Analytics & Alpha Generation</h4>
        <button
          onClick={() => setShowBenchmark(!showBenchmark)}
          className="px-2 py-0.5 text-[10px] uppercase font-bold rounded bg-secondaryBg text-mutedCustom border border-borderCustom hover:text-white"
        >
          {showBenchmark ? "Hide Benchmark" : "Show Benchmark"}
        </button>
      </div>

      <div className="h-64 w-full bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
        <ResponsiveContainer width="100%" height="100%">
          <ComposedChart data={data}>
            <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
            <XAxis dataKey="name" stroke="#94A3B8" fontSize={10} />
            <YAxis yAxisId="left" stroke="#94A3B8" fontSize={10} domain={["auto", "auto"]} />
            <YAxis yAxisId="right" orientation="right" stroke="#10B981" fontSize={10} domain={["auto", "auto"]} />
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
              name="Portfolio Value"
              stroke="#00D4FF"
              strokeWidth={2}
              dot={false}
            />
            {showBenchmark && (
              <Line
                yAxisId="left"
                type="monotone"
                dataKey="SPY"
                name="SPY Index"
                stroke="#94A3B8"
                strokeWidth={1.5}
                strokeDasharray="4 4"
                dot={false}
              />
            )}
            <Line
              yAxisId="right"
              type="monotone"
              dataKey="Alpha"
              name="Alpha Generation %"
              stroke="#10B981"
              strokeWidth={1.5}
              dot={false}
            />
          </ComposedChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};
export default EquityAnalytics;
