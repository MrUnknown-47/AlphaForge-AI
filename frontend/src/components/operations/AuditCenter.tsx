"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const AuditCenter = () => {
  const logs = [
    { time: "14:24:02", action: "Live shadow validation PM weights updated", type: "SYSTEM" },
    { time: "12:12:05", action: "User JWT auth token re-verified successfully", type: "SECURITY" }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Chronological System Audit Trail</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 font-mono text-[11px] text-mutedCustom">
        {logs.map((log, idx) => (
          <div key={idx} className="flex justify-between items-start border-b border-borderCustom pb-3 last:border-0 last:pb-0">
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <Badge variant="info">{log.type}</Badge>
                <span className="text-white font-medium">{log.action}</span>
              </div>
            </div>
            <span className="text-[10px] text-mutedCustom font-semibold">{log.time}</span>
          </div>
        ))}
      </div>
    </div>
  );
};
export default AuditCenter;
