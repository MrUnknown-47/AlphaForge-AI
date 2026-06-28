"use client";

import React from "react";
import { ProgressBar } from "../ui/ProgressBar";

export const RiskMonitor = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Risk Limits Monitor</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="grid grid-cols-2 gap-4">
          <div className="border-b border-borderCustom pb-2">
            <span>Portfolio Exposure Limit (Max 50%)</span>
            <span className="block text-white font-mono mt-1">42.1%</span>
            <ProgressBar value={84} className="mt-1" />
          </div>
          <div className="border-b border-borderCustom pb-2">
            <span>Daily Loss Limit (Max 3%)</span>
            <span className="block text-white font-mono mt-1">0.12%</span>
            <ProgressBar value={4} className="mt-1" />
          </div>
        </div>

        <div className="grid grid-cols-3 gap-2 text-[10px] text-mutedCustom uppercase font-bold">
          <div>
            <span>VaR 95%</span>
            <span className="block text-white font-mono mt-0.5">$12,400</span>
          </div>
          <div>
            <span>CVaR 95%</span>
            <span className="block text-white font-mono mt-0.5">$18,500</span>
          </div>
          <div>
            <span>Leverage</span>
            <span className="block text-accentCustom font-mono mt-0.5">1.2x</span>
          </div>
        </div>
      </div>
    </div>
  );
};
export default RiskMonitor;
