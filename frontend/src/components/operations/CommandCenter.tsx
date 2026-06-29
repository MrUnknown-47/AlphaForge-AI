"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const CommandCenter: React.FC = () => {
  const services = [
    { name: "PostgreSQL Database", status: "ONLINE", type: "success" },
    { name: "Redis Cache Engine", status: "ONLINE", type: "success" },
    { name: "Alpaca Broker Bridge", status: "ONLINE", type: "success" },
    { name: "Polygon Market Feeds", status: "ONLINE", type: "success" },
    { name: "ML Forecasting Worker", status: "DEGRADED", type: "warning" },
    { name: "AI Agent Orchestrator", status: "ONLINE", type: "success" },
    { name: "Risk Management Engine", status: "ONLINE", type: "success" }
  ];

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">NOC Service Status Panel</h4>
        <span className="text-[10px] text-mutedCustom font-semibold uppercase">Realtime Health Checks</span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
        {services.map((svc) => (
          <div key={svc.name} className="flex justify-between items-center p-2.5 bg-cardBg border border-borderCustom rounded text-xs font-semibold">
            <span className="text-white">{svc.name}</span>
            <Badge variant={svc.type as any}>{svc.status}</Badge>
          </div>
        ))}
      </div>
    </div>
  );
};

export default CommandCenter;
