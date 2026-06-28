"use client";

import React from "react";

export const FundOperations = () => {
  const monitors = [
    { name: "Alpaca Paper Bridge Latency", status: "45ms (GREEN)" },
    { name: "Database Replication sync", status: "CONNECTED (GREEN)" },
    { name: "Execution Engine status", status: "LISTENING (GREEN)" },
    { name: "RAG vector indices host", status: "STABLE (GREEN)" }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Fund execution & Operations Monitors</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-3">
        {monitors.map((m) => (
          <div key={m.name} className="flex justify-between items-center text-xs font-semibold">
            <span className="text-mutedCustom uppercase">{m.name}</span>
            <div className="flex items-center gap-1.5">
              <span className="w-2 h-2 rounded-full bg-successCustom" />
              <span className="text-successCustom text-[10px] uppercase font-bold">{m.status}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
export default FundOperations;
