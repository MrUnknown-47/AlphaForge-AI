"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { ProgressBar } from "../ui/ProgressBar";

export const SecurityOperations = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">SOC threat Intelligence center</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
        <div className="flex justify-between items-center">
          <span className="text-mutedCustom uppercase text-[10px]">Threat Level Rating:</span>
          <Badge variant="success">LOW THREAT</Badge>
        </div>

        <div className="space-y-1">
          <div className="flex justify-between text-[10px] uppercase font-bold text-mutedCustom">
            <span>Overall Security Score</span>
            <span className="text-white font-mono">98/100</span>
          </div>
          <ProgressBar value={98} />
        </div>
      </div>
    </div>
  );
};
export default SecurityOperations;
