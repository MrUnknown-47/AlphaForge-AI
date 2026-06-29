"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const RegimeMonitor: React.FC = () => {
  const currentRegime = "BULL";
  
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Dynamic Market Regime Allocator</h4>
        <Badge variant="success">STABLE</Badge>
      </div>

      <div className="p-4 bg-secondaryBg bg-opacity-20 border border-borderCustom rounded space-y-3">
        <div className="flex justify-between items-center">
          <span className="text-xs font-bold text-mutedCustom">Current Allocation Regime:</span>
          <Badge variant="info">{currentRegime}</Badge>
        </div>
        <p className="text-xs text-mutedCustom leading-relaxed">
          The system shifts leverage budgets, asset concentrations, and hedging overlays dynamically based on Markov-switching vector autoregressive regime classifiers.
        </p>

        <div className="grid grid-cols-2 gap-4 text-xs font-semibold text-mutedCustom pt-2 border-t border-borderCustom border-opacity-40">
          <div>
            <span>Leverage Limits:</span>
            <span className="block text-white font-mono mt-1">1.5x Limit</span>
          </div>
          <div>
            <span>Hedging Required:</span>
            <span className="block text-white font-mono mt-1">OPTIONAL</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RegimeMonitor;
