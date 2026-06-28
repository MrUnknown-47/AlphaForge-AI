"use client";

import React from "react";
import { Badge } from "../ui/Badge";

interface Alerts {
  severity: "P0" | "P1" | "P2";
  module: string;
  message: string;
  timestamp: string;
}

const mockAlerts: Alerts[] = [
  { severity: "P2", module: "DRIFT", message: "Prediction probabilities minor variance spike", timestamp: "5 mins ago" },
  { severity: "P1", module: "RISK", message: "Leverage usage matching warnings trigger: 1.2x", timestamp: "12 mins ago" }
];

export const AlertsPanel = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Live System Operations Alerts</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4">
        {mockAlerts.map((alert, idx) => (
          <div key={idx} className="flex justify-between items-start text-xs border-b border-borderCustom pb-3 last:border-0 last:pb-0">
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <Badge variant={alert.severity === "P0" ? "danger" : alert.severity === "P1" ? "warning" : "info"}>
                  {alert.severity}
                </Badge>
                <span className="text-white font-bold">{alert.module}</span>
              </div>
              <p className="text-[10px] text-mutedCustom font-medium mt-0.5">{alert.message}</p>
            </div>
            <span className="text-[10px] text-mutedCustom font-semibold uppercase">{alert.timestamp}</span>
          </div>
        ))}
      </div>
    </div>
  );
};
export default AlertsPanel;
