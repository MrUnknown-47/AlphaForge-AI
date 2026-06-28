"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const SECResearch = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">SEC Filing Intelligence Terminal</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs">
        <div className="flex justify-between items-center">
          <span className="font-bold text-white uppercase">Form 10-Q - Apple Inc.</span>
          <Badge variant="info">Mar 2026</Badge>
        </div>

        <div className="space-y-3 font-semibold text-mutedCustom">
          <div>
            <span className="block text-accentCustom text-[10px] uppercase font-bold mb-1">Management Commentary</span>
            <p className="leading-relaxed">
              Management indicates margins remain robust led by services revenue lines. Supply chain variables are fully stabilized.
            </p>
          </div>
          <div className="border-t border-borderCustom pt-3">
            <span className="block text-accentCustom text-[10px] uppercase font-bold mb-1">Key Risk Factors</span>
            <p className="leading-relaxed text-dangerCustom">
              Macro conditions and interest rate levels might impact consumer spending margins over Q3.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};
export default SECResearch;
