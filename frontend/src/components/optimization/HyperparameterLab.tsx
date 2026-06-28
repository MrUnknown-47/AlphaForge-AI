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

const convergenceData = [
  { trial: 1, value: 1.22, best: 1.22 },
  { trial: 5, value: 1.45, best: 1.45 },
  { trial: 10, value: 1.32, best: 1.45 },
  { trial: 15, value: 1.68, best: 1.68 },
  { trial: 20, value: 1.55, best: 1.68 },
  { trial: 25, value: 1.85, best: 1.85 }
];

export const HyperparameterLab = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Optuna Objective Value Convergence Curve</h4>

      <div className="h-48 w-full bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={convergenceData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
            <XAxis dataKey="trial" stroke="#94A3B8" fontSize={10} name="Trials" />
            <YAxis stroke="#94A3B8" fontSize={10} domain={["auto", "auto"]} name="Sharpe Ratio" />
            <Tooltip
              contentStyle={{
                backgroundColor: "#111827",
                borderColor: "#1F2937",
                borderRadius: "4px",
                fontSize: "10px",
                color: "#FFFFFF"
              }}
            />
            <Line type="monotone" dataKey="value" name="Trial Sharpe" stroke="#94A3B8" strokeWidth={1} dot={{ r: 2 }} />
            <Line type="monotone" dataKey="best" name="Best Sharpe" stroke="#00D4FF" strokeWidth={2} dot={false} />
          </LineChart>
        </ResponsiveContainer>
      </div>

      <div className="grid grid-cols-2 gap-4 text-xs font-semibold text-mutedCustom uppercase font-mono border-t border-borderCustom pt-2">
        <div>
          <span>Optimal Learning Rate:</span>
          <span className="block text-white font-bold mt-0.5">0.0245</span>
        </div>
        <div>
          <span>Optimal Max Depth (XGB):</span>
          <span className="block text-white font-bold mt-0.5">6</span>
        </div>
      </div>
    </div>
  );
};
export default HyperparameterLab;
