"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const HedgeFundAdvisor = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">AI Hedge Fund Advisor Suggestions</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
        <div className="flex justify-between items-center">
          <span className="text-mutedCustom uppercase text-[10px]">Optimal Strategy Candidate:</span>
          <Badge variant="success">TFT TRANSFORMER (OPT_RUN_702)</Badge>
        </div>

        <div className="border-t border-borderCustom pt-3 space-y-2">
          <span className="block text-accentCustom font-bold uppercase text-[10px] tracking-wider">Capacity Limits Analysis</span>
          <p className="text-mutedCustom leading-relaxed text-[11px]">
            Estimated strategy capacity stands at $50M before transaction slippage impact triggers signal alpha decay.
          </p>
        </div>

        <div className="border-t border-borderCustom pt-3 space-y-2">
          <span className="block text-accentCustom font-bold uppercase text-[10px] tracking-wider">Deployment Recommendations</span>
          <p className="text-mutedCustom leading-relaxed text-[11px]">
            HRP portfolio weights rebalancing suggested. Deploy OPT_RUN_702 to live shadow validation mode.
          </p>
        </div>
      </div>
    </div>
  );
};
export default HedgeFundAdvisor;
