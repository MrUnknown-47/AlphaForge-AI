"use client";

import React from "react";
import { ProgressBar } from "../ui/ProgressBar";

export const MemoryCenter = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Agent Vector Memory Growth</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="space-y-1.5">
          <div className="flex justify-between uppercase text-[10px] font-bold">
            <span>Conversational Memory Size (100K max)</span>
            <span className="text-white font-mono">24.5K Vectors</span>
          </div>
          <ProgressBar value={24.5} />
        </div>

        <div className="space-y-1.5 border-t border-borderCustom pt-3">
          <div className="flex justify-between uppercase text-[10px] font-bold">
            <span>Retrieval Quality Index</span>
            <span className="text-successCustom font-mono">92%</span>
          </div>
          <ProgressBar value={92} />
        </div>
      </div>
    </div>
  );
};
export default MemoryCenter;
