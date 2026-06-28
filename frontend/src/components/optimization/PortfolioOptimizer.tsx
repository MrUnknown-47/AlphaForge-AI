"use client";

import React, { useState } from "react";
import { Button } from "../ui/Button";

interface OptimizationRow {
  ticker: string;
  current: number;
  hrp: number;
}

const hrpAllocation: OptimizationRow[] = [
  { ticker: "AAPL", current: 24.5, hrp: 28.0 },
  { ticker: "NVDA", current: 41.2, hrp: 30.0 },
  { ticker: "MSFT", current: 18.5, hrp: 25.0 },
  { ticker: "TSLA", current: 15.8, hrp: 17.0 }
];

export const PortfolioOptimizer = () => {
  const [method, setMethod] = useState("HRP");

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Hierarchical Risk Parity Optimizer</h4>
        <div className="flex gap-1">
          {["HRP", "Risk Parity"].map((m) => (
            <button
              key={m}
              onClick={() => setMethod(m)}
              className={`px-1.5 py-0.5 text-[10px] font-bold rounded uppercase tracking-wider border ${
                method === m
                  ? "bg-accentCustom text-terminal border-accentCustom"
                  : "bg-secondaryBg text-mutedCustom border-borderCustom hover:text-white"
              }`}
            >
              {m}
            </button>
          ))}
        </div>
      </div>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
        <div className="flex justify-between items-center text-xs font-bold text-mutedCustom border-b border-borderCustom pb-2 uppercase">
          <span>Asset</span>
          <div className="flex gap-12 font-mono text-[10px]">
            <span>Current Weight</span>
            <span>Optimal Weight</span>
          </div>
        </div>

        <div className="space-y-3 font-semibold text-white">
          {hrpAllocation.map((row) => (
            <div key={row.ticker} className="flex justify-between items-center">
              <span className="font-bold">{row.ticker}</span>
              <div className="flex gap-16 font-mono text-[10px]">
                <span className="text-mutedCustom">{row.current}%</span>
                <span className="text-accentCustom font-bold">{row.hrp}%</span>
              </div>
            </div>
          ))}
        </div>

        <div className="flex justify-end pt-2">
          <Button variant="primary" size="sm">APPLY HRP WEIGHTS</Button>
        </div>
      </div>
    </div>
  );
};
export default PortfolioOptimizer;
