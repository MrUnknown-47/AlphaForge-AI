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

const capacityCurve = [
  { aum: "1M", slippage: 0.01, sharpe: 1.85 },
  { name: "10M", slippage: 0.05, sharpe: 1.80 },
  { name: "50M", slippage: 0.12, sharpe: 1.70 },
  { name: "100M", slippage: 0.25, sharpe: 1.50 },
  { name: "500M", slippage: 0.65, sharpe: 0.85 }
];

export const CapacitySimulator = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">AUM Capacity & Sharpe decay Curve</h4>

      <div className="h-48 w-full bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
        <ResponsiveContainer width="100%" height="100%">
          <ComposedChart data={capacityCurve}>
            <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
            <XAxis dataKey="name" stroke="#94A3B8" fontSize={10} name="AUM Size" />
            <YAxis yAxisId="left" stroke="#94A3B8" fontSize={10} domain={["auto", "auto"]} name="Sharpe" />
            <YAxis yAxisId="right" orientation="right" stroke="#EF4444" fontSize={10} domain={[0, 1]} name="Slippage %" />
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
            <Line yAxisId="left" type="monotone" dataKey="sharpe" name="Sharpe Index" stroke="#00D4FF" strokeWidth={2} dot={false} />
            <Line yAxisId="right" type="monotone" dataKey="slippage" name="Slippage %" stroke="#EF4444" strokeWidth={1} dot={false} />
          </ComposedChart>
        </ResponsiveContainer>
      </div>

      <div className="grid grid-cols-2 gap-4 text-xs font-semibold text-mutedCustom uppercase font-mono border-t border-borderCustom pt-2">
        <div>
          <span>Optimal Fund capacity:</span>
          <span className="block text-white font-bold mt-0.5">$50,000,000</span>
        </div>
        <div>
          <span>Max slippage decay:</span>
          <span className="block text-white font-bold mt-0.5">12 bps</span>
        </div>
      </div>
    </div>
  );
};
export default CapacitySimulator;
