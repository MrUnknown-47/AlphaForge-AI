"use client";

import React, { useState } from "react";
import { Badge } from "../ui/Badge";
import { Button } from "../ui/Button";

interface WeightAllocation {
  ticker: string;
  current: number;
  optimal: number;
}

const allocations: Record<string, WeightAllocation[]> = {
  "Mean Variance": [
    { ticker: "AAPL", current: 24.5, optimal: 20.0 },
    { ticker: "NVDA", current: 41.2, optimal: 45.0 },
    { ticker: "MSFT", current: 18.5, optimal: 25.0 },
    { ticker: "TSLA", current: 15.8, optimal: 10.0 }
  ],
  "Risk Parity": [
    { ticker: "AAPL", current: 24.5, optimal: 30.0 },
    { ticker: "NVDA", current: 41.2, optimal: 20.0 },
    { ticker: "MSFT", current: 18.5, optimal: 35.0 },
    { ticker: "TSLA", current: 15.8, optimal: 15.0 }
  ]
};

export const OptimizerPanel = () => {
  const [model, setModel] = useState("Mean Variance");
  const weights = allocations[model] || allocations["Mean Variance"];

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Portfolio Optimization Engine</h4>
        <div className="flex gap-1.5">
          {["Mean Variance", "Risk Parity"].map((m) => (
            <button
              key={m}
              onClick={() => setModel(m)}
              className={`px-2 py-0.5 text-[10px] font-bold rounded uppercase tracking-wider border ${
                model === m
                  ? "bg-accentCustom text-terminal border-accentCustom"
                  : "bg-secondaryBg text-mutedCustom border-borderCustom hover:text-white"
              }`}
            >
              {m}
            </button>
          ))}
        </div>
      </div>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs">
        <div className="flex justify-between items-center font-bold text-mutedCustom uppercase border-b border-borderCustom pb-2">
          <span>Asset</span>
          <div className="flex gap-12 font-mono text-[10px]">
            <span>Current Weight</span>
            <span>Optimal Weight</span>
          </div>
        </div>

        <div className="space-y-3 font-semibold text-white">
          {weights.map((row) => (
            <div key={row.ticker} className="flex justify-between items-center">
              <span className="font-bold">{row.ticker}</span>
              <div className="flex gap-16 font-mono text-[10px]">
                <span className="text-mutedCustom">{row.current}%</span>
                <span className="text-accentCustom font-bold">{row.optimal}%</span>
              </div>
            </div>
          ))}
        </div>

        <div className="flex justify-end pt-2">
          <Button variant="primary" size="sm">REBALANCE PORTFOLIO TARGETS</Button>
        </div>
      </div>
    </div>
  );
};
export default OptimizerPanel;
