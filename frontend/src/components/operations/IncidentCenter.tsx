"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const IncidentCenter = () => {
  const incidents = [
    { date: "June 25", issue: "Database read latency spike resolved", sev: "P2", status: "RESOLVED" },
    { date: "June 12", issue: "Faiss index vectors re-aligned successfully", sev: "P3", status: "RESOLVED" }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Incident Timeline logs</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4">
        {incidents.map((inc, idx) => (
          <div key={idx} className="flex justify-between items-start text-xs border-b border-borderCustom pb-3 last:border-0 last:pb-0">
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <Badge variant="danger">{inc.sev}</Badge>
                <span className="text-white font-medium">{inc.issue}</span>
              </div>
            </div>
            <span className="text-[10px] text-mutedCustom font-semibold uppercase">{inc.date}</span>
          </div>
        ))}
      </div>
    </div>
  );
};
export default IncidentCenter;
