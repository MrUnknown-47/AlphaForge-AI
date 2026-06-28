"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const ExecutionAgent = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Execution Agent fills & latency Metrics</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="flex justify-between border-b border-borderCustom pb-2">
          <span>Average slippage cost:</span>
          <span className="text-white font-mono">1.2 cents/share</span>
        </div>
        <div className="flex justify-between border-b border-borderCustom pb-2">
          <span>Execution Latency:</span>
          <span className="text-white font-mono">42ms</span>
        </div>
        <div className="flex justify-between pb-2">
          <span>Alpaca Broker Bridge Sync:</span>
          <Badge variant="success">CONNECTED</Badge>
        </div>
      </div>
    </div>
  );
};
export default ExecutionAgent;
