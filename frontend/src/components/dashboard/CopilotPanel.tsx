"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const CopilotPanel = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">AI Copilot Research Feed</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-3 text-xs">
        <div>
          <span className="block font-bold text-accentCustom uppercase mb-1">Market Sentiment Overview</span>
          <p className="text-mutedCustom leading-relaxed">
            Market sentiment remains bullish led by tech sector rotation. High conviction on NVDA and AAPL based on XGBoost/LSTM signals.
          </p>
        </div>

        <div className="border-t border-borderCustom pt-3">
          <span className="block font-bold text-accentCustom uppercase mb-1">Risk Assessment Summary</span>
          <p className="text-mutedCustom leading-relaxed">
            Total exposure is 42.1%, safely below the 50% system guardrails limit. Drawdown is stable.
          </p>
        </div>

        <div className="border-t border-borderCustom pt-3 space-y-2">
          <span className="block font-bold text-white uppercase text-[10px] tracking-wider">Research Alerts</span>
          <ul className="space-y-1.5 font-semibold text-mutedCustom text-[10px] uppercase">
            <li className="flex items-center gap-2">
              <span className="text-accentCustom">●</span> Rebalanced NVDA portfolio exposure allocation
            </li>
            <li className="flex items-center gap-2">
              <span className="text-accentCustom">●</span> Stop loss threshold trigger matched on minor index hedge
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
};
export default CopilotPanel;
