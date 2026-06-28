"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { ProgressBar } from "../ui/ProgressBar";

export const AIResearchAssistant = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">AI Quantitative Research Analyst</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
        <div className="flex justify-between items-center">
          <span className="text-mutedCustom uppercase text-[10px]">Overfitting Index:</span>
          <Badge variant="success">LOW RISK (PASS)</Badge>
        </div>

        <div className="space-y-1">
          <div className="flex justify-between text-[10px] uppercase font-bold text-mutedCustom">
            <span>Probability of Overfitting</span>
            <span className="text-white font-mono">12%</span>
          </div>
          <ProgressBar value={12} />
        </div>

        <div className="border-t border-borderCustom pt-3 space-y-2">
          <span className="block text-accentCustom font-bold uppercase text-[10px] tracking-wider">Strengths & Capacity</span>
          <p className="text-mutedCustom leading-relaxed text-[11px]">
            Strong predictive power during low-volatility bullish regimes. Signals decay is slow, supporting holding periods up to 3 days.
          </p>
        </div>

        <div className="border-t border-borderCustom pt-3 space-y-2">
          <span className="block text-accentCustom font-bold uppercase text-[10px] tracking-wider">Regime Vulnerabilities</span>
          <p className="text-mutedCustom leading-relaxed text-[11px]">
            Model show minor decay during volatile sideways periods where mean-reversion factors dominate. Consider integrating RSI features.
          </p>
        </div>
      </div>
    </div>
  );
};
export default AIResearchAssistant;
