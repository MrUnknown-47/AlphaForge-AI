"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const PortfolioAgent = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Portfolio Manager Agent Decisions</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
        <div className="flex justify-between items-center">
          <span className="text-mutedCustom uppercase text-[10px]">Optimal Rebalance Strategy:</span>
          <Badge variant="success">HRP WEIGHTS REBALANCED</Badge>
        </div>

        <div className="border-t border-borderCustom pt-3 space-y-2">
          <span className="block text-accentCustom font-bold uppercase text-[10px] tracking-wider">Weight Reallocations Details</span>
          <p className="text-mutedCustom leading-relaxed text-[11px]">
            Targeting long positions alignment. Net exposure allocations adjusted dynamically to 36.5% levels.
          </p>
        </div>
      </div>
    </div>
  );
};
export default PortfolioAgent;
