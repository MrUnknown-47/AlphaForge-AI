"use client";

import React from "react";
import { ProgressBar } from "../ui/ProgressBar";
import { Badge } from "../ui/Badge";

export const InfrastructureMonitor: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">System Telemetry Monitor</h4>
        <Badge variant="success">WEBSOCKET ONLINE</Badge>
      </div>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="space-y-1.5">
          <div className="flex justify-between uppercase text-[10px] font-bold">
            <span>CPU Core Utilization</span>
            <span className="text-white font-mono">24.5%</span>
          </div>
          <ProgressBar value={25} />
        </div>

        <div className="space-y-1.5 border-t border-borderCustom pt-3">
          <div className="flex justify-between uppercase text-[10px] font-bold">
            <span>Memory Consumption</span>
            <span className="text-white font-mono">42.1%</span>
          </div>
          <ProgressBar value={42} />
        </div>

        <div className="space-y-1.5 border-t border-borderCustom pt-3">
          <div className="flex justify-between uppercase text-[10px] font-bold">
            <span>Disk Space Usage</span>
            <span className="text-white font-mono">68.4%</span>
          </div>
          <ProgressBar value={68} />
        </div>

        <div className="grid grid-cols-2 gap-4 border-t border-borderCustom pt-3">
          <div>
            <span className="text-[10px] uppercase block tracking-wider">Average Latency</span>
            <span className="block text-accentCustom font-mono mt-1">12 ms</span>
          </div>
          <div>
            <span className="text-[10px] uppercase block tracking-wider">Websocket Status</span>
            <span className="block text-successCustom font-mono mt-1">CONNECTED</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default InfrastructureMonitor;
