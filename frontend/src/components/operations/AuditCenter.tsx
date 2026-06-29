"use client";

import React from "react";
import { Badge } from "../ui/Badge";

interface EventStreamLog {
  id: string;
  type: "BROKER_DISCONNECT" | "FEED_STALE" | "RISK_BREACH" | "KILL_SWITCH";
  message: string;
  timestamp: string;
}

const mockEvents: EventStreamLog[] = [
  { id: "evt_701", type: "RISK_BREACH", message: "Portfolio exposure breaching 48% target constraint limit.", timestamp: "10:14:02" },
  { id: "evt_702", type: "KILL_SWITCH", message: "Emergency system Kill Switch deactivated by root operator.", timestamp: "10:12:05" },
  { id: "evt_703", type: "FEED_STALE", message: "Polygon sub-feed AAPL quote latency exceeding 120ms threshold.", timestamp: "09:58:32" },
  { id: "evt_704", type: "BROKER_DISCONNECT", message: "Connection lost with Alpaca Broker API gateway. Reconnecting...", timestamp: "09:42:15" }
];

export const AuditCenter: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Operations Live Event Stream</h4>
        <span className="text-[10px] text-mutedCustom font-semibold uppercase">Realtime websocket logs</span>
      </div>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 font-mono text-[11px] text-mutedCustom max-h-64 overflow-y-auto">
        {mockEvents.map((log) => {
          let badgeVariant: "info" | "warning" | "danger" | "success" = "info";
          if (log.type === "BROKER_DISCONNECT" || log.type === "KILL_SWITCH") badgeVariant = "danger";
          if (log.type === "FEED_STALE") badgeVariant = "warning";
          if (log.type === "RISK_BREACH") badgeVariant = "danger";

          return (
            <div key={log.id} className="flex justify-between items-start border-b border-borderCustom border-opacity-40 pb-3 last:border-0 last:pb-0">
              <div className="space-y-1">
                <div className="flex items-center gap-2">
                  <Badge variant={badgeVariant}>{log.type}</Badge>
                  <span className="text-white font-medium">{log.message}</span>
                </div>
              </div>
              <span className="text-[10px] text-mutedCustom font-semibold">{log.timestamp}</span>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default AuditCenter;
