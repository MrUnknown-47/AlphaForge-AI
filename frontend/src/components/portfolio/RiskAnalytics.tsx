"use client";

import React from "react";
import { ProgressBar } from "../ui/ProgressBar";

export const RiskAnalytics = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Advanced Risk Analytics & Factor Attribution</h4>

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
          <div className="border-b border-borderCustom pb-2">
            <span>Annualized Volatility:</span>
            <span className="block text-white font-mono mt-1">11.85%</span>
          </div>
          <div className="border-b border-borderCustom pb-2">
            <span>Tracking Error (vs SPY):</span>
            <span className="block text-white font-mono mt-1">2.14%</span>
          </div>
        </div>

        <div className="grid grid-cols-3 gap-2 text-[10px] text-mutedCustom uppercase font-bold">
          <div>
            <span>Information Ratio</span>
            <span className="block text-white font-mono mt-0.5">1.45</span>
          </div>
          <div>
            <span>Treynor Ratio</span>
            <span className="block text-white font-mono mt-0.5">18.42%</span>
          </div>
          <div>
            <span>Portfolio Beta</span>
            <span className="block text-accentCustom font-mono mt-0.5">0.88</span>
          </div>
        </div>
      </div>
    </div>
  );
};
export default RiskAnalytics;
