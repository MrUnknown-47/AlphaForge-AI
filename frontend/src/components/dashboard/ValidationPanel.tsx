"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const ValidationPanel = () => {
  const scorecards = [
    { metric: "Sharpe Ratio", target: "> 1.50", current: "1.85", status: "PASS" },
    { metric: "Hit Ratio", target: "> 55%", current: "62.4%", status: "PASS" },
    { metric: "Max Drawdown", target: "< 20%", current: "3.12%", status: "PASS" },
    { metric: "Population Stability (PSI)", target: "< 0.1", current: "0.08", status: "PASS" },
    { metric: "Probability of Ruin", target: "< 1%", current: "0.01%", status: "PASS" }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Validation Scorecard Gates</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4">
        <div className="flex justify-between items-center text-xs font-bold text-mutedCustom border-b border-borderCustom pb-2">
          <span>Metric</span>
          <div className="flex gap-12 font-mono text-[10px]">
            <span>Target</span>
            <span>Current</span>
          </div>
        </div>

        <div className="space-y-3">
          {scorecards.map((gate) => (
            <div key={gate.metric} className="flex justify-between items-center text-xs font-semibold">
              <span className="text-white uppercase">{gate.metric}</span>
              <div className="flex items-center gap-6 font-mono text-[10px]">
                <span className="text-mutedCustom">{gate.target}</span>
                <span className="text-accentCustom">{gate.current}</span>
                <Badge variant="success">{gate.status}</Badge>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
export default ValidationPanel;
