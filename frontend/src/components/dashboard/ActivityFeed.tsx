"use client";

import React from "react";
import { Badge } from "../ui/Badge";

interface Activity {
  type: "TRADE" | "ALERT" | "RISK" | "AI";
  message: string;
  timestamp: string;
}

const mockActivity: Activity[] = [
  { type: "TRADE", message: "BUY 100 shares AAPL @ $182.50", timestamp: "10 mins ago" },
  { type: "ALERT", message: "System health check complete: All services green", timestamp: "30 mins ago" },
  { type: "RISK", message: "Drawdown check passed: 1.05% < 20% limit", timestamp: "1 hour ago" },
  { type: "AI", message: "Copilot generated daily regime classification: BULL", timestamp: "2 hours ago" }
];

export const ActivityFeed = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Execution & Audit Activity</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4">
        {mockActivity.map((act, idx) => (
          <div key={idx} className="flex justify-between items-start text-xs border-b border-borderCustom pb-3 last:border-0 last:pb-0">
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <Badge variant={act.type === "TRADE" ? "success" : act.type === "RISK" ? "danger" : "info"}>
                  {act.type}
                </Badge>
                <span className="text-white font-medium">{act.message}</span>
              </div>
            </div>
            <span className="text-[10px] text-mutedCustom font-semibold uppercase">{act.timestamp}</span>
          </div>
        ))}
      </div>
    </div>
  );
};
export default ActivityFeed;
