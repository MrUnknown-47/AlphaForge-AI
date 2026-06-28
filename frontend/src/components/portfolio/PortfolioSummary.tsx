"use client";

import React from "react";
import { MetricCard } from "../ui/MetricCard";

export const PortfolioSummary = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Aladdin Portfolio Metrics Summary</h4>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <MetricCard label="Portfolio Value" value="$1,054,231.82" delta={0.24} />
        <MetricCard label="Cash Balance" value="$500,000.00" />
        <MetricCard label="Sharpe Ratio" value="1.85" delta={1.2} />
        <MetricCard label="Sortino Ratio" value="2.14" />
      </div>
      
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-xs font-semibold text-mutedCustom bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
        <div>
          <span>Gross Exposure:</span>
          <span className="block text-white font-mono mt-1">42.1%</span>
        </div>
        <div>
          <span>Net Exposure:</span>
          <span className="block text-white font-mono mt-1">36.5%</span>
        </div>
        <div>
          <span>YTD Return:</span>
          <span className="block text-successCustom font-mono mt-1">+14.85%</span>
        </div>
        <div>
          <span>Calmar Ratio:</span>
          <span className="block text-white font-mono mt-1">4.76</span>
        </div>
      </div>
    </div>
  );
};
export default PortfolioSummary;
