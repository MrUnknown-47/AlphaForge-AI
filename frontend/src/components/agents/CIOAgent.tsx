"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const CIOAgent = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Chief Investment Officer investment Thesis</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
        <div className="flex justify-between items-center">
          <span className="text-mutedCustom uppercase text-[10px]">Macro Outlook Strategy:</span>
          <Badge variant="success">BULL EXPANSION</Badge>
        </div>

        <div className="border-t border-borderCustom pt-3 space-y-2">
          <span className="block text-accentCustom font-bold uppercase text-[10px] tracking-wider">Investment Thesis</span>
          <p className="text-mutedCustom leading-relaxed text-[11px]">
            Semi momentum factor scores support long exposure targets on AAPL/NVDA. Under-allocation triggers suggest minor rebalancing moves.
          </p>
        </div>

        <div className="border-t border-borderCustom pt-3 space-y-2">
          <span className="block text-accentCustom font-bold uppercase text-[10px] tracking-wider">Risk Budget Allocations</span>
          <p className="text-mutedCustom leading-relaxed text-[11px]">
            Maintain net exposures under 36.5% limits. Index put protection options must be reallocated dynamically.
          </p>
        </div>
      </div>
    </div>
  );
};
export default CIOAgent;
