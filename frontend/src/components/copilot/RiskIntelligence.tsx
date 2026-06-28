"use client";

import React from "react";
import { ProgressBar } from "../ui/ProgressBar";

export const RiskIntelligence = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Risk Intelligence Telemetry</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="grid grid-cols-2 gap-4">
          <div className="border-b border-borderCustom pb-2">
            <span>Value-at-Risk (VaR 95%):</span>
            <span className="block text-white font-mono mt-1">$12,400</span>
          </div>
          <div className="border-b border-borderCustom pb-2">
            <span>Conditional VaR (CVaR):</span>
            <span className="block text-white font-mono mt-1">$18,500</span>
          </div>
        </div>

        <div className="space-y-1.5">
          <div className="flex justify-between uppercase text-[10px] font-bold">
            <span>Current Exposure (Max 50%)</span>
            <span className="text-white font-mono">42.1%</span>
          </div>
          <ProgressBar value={84} />
        </div>
      </div>
    </div>
  );
};
export default RiskIntelligence;
