"use client";

import React from "react";
import { Badge } from "../ui/Badge";

interface Log {
  type: "REBALANCE" | "TRADE" | "RISK" | "ALERT";
  msg: string;
  time: string;
}

const logs: Log[] = [
  { type: "REBALANCE", msg: "Rebalanced Apple/Nvidia target weights", time: "10 mins ago" },
  { type: "TRADE", msg: "BUY 100 shares AAPL @ $182.50", time: "25 mins ago" },
  { type: "RISK", msg: "Drawdown verified: 1.05% matches limits", time: "1 hour ago" },
  { type: "ALERT", msg: "Daily covariance updates calculated successfully", time: "4 hours ago" }
];

export const PortfolioActivity = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Rebalancing & Risk Activity</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4">
        {logs.map((log, idx) => (
          <div key={idx} className="flex justify-between items-start text-xs border-b border-borderCustom pb-3 last:border-0 last:pb-0">
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <Badge variant={log.type === "REBALANCE" ? "info" : log.type === "TRADE" ? "success" : "danger"}>
                  {log.type}
                </Badge>
                <span className="text-white font-medium">{log.msg}</span>
              </div>
            </div>
            <span className="text-[10px] text-mutedCustom font-semibold uppercase">{log.time}</span>
          </div>
        ))}
      </div>
    </div>
  );
};
export default PortfolioActivity;
