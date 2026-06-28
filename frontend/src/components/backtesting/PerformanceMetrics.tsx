"use client";

import React from "react";
import { MetricCard } from "../ui/MetricCard";

export const PerformanceMetrics = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Backtest Key Performance Indicators</h4>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <MetricCard label="CAGR (Annual Return)" value="+18.54%" delta={2.1} />
        <MetricCard label="Sharpe Ratio" value="1.85" />
        <MetricCard label="Profit Factor" value="2.14" />
        <MetricCard label="Hit Ratio (Win %)" value="62.4%" />
      </div>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-xs font-semibold text-mutedCustom bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
        <div>
          <span>Sortino Ratio:</span>
          <span className="block text-white font-mono mt-1">2.12</span>
        </div>
        <div>
          <span>Calmar Ratio:</span>
          <span className="block text-white font-mono mt-1">4.85</span>
        </div>
        <div>
          <span>Annual Volatility:</span>
          <span className="block text-white font-mono mt-1">11.8%</span>
        </div>
        <div>
          <span>Beta Coefficient:</span>
          <span className="block text-white font-mono mt-1">0.88</span>
        </div>
      </div>
    </div>
  );
};
export default PerformanceMetrics;
