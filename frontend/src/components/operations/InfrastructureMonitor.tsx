"use client";

import React from "react";
import { ProgressBar } from "../ui/ProgressBar";

export const InfrastructureMonitor = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">NOC Infrastructure Metrics</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="space-y-1.5">
          <div className="flex justify-between uppercase text-[10px] font-bold">
            <span>CPU core utilization (8 Cores)</span>
            <span className="text-white font-mono">24.5%</span>
          </div>
          <ProgressBar value={25} />
        </div>

        <div className="space-y-1.5 border-t border-borderCustom pt-3">
          <div className="flex justify-between uppercase text-[10px] font-bold">
            <span>RAM memory consumption (16GB Cap)</span>
            <span className="text-white font-mono">42.1%</span>
          </div>
          <ProgressBar value={42} />
        </div>
      </div>
    </div>
  );
};
export default InfrastructureMonitor;
