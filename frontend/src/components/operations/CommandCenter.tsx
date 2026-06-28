"use client";

import React from "react";
import { MetricCard } from "../ui/MetricCard";

export const CommandCenter = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Global Operations Command Center</h4>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <MetricCard label="System availability Uptime" value="99.99%" />
        <MetricCard label="Average API Latency" value="12ms" />
        <MetricCard label="Database health Status" value="HEALTHY (GREEN)" />
        <MetricCard label="Broker Connection sync" value="CONNECTED (GREEN)" />
      </div>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-xs font-semibold text-mutedCustom bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 uppercase">
        <div>
          <span>API Throughput:</span>
          <span className="block text-white font-mono mt-1">1,452 req/sec</span>
        </div>
        <div>
          <span>Error rate (5xx):</span>
          <span className="block text-successCustom font-mono mt-1">0.00%</span>
        </div>
        <div>
          <span>Active incidents:</span>
          <span className="block text-successCustom font-mono mt-1">0 Active</span>
        </div>
        <div>
          <span>Mean recovery duration:</span>
          <span className="block text-white font-mono mt-1">12 Mins</span>
        </div>
      </div>
    </div>
  );
};
export default CommandCenter;
