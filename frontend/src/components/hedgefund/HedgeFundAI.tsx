"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { ProgressBar } from "../ui/ProgressBar";

export const HedgeFundAI = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">AI Portfolio Quality Diagnoses</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
        <div className="flex justify-between items-center">
          <span className="text-mutedCustom uppercase text-[10px]">AUM Viability:</span>
          <Badge variant="success">STABLE CAPACITY</Badge>
        </div>

        <div className="space-y-1">
          <div className="flex justify-between text-[10px] uppercase font-bold text-mutedCustom">
            <span>Overall Capital Efficiency Score</span>
            <span className="text-white font-mono">88/100</span>
          </div>
          <ProgressBar value={88} />
        </div>

        <div className="border-t border-borderCustom pt-3 space-y-2">
          <span className="block text-accentCustom font-bold uppercase text-[10px] tracking-wider">Hedge Allocation Suggestions</span>
          <p className="text-mutedCustom leading-relaxed text-[11px]">
            HRP models indicate semi momentum rotation. Suggest allocating 5% cash reserves in index protection puts to mitigate downside tail-risks.
          </p>
        </div>
      </div>
    </div>
  );
};
export default HedgeFundAI;
