"use client";

import React from "react";

export const RiskAnalytics: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Risk Metrics (Volatility & Drawdowns)</h4>
        <span className="text-[10px] text-mutedCustom font-semibold uppercase">Daily VAR</span>
      </div>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="grid grid-cols-2 gap-4">
          <div className="border-b border-borderCustom pb-2">
            <span className="text-[10px] uppercase block tracking-wider">Value-at-Risk (VaR 95%)</span>
            <span className="block text-white font-mono mt-1">$12,400</span>
          </div>
          <div className="border-b border-borderCustom pb-2">
            <span className="text-[10px] uppercase block tracking-wider">Conditional VaR (CVaR)</span>
            <span className="block text-white font-mono mt-1">$18,500</span>
          </div>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div className="border-b border-borderCustom pb-2">
            <span className="text-[10px] uppercase block tracking-wider">Portfolio Beta (vs SPY)</span>
            <span className="block text-accentCustom font-mono mt-1">0.88</span>
          </div>
          <div className="border-b border-borderCustom pb-2">
            <span className="text-[10px] uppercase block tracking-wider">Sharpe Ratio</span>
            <span className="block text-successCustom font-mono mt-1">1.85</span>
          </div>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div>
            <span className="text-[10px] uppercase block tracking-wider">Sortino Ratio</span>
            <span className="block text-successCustom font-mono mt-1">2.14</span>
          </div>
          <div>
            <span className="text-[10px] uppercase block tracking-wider">Calmar Ratio</span>
            <span className="block text-white font-mono mt-1">4.76</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RiskAnalytics;
