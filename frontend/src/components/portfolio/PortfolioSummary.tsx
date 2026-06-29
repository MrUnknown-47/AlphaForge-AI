"use client";

import React from "react";
import { MetricCard } from "../ui/MetricCard";

export const PortfolioSummary: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Portfolio Summary Overview</h4>
        <span className="text-[10px] text-mutedCustom font-semibold uppercase">Realtime Live Sync</span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6">
        <MetricCard label="Portfolio Equity" value="$1,054,231.82" delta={0.24} />
        <MetricCard label="Cash Balance" value="$500,000.00" />
        <MetricCard label="Buying Power" value="$2,000,000.00" />
        <MetricCard label="Margin Status" value="4x Reg-T Leverage" />
        <MetricCard label="Daily Return" value="+$2,585.00" delta={1.12} />
      </div>
    </div>
  );
};

export default PortfolioSummary;
