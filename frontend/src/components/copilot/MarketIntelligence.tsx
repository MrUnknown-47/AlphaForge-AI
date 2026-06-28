"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const MarketIntelligence = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Market Intelligence Diagnostic</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="flex justify-between items-center">
          <span>Market Volatility Regime:</span>
          <Badge variant="success">BULLISH EXPANSION</Badge>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div className="border-b border-borderCustom pb-2">
            <span>VIX Index level:</span>
            <span className="block text-white font-mono mt-1">14.25</span>
          </div>
          <div className="border-b border-borderCustom pb-2">
            <span>Risk Sentiment:</span>
            <span className="block text-successCustom font-mono mt-1">RISK-ON</span>
          </div>
          <div>
            <span>Sector Rotation Lead:</span>
            <span className="block text-white font-mono mt-1">Technology / Semi</span>
          </div>
          <div>
            <span>Liquidity Depth:</span>
            <span className="block text-white font-mono mt-1">HIGH DEPTH</span>
          </div>
        </div>
      </div>
    </div>
  );
};
export default MarketIntelligence;
