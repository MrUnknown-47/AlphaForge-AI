"use client";

import React from "react";

export const OperationsPanel = () => {
  const services = [
    { name: "Alpaca Paper API", status: "GREEN" },
    { name: "Polygon WebSocket", status: "GREEN" },
    { name: "SQLite Primary DB", status: "GREEN" },
    { name: "Redis Memory Cache", status: "GREEN" },
    { name: "Copilot LLM API", status: "GREEN" },
    { name: "Signal Scheduler", status: "GREEN" }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">System Operations Health</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-3">
        {services.map((srv) => (
          <div key={srv.name} className="flex justify-between items-center text-xs font-semibold">
            <span className="text-mutedCustom uppercase">{srv.name}</span>
            <div className="flex items-center gap-1.5">
              <span className="w-2 h-2 rounded-full bg-successCustom" />
              <span className="text-successCustom text-[10px] uppercase font-bold">{srv.status}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
export default OperationsPanel;
