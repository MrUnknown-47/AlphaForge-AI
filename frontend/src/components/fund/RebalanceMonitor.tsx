"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { Button } from "../ui/Button";

export const RebalanceMonitor: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Autonomous Rebalance Scheduler</h4>
        <Badge variant="success">IN SYNC</Badge>
      </div>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="flex justify-between items-center pb-2 border-b border-borderCustom border-opacity-40">
          <span>Active Rebalance Frequency:</span>
          <span className="text-white font-mono">DAILY END-OF-DAY</span>
        </div>
        <div className="flex justify-between items-center pb-2 border-b border-borderCustom border-opacity-40">
          <span>Drift Tolerance threshold:</span>
          <span className="text-white font-mono">5.0% weight drift</span>
        </div>
        <div className="flex justify-between items-center">
          <span>Target Rebalance execution:</span>
          <span className="text-accentCustom font-mono">Today 15:45 EST</span>
        </div>
      </div>

      <div className="flex justify-end">
        <Button variant="primary" size="sm">TRIGGER AUTONOMOUS REBALANCE</Button>
      </div>
    </div>
  );
};

export default RebalanceMonitor;
