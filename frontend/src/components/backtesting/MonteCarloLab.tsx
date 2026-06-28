"use client";

import React from "react";
import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";

const simulations = [
  { name: "Step 0", Path1: 1000000, Path2: 1000000, Path3: 1000000 },
  { name: "Step 1", Path1: 1020000, Path2: 990000, Path3: 1010000 },
  { name: "Step 2", Path1: 1045000, Path2: 975000, Path3: 1030000 },
  { name: "Step 3", Path1: 1080000, Path2: 960000, Path3: 1045000 },
  { name: "Step 4", Path1: 1120000, Path2: 980000, Path3: 1060000 }
];

export const MonteCarloLab = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Monte Carlo Simulation Paths (1000 Iterations)</h4>

      <div className="h-48 w-full bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={simulations}>
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
            <Line type="monotone" dataKey="Path1" stroke="#10B981" strokeWidth={1} dot={false} name="Optimistic Path" />
            <Line type="monotone" dataKey="Path2" stroke="#EF4444" strokeWidth={1} dot={false} name="Pessimistic Path" />
            <Line type="monotone" dataKey="Path3" stroke="#00D4FF" strokeWidth={1.5} dot={false} name="Mean Path" />
          </LineChart>
        </ResponsiveContainer>
      </div>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-xs font-semibold text-mutedCustom bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 uppercase">
        <div>
          <span>Expected CAGR:</span>
          <span className="block text-white font-mono mt-1">+18.52%</span>
        </div>
        <div>
          <span>Expected Sharpe:</span>
          <span className="block text-white font-mono mt-1">1.82</span>
        </div>
        <div>
          <span>Probability of Ruin:</span>
          <span className="block text-successCustom font-mono mt-1">0.01%</span>
        </div>
        <div>
          <span>95% confidence interval:</span>
          <span className="block text-white font-mono mt-1">$940K - $1.4M</span>
        </div>
      </div>
    </div>
  );
};
export default MonteCarloLab;
