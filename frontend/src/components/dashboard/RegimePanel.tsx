"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const RegimePanel = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Market Regime Classification</h4>
      
      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4">
        <div className="flex justify-between items-center">
          <span className="text-xs font-bold text-mutedCustom uppercase">Regime Index:</span>
          <Badge variant="success">BULLISH EXPANSION</Badge>
        </div>

        <div className="grid grid-cols-2 gap-4 text-xs font-semibold text-mutedCustom">
          <div className="border-b border-borderCustom pb-2">
            <span>Volatility Index (VIX):</span>
            <span className="block text-white font-mono mt-1">14.25</span>
          </div>
          <div className="border-b border-borderCustom pb-2">
            <span>SPY Volatility:</span>
            <span className="block text-white font-mono mt-1">12.8%</span>
          </div>
          <div>
            <span>Market Beta:</span>
            <span className="block text-white font-mono mt-1">0.95</span>
          </div>
          <div>
            <span>Detector Confidence:</span>
            <span className="block text-accentCustom font-mono mt-1">88.5%</span>
          </div>
        </div>

        <div className="text-[10px] text-mutedCustom bg-cardBg border border-borderCustom p-2.5 rounded uppercase leading-relaxed font-semibold">
          Regime classifier indicates structural bull market. Re-allocating model weights to momentum signals.
        </div>
      </div>
    </div>
  );
};
export default RegimePanel;
