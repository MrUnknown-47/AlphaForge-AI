"use client";

import React from "react";
import {
  ResponsiveContainer,
  AreaChart,
  Area,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";

const drawdownHistory = [
  { name: "Week 1", drawdown: 0 },
  { name: "Week 2", drawdown: -1.25 },
  { name: "Week 3", drawdown: -3.12 },
  { name: "Week 4", drawdown: -0.50 },
  { name: "Week 5", drawdown: 0 }
];

export const DrawdownAnalysis = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Underwater Drawdown Curve</h4>

      <div className="h-48 w-full bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={drawdownHistory}>
            <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
            <XAxis dataKey="name" stroke="#94A3B8" fontSize={10} />
            <YAxis stroke="#94A3B8" fontSize={10} domain={[-5, 0]} />
            <Tooltip
              contentStyle={{
                backgroundColor: "#111827",
                borderColor: "#1F2937",
                borderRadius: "4px",
                fontSize: "10px",
                color: "#FFFFFF"
              }}
            />
            <Area type="monotone" dataKey="drawdown" name="Drawdown %" stroke="#EF4444" fill="#EF4444" fillOpacity={0.15} />
          </AreaChart>
        </ResponsiveContainer>
      </div>

      <div className="grid grid-cols-3 gap-2 text-xs font-semibold text-mutedCustom uppercase font-mono">
        <div>
          <span>Max Drawdown:</span>
          <span className="block text-dangerCustom font-bold mt-0.5">3.12%</span>
        </div>
        <div>
          <span>Ulcer Index:</span>
          <span className="block text-white font-bold mt-0.5">1.05</span>
        </div>
        <div>
          <span>Recovery Days:</span>
          <span className="block text-white font-bold mt-0.5">12 Days</span>
        </div>
      </div>
    </div>
  );
};
export default DrawdownAnalysis;
