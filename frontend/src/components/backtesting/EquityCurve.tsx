"use client";

import React from "react";
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

const rawData = [
  { name: "Month 1", Strategy: 1000000, Benchmark: 1000000 },
  { name: "Month 2", Strategy: 1050000, Benchmark: 1010000 },
  { name: "Month 3", Strategy: 1082000, Benchmark: 1018000 },
  { name: "Month 4", Strategy: 1140000, Benchmark: 1032000 },
  { name: "Month 5", Strategy: 1185423, Benchmark: 1045000 }
];

export const EquityCurve = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Backtest Equity Curve vs SPY Benchmark</h4>

      <div className="h-64 w-full bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
        <ResponsiveContainer width="100%" height="100%">
          <ComposedChart data={rawData}>
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
          </ComposedChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};
export default EquityCurve;
