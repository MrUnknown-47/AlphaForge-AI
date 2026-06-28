"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const TradingOperations = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Live Desk Trading Operations</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="flex justify-between border-b border-borderCustom pb-2">
          <span>Executed orders (YTD):</span>
          <span className="text-white font-mono">1,424 Executed</span>
        </div>
        <div className="flex justify-between border-b border-borderCustom pb-2">
          <span>Order rejection rate:</span>
          <span className="text-successCustom font-mono">0.00%</span>
        </div>
        <div className="flex justify-between pb-2">
          <span>Alpaca Paper sync:</span>
          <Badge variant="success">ACTIVE</Badge>
        </div>
      </div>
    </div>
  );
};
export default TradingOperations;
