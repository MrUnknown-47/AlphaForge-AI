"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const CIOAgent = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Chief Investment Officer daily Briefing</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
        <div className="flex justify-between items-center">
          <span className="text-mutedCustom uppercase text-[10px]">Strategy Recommendation:</span>
          <Badge variant="success">DEPLOY TFT TRANSFORMER (EXP_702)</Badge>
        </div>

        <div className="border-t border-borderCustom pt-3 space-y-2">
          <span className="block text-accentCustom font-bold uppercase text-[10px] tracking-wider">Market Executive Summary</span>
          <p className="text-mutedCustom leading-relaxed text-[11px]">
            Market regimes align with structural bull expansions. Technology leadership remains high conviction led by semi momentum factors.
          </p>
        </div>

        <div className="border-t border-borderCustom pt-3 space-y-2">
          <span className="block text-accentCustom font-bold uppercase text-[10px] tracking-wider">Hedge Allocation Outlook</span>
          <p className="text-mutedCustom leading-relaxed text-[11px]">
            Maintain active exposure limits under 42.1% levels. Covariance updates suggest index put hedges rebalancing triggers.
          </p>
        </div>
      </div>
    </div>
  );
};
export default CIOAgent;
