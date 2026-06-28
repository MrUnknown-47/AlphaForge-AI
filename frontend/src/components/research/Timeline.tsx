"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const Timeline = () => {
  const events = [
    { date: "June 25", event: "Strategy weights rebalanced to TFT Transformer model", type: "STRATEGY" },
    { date: "June 12", event: "Apple SEC Form 10-Q filing parsed", type: "SEC FILING" },
    { date: "June 01", event: "NVIDIA Q1 2026 Earnings call recorded", type: "EARNINGS" }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">RAG Timeline Event Log</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4">
        {events.map((ev, idx) => (
          <div key={idx} className="flex justify-between items-start text-xs border-b border-borderCustom pb-3 last:border-0 last:pb-0">
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <Badge variant="info">{ev.type}</Badge>
                <span className="text-white font-medium">{ev.event}</span>
              </div>
            </div>
            <span className="text-[10px] text-mutedCustom font-semibold uppercase">{ev.date}</span>
          </div>
        ))}
      </div>
    </div>
  );
};
export default Timeline;
