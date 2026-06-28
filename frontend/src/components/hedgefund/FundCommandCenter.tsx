"use client";

import React from "react";
import { MetricCard } from "../ui/MetricCard";
import { Button } from "../ui/Button";

export const FundCommandCenter = ({ onStressTest }: { onStressTest: () => void }) => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Hedge Fund AUM & Leverage Command Center</h4>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <MetricCard label="Assets under Management (AUM)" value="$10,542,318.20" delta={0.24} />
        <MetricCard label="Net Asset Value (NAV)" value="105.42" />
        <MetricCard label="Fund Leverage ratio" value="1.20x" />
        <MetricCard label="Fund Sharpe Index" value="1.85" />
      </div>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-xs font-semibold text-mutedCustom bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 uppercase">
        <div>
          <span>Gross Exposure Limit:</span>
          <span className="block text-white font-mono mt-1">42.1%</span>
        </div>
        <div>
          <span>Net Exposure Limit:</span>
          <span className="block text-white font-mono mt-1">36.5%</span>
        </div>
        <div>
          <span>Value-at-Risk (95% VaR):</span>
          <span className="block text-dangerCustom font-mono mt-1">$124,000</span>
        </div>
        <div>
          <span>Expected Shortfall (CVaR):</span>
          <span className="block text-dangerCustom font-mono mt-1">$185,000</span>
        </div>
      </div>

      <div className="flex gap-3 justify-end">
        <Button variant="secondary" size="sm" onClick={onStressTest}>Stress Test</Button>
        <Button variant="danger" size="sm">Liquidate Assets</Button>
      </div>
    </div>
  );
};
export default FundCommandCenter;
