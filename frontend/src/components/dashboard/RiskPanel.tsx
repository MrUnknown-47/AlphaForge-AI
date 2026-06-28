"use client";

import React from "react";
import { ProgressBar } from "../ui/ProgressBar";

export const RiskPanel = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Risk & Drawdown Telemetry</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="grid grid-cols-2 gap-4">
          <div className="border-b border-borderCustom pb-2">
            <span>VaR (95% 1-Day):</span>
            <span className="block text-white font-mono mt-1">$12,400</span>
          </div>
          <div className="border-b border-borderCustom pb-2">
            <span>CVaR (Expected Shortfall):</span>
            <span className="block text-white font-mono mt-1">$18,500</span>
          </div>
        </div>

        <div className="space-y-1.5">
          <div className="flex justify-between uppercase text-[10px] font-bold">
            <span>Portfolio Beta Target</span>
            <span className="text-white font-mono">0.88</span>
          </div>
          <ProgressBar value={88} />
        </div>

        <div className="space-y-1.5">
          <div className="flex justify-between uppercase text-[10px] font-bold">
            <span>Current Exposure Limit (Max 50%)</span>
            <span className="text-white font-mono">42.1%</span>
          </div>
          <ProgressBar value={84} />
        </div>

        <div className="space-y-1.5">
          <div className="flex justify-between uppercase text-[10px] font-bold">
            <span>Daily Loss Limit (Max 3%)</span>
            <span className="text-white font-mono">0.12%</span>
          </div>
          <ProgressBar value={4} />
        </div>
      </div>
    </div>
  );
};
export default RiskPanel;
