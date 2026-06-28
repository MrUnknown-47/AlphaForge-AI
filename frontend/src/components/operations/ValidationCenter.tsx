"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const ValidationCenter = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Shadow validation Engine Metrics</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="flex justify-between border-b border-borderCustom pb-2">
          <span>YTD Sharpe ratio:</span>
          <span className="text-accentCustom font-mono">1.85 (STABLE)</span>
        </div>
        <div className="flex justify-between border-b border-borderCustom pb-2">
          <span>Overall Hit Ratio:</span>
          <span className="text-white font-mono">62.4%</span>
        </div>
        <div className="flex justify-between pb-2">
          <span>Overall status:</span>
          <Badge variant="success">PASSING GATES</Badge>
        </div>
      </div>
    </div>
  );
};
export default ValidationCenter;
