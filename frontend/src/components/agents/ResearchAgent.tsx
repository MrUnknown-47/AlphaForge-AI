"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const ResearchAgent = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">RAG Research Agent citations Summary</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="flex justify-between items-start border-b border-borderCustom pb-3 last:border-0 last:pb-0">
          <div className="space-y-1">
            <div className="flex items-center gap-2">
              <Badge variant="info">EARNINGS</Badge>
              <span className="text-white font-medium">NVDA Corp. Q1 Earnings call transcript</span>
            </div>
          </div>
          <span className="text-[10px] text-accentCustom font-bold">94% Confidence</span>
        </div>
      </div>
    </div>
  );
};
export default ResearchAgent;
