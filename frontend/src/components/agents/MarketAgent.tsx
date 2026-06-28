"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const MarketAgent = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Market Intelligence Agent Indicators</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="flex justify-between items-center">
          <span>Volatility Regime Index:</span>
          <Badge variant="success">BULLISH EXPANSION</Badge>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div className="border-b border-borderCustom pb-2">
            <span>Risk Sentiment Model:</span>
            <span className="block text-successCustom font-mono mt-1">RISK-ON</span>
          </div>
          <div className="border-b border-borderCustom pb-2">
            <span>Leading Sector Momentum:</span>
            <span className="block text-white font-mono mt-1">Technology</span>
          </div>
        </div>
      </div>
    </div>
  );
};
export default MarketAgent;
