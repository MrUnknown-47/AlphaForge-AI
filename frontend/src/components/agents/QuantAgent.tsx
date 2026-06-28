"use client";

import React from "react";
import { ProgressBar } from "../ui/ProgressBar";

export const QuantAgent = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Quant Agent Factor Discovery Diagnostics</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
        <div className="space-y-1">
          <div className="flex justify-between text-[10px] uppercase font-bold text-mutedCustom">
            <span>Probability of Overfitting</span>
            <span className="text-white font-mono">12%</span>
          </div>
          <ProgressBar value={12} />
        </div>

        <div className="grid grid-cols-2 gap-4 text-xs font-semibold text-mutedCustom uppercase font-mono border-t border-borderCustom pt-3">
          <div>
            <span>Expected Sharpe Ratio:</span>
            <span className="block text-white font-bold mt-0.5">2.05</span>
          </div>
          <div>
            <span>Expected CAGR Return:</span>
            <span className="block text-successCustom font-bold mt-0.5">+22.4%</span>
          </div>
        </div>
      </div>
    </div>
  );
};
export default QuantAgent;
