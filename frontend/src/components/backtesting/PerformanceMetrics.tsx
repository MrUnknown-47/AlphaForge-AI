"use client";

import React from "react";
import { MetricCard } from "../ui/MetricCard";

export const PerformanceMetrics: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Backtest Key Performance & Risk Ratios</h4>
        <span className="text-[10px] text-mutedCustom font-semibold uppercase">KPI Analysis</span>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4">
        <MetricCard label="Sharpe Ratio" value="1.85" delta={0.15} />
        <MetricCard label="Sortino Ratio" value="2.12" />
        <MetricCard label="Calmar Ratio" value="4.85" />
        <MetricCard label="Win Rate (Hit %)" value="62.4%" />
        <MetricCard label="Profit Factor" value="2.14" />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs font-semibold text-mutedCustom bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
        <div>
          <span>Annual Volatility:</span>
          <span className="block text-white font-mono mt-1">11.8%</span>
        </div>
        <div>
          <span>Beta Coefficient (vs SPY):</span>
          <span className="block text-accentCustom font-mono mt-1">0.88</span>
        </div>
        <div>
          <span>Value-at-Risk (95% Daily VaR):</span>
          <span className="block text-warningCustom font-mono mt-1">$8,250</span>
        </div>
      </div>
    </div>
  );
};

export default PerformanceMetrics;
