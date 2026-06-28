"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const StrategyOptimizer = () => {
  const params = [
    { name: "Entry Probability Threshold", current: "0.70", optimal: "0.75", delta: "Sharpe +0.12" },
    { name: "Exit Probability Threshold", current: "0.30", optimal: "0.25", delta: "Sharpe +0.05" },
    { name: "Stop Loss Limit", current: "3.00%", optimal: "2.85%", delta: "Drawdown -0.24%" },
    { name: "Take Profit Target", current: "20.00%", optimal: "18.50%", delta: "Hit Rate +1.2%" }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Strategy Hyperparameter Optimizer</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="flex justify-between items-center text-xs font-bold text-mutedCustom border-b border-borderCustom pb-2 uppercase">
          <span>Parameter Target</span>
          <div className="flex gap-12 font-mono text-[10px]">
            <span>Current</span>
            <span>Optimal</span>
          </div>
        </div>

        <div className="space-y-3">
          {params.map((row) => (
            <div key={row.name} className="flex justify-between items-center">
              <span className="text-white uppercase">{row.name}</span>
              <div className="flex items-center gap-12 font-mono text-[10px]">
                <span className="text-mutedCustom">{row.current}</span>
                <span className="text-accentCustom font-bold">{row.optimal}</span>
                <Badge variant="success">{row.delta}</Badge>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
export default StrategyOptimizer;
