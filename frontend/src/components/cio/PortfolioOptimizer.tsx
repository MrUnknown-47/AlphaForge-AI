"use client";

import React, { useState } from "react";
import { Badge } from "../ui/Badge";
import { Button } from "../ui/Button";

export const PortfolioOptimizer: React.FC = () => {
  const [method, setMethod] = useState<"MVO" | "BLACK_LITTERMAN" | "RISK_PARITY">("MVO");

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Institutional Portfolio Optimization Engine</h4>
        <Badge variant="info">OPTIMIZER ACTIVE</Badge>
      </div>

      <div className="grid grid-cols-3 gap-2">
        {["MVO", "BLACK_LITTERMAN", "RISK_PARITY"].map((m) => (
          <button
            key={m}
            onClick={() => setMethod(m as any)}
            className={`px-3 py-2 rounded text-[10px] font-bold uppercase tracking-wider transition-colors border ${
              method === m
                ? "bg-accentCustom bg-opacity-25 border-accentCustom text-accentCustom"
                : "bg-secondaryBg border-borderCustom text-mutedCustom hover:text-white"
            }`}
          >
            {m.replace("_", " ")}
          </button>
        ))}
      </div>

      <div className="grid grid-cols-2 gap-4 text-xs font-semibold text-mutedCustom bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
        <div>
          <span>Target Portfolio Volatility Limit:</span>
          <span className="block text-white font-mono mt-1">15.0%</span>
        </div>
        <div>
          <span>Ledoit-Wolf Covariance Shrinkage:</span>
          <span className="block text-successCustom font-mono mt-1">ENABLED (15% Shrink)</span>
        </div>
      </div>

      <div className="flex justify-between items-center pt-2">
        <span className="text-[10px] text-mutedCustom uppercase font-bold">Efficient Frontier Bounds</span>
        <Button variant="primary" size="sm">CALCULATE OPTIMAL BORDER</Button>
      </div>
    </div>
  );
};

export default PortfolioOptimizer;
