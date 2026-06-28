"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { ProgressBar } from "../ui/ProgressBar";

export const EarningsResearch = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Earnings Sentiment Analyzer</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
        <div className="flex justify-between items-center">
          <span className="text-mutedCustom uppercase text-[10px]">Management Sentiment:</span>
          <Badge variant="success">BULLISH SENTIMENT</Badge>
        </div>

        <div className="space-y-1">
          <div className="flex justify-between text-[10px] uppercase font-bold text-mutedCustom">
            <span>Bullish Score Ratio</span>
            <span className="text-white font-mono">82%</span>
          </div>
          <ProgressBar value={82} />
        </div>

        <div className="space-y-1">
          <div className="flex justify-between text-[10px] uppercase font-bold text-mutedCustom">
            <span>Management Confidence Level</span>
            <span className="text-white font-mono">91%</span>
          </div>
          <ProgressBar value={91} />
        </div>
      </div>
    </div>
  );
};
export default EarningsResearch;
