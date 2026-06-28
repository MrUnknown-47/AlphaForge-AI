"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const DebateChamber = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Multi-Agent Debate Chamber & Consensus logs</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
        <div className="flex justify-between items-center">
          <span className="text-mutedCustom uppercase text-[10px]">Overall Consensus Score:</span>
          <Badge variant="success">88/100 (HIGH CONSENSUS)</Badge>
        </div>

        <div className="space-y-3">
          <div className="border-t border-borderCustom pt-3 space-y-1">
            <span className="text-successCustom uppercase font-bold">[BULL AGENT PROPOSITION]</span>
            <p className="text-white leading-relaxed font-normal">
              High conviction score (94%) on tech momentum supports allocation. Margin levels remain strong YTD.
            </p>
          </div>

          <div className="border-t border-borderCustom pt-3 space-y-1">
            <span className="text-dangerCustom uppercase font-bold">[BEAR AGENT OBJECTION]</span>
            <p className="text-white leading-relaxed font-normal">
              Macro interest rates levels might suppress consumer margin indexes over the medium term.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};
export default DebateChamber;
