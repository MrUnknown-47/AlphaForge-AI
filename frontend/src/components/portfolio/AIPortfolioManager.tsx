"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { ProgressBar } from "../ui/ProgressBar";

export const AIPortfolioManager = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">AI Portfolio Risk Diagnoses & Hedges</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
        <div className="flex justify-between items-center">
          <span className="text-mutedCustom uppercase text-[10px]">Diversification Score:</span>
          <Badge variant="success">OPTIMAL</Badge>
        </div>

        <div className="space-y-1">
          <div className="flex justify-between text-[10px] uppercase font-bold text-mutedCustom">
            <span>Overall Diversification Index</span>
            <span className="text-white font-mono">85/100</span>
          </div>
          <ProgressBar value={85} />
        </div>

        <div className="border-t border-borderCustom pt-3 space-y-2">
          <span className="block text-accentCustom font-bold uppercase text-[10px] tracking-wider">Rebalancing Suggestions</span>
          <p className="text-mutedCustom leading-relaxed text-[11px]">
            Tech sector concentration matches 84%. Suggest pruning NVDA exposure allocation from 41% to 35% target to reduce single stock tail risks.
          </p>
        </div>

        <div className="border-t border-borderCustom pt-3 space-y-2">
          <span className="block text-accentCustom font-bold uppercase text-[10px] tracking-wider">Hedge Allocations</span>
          <p className="text-mutedCustom leading-relaxed text-[11px]">
            Consider a 5% allocation in SPY puts or index options to mitigate downside shocks under volatility spike regimes.
          </p>
        </div>
      </div>
    </div>
  );
};
export default AIPortfolioManager;
