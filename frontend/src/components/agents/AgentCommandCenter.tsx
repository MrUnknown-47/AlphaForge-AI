"use client";

import React, { useState } from "react";
import { Badge } from "../ui/Badge";
import { Button } from "../ui/Button";

export const AgentCommandCenter: React.FC = () => {
  const [userVote, setUserVote] = useState<string | null>(null);

  const votes = [
    { type: "BUY", count: 4, pct: 57 },
    { type: "SELL", count: 0, pct: 0 },
    { type: "HOLD", count: 2, pct: 28 },
    { type: "REDUCE", count: 0, pct: 0 },
    { type: "HEDGE", count: 1, pct: 14 }
  ];

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Committee Voting Panel</h4>
        <Badge variant="info">Consensus: BUY (57%)</Badge>
      </div>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
        <div className="grid grid-cols-5 gap-2">
          {votes.map((v) => (
            <button
              key={v.type}
              onClick={() => setUserVote(v.type)}
              className={`p-3 rounded text-center border transition-all ${
                userVote === v.type
                  ? "bg-accentCustom bg-opacity-25 border-accentCustom text-accentCustom"
                  : "bg-cardBg border-borderCustom text-mutedCustom hover:text-white"
              }`}
            >
              <div className="font-bold text-sm">{v.type}</div>
              <div className="text-[10px] mt-1 font-mono">{v.pct}% ({v.count} votes)</div>
            </button>
          ))}
        </div>

        <div className="grid grid-cols-2 gap-4 border-t border-borderCustom pt-3 font-mono">
          <div>
            <span className="text-[10px] text-mutedCustom block uppercase tracking-wider">Final Consensus</span>
            <span className="text-sm font-bold text-successCustom">BUY TARGET ALLOCATION</span>
          </div>
          <div>
            <span className="text-[10px] text-mutedCustom block uppercase tracking-wider">Confidence %</span>
            <span className="text-sm font-bold text-white">82.5%</span>
          </div>
        </div>

        <div className="border-t border-borderCustom pt-3 space-y-1">
          <span className="text-[10px] text-mutedCustom block uppercase tracking-wider">Explainability Output (LIME/SHAP Attribution)</span>
          <p className="text-[10px] text-white font-mono leading-relaxed bg-black bg-opacity-40 p-2 border border-borderCustom rounded">
            Consensus BUY triggered by: Tech Momentum loading (+0.42), Yield Curve shift (+0.18), and positive Social Sentiment spikes (+0.25). HEDGE recommendations were active due to Macro inflation risks (-0.11).
          </p>
        </div>
      </div>
    </div>
  );
};

export default AgentCommandCenter;
