"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const OperationsTimeline = () => {
  const events = [
    { date: "June 25", action: "Production build validation successfully completed", type: "BUILD" },
    { date: "June 12", action: "ML model weights retraining verified", type: "TRAINING" }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Operations Timeline Logs</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        {events.map((ev, idx) => (
          <div key={idx} className="flex justify-between items-start border-b border-borderCustom pb-3 last:border-0 last:pb-0">
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <Badge variant="info">{ev.type}</Badge>
                <span className="text-white font-medium">{ev.action}</span>
              </div>
            </div>
            <span className="text-[10px] text-mutedCustom font-semibold uppercase">{ev.date}</span>
          </div>
        ))}
      </div>
    </div>
  );
};
export default OperationsTimeline;
