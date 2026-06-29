"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { ProgressBar } from "../ui/ProgressBar";

export const PortfolioConstruction: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Portfolio Construction & Exposure Limits</h4>
        <span className="text-[10px] text-mutedCustom font-semibold uppercase">EXPOSURES</span>
      </div>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="space-y-1.5">
          <div className="flex justify-between uppercase text-[10px] font-bold">
            <span>Gross Exposure (Limit: 200.0%)</span>
            <span className="text-white font-mono">135.0%</span>
          </div>
          <ProgressBar value={67.5} />
        </div>

        <div className="space-y-1.5 border-t border-borderCustom pt-3">
          <div className="flex justify-between uppercase text-[10px] font-bold">
            <span>Net Exposure Target (Beta Adjusted)</span>
            <span className="text-white font-mono">85.0%</span>
          </div>
          <ProgressBar value={85.0} />
        </div>

        <div className="space-y-1.5 border-t border-borderCustom pt-3">
          <div className="flex justify-between uppercase text-[10px] font-bold">
            <span>Portfolio Net Beta Factor</span>
            <span className="text-white font-mono">1.12x</span>
          </div>
          <ProgressBar value={56.0} />
        </div>
      </div>
    </div>
  );
};

export default PortfolioConstruction;
