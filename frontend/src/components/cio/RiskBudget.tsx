"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { ProgressBar } from "../ui/ProgressBar";

export const RiskBudget: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Asset Risk Budget Allocation</h4>
        <span className="text-[10px] text-mutedCustom font-semibold uppercase">Risk Limits</span>
      </div>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="space-y-1.5">
          <div className="flex justify-between uppercase text-[10px] font-bold">
            <span>Technology Sector Cap (Limit: 40%)</span>
            <span className="text-white font-mono">35.0%</span>
          </div>
          <ProgressBar value={87.5} />
        </div>

        <div className="space-y-1.5 border-t border-borderCustom pt-3">
          <div className="flex justify-between uppercase text-[10px] font-bold">
            <span>Healthcare Sector Cap (Limit: 40%)</span>
            <span className="text-white font-mono">15.0%</span>
          </div>
          <ProgressBar value={37.5} />
        </div>

        <div className="space-y-1.5 border-t border-borderCustom pt-3">
          <div className="flex justify-between uppercase text-[10px] font-bold">
            <span>Financials Sector Cap (Limit: 40%)</span>
            <span className="text-white font-mono">20.0%</span>
          </div>
          <ProgressBar value={50} />
        </div>
      </div>
    </div>
  );
};

export default RiskBudget;
