"use client";

import React from "react";
import { Badge } from "../ui/Badge";

interface SystemAlert {
  id: string;
  level: "INFO" | "WARNING" | "ERROR" | "CRITICAL";
  source: string;
  message: string;
  timestamp: string;
}

const mockAlerts: SystemAlert[] = [
  { id: "alt_501", level: "CRITICAL", source: "RISK", message: "Portfolio exposure breaching 48% target constraint.", timestamp: "1 min ago" },
  { id: "alt_502", level: "ERROR", source: "ML", message: "LSTM sequence prediction model output mismatch.", timestamp: "5 mins ago" },
  { id: "alt_503", level: "WARNING", source: "TELEMETRY", message: "Websocket subscription connection jitter spikes.", timestamp: "12 mins ago" },
  { id: "alt_504", level: "INFO", source: "POLYGON", message: "Stock tickers subscription re-aligned.", timestamp: "20 mins ago" }
];

export const TradingOperations: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">System Alert Log Dashboard</h4>
        <span className="text-[10px] text-mutedCustom font-semibold uppercase">Realtime Telemetry</span>
      </div>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Alert ID</th>
              <th className="px-3 py-2.5">Severity Level</th>
              <th className="px-3 py-2.5">Source Module</th>
              <th className="px-3 py-2.5">Log Description</th>
              <th className="px-3 py-2.5 text-right">Age</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {mockAlerts.map((alt) => {
              let badgeVariant: "info" | "warning" | "danger" | "success" = "info";
              if (alt.level === "CRITICAL" || alt.level === "ERROR") badgeVariant = "danger";
              if (alt.level === "WARNING") badgeVariant = "warning";

              return (
                <tr key={alt.id} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                  <td className="px-3 py-2.5 text-white font-mono">{alt.id}</td>
                  <td className="px-3 py-2.5">
                    <Badge variant={badgeVariant}>
                      {alt.level}
                    </Badge>
                  </td>
                  <td className="px-3 py-2.5 text-accentCustom">{alt.source}</td>
                  <td className="px-3 py-2.5 text-white">{alt.message}</td>
                  <td className="px-3 py-2.5 text-right text-mutedCustom font-mono">{alt.timestamp}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default TradingOperations;
