"use client";

import React from "react";
import { useTradingStore } from "../../store/tradingStore";
import { Badge } from "../ui/Badge";

export const AlertsPanel: React.FC = () => {
  const { events } = useTradingStore();

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Event Stream Panel</h4>
        <span className="text-[10px] text-mutedCustom font-semibold uppercase">Realtime WebSockets</span>
      </div>

      {events.length === 0 ? (
        <div className="py-8 text-center text-xs text-mutedCustom border border-dashed border-borderCustom rounded">
          No real-time events received yet. Listening on live trading ws streams...
        </div>
      ) : (
        <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 max-h-64 overflow-y-auto">
          {events.map((evt) => {
            let badgeVariant: "info" | "warning" | "danger" | "success" = "info";
            if (evt.event_type === "RISK_WARNING") badgeVariant = "warning";
            if (evt.event_type === "BROKER_DISCONNECT") badgeVariant = "danger";
            if (evt.event_type === "FILL_COMPLETED") badgeVariant = "success";

            return (
              <div key={evt.id} className="flex justify-between items-start text-xs border-b border-borderCustom pb-3 last:border-0 last:pb-0">
                <div className="space-y-1">
                  <div className="flex items-center gap-2">
                    <Badge variant={badgeVariant}>
                      {evt.event_type}
                    </Badge>
                  </div>
                  <p className="text-[10px] text-white mt-1 font-medium">{evt.message}</p>
                </div>
                <span className="text-[9px] text-mutedCustom font-mono uppercase">
                  {new Date(evt.timestamp).toLocaleTimeString()}
                </span>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};

export default AlertsPanel;
