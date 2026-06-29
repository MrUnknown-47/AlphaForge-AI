"use client";

import React from "react";
import { useTradingStore } from "../../store/tradingStore";
import { ProgressBar } from "../ui/ProgressBar";
import { Badge } from "../ui/Badge";

export const BrokerPanel: React.FC = () => {
  const { telemetry } = useTradingStore();

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Execution Quality Panel</h4>
        <span className="text-[10px] text-mutedCustom font-semibold uppercase">Performance Metrics</span>
      </div>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="grid grid-cols-2 gap-4">
          <div className="border-b border-borderCustom pb-2">
            <span className="text-[10px] uppercase block tracking-wider">Average Slippage</span>
            <span className="block text-white font-mono mt-1">{telemetry.average_slippage_bps} bps</span>
          </div>
          <div className="border-b border-borderCustom pb-2">
            <span className="text-[10px] uppercase block tracking-wider">Fill Ratio</span>
            <span className="block text-successCustom font-mono mt-1">{(telemetry.fill_ratio * 100).toFixed(1)}%</span>
          </div>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div className="border-b border-borderCustom pb-2">
            <span className="text-[10px] uppercase block tracking-wider">Avg Latency</span>
            <span className="block text-accentCustom font-mono mt-1">{telemetry.average_latency_ms} ms</span>
          </div>
          <div className="border-b border-borderCustom pb-2">
            <span className="text-[10px] uppercase block tracking-wider">Implementation Shortfall</span>
            <span className="block text-white font-mono mt-1">{telemetry.implementation_shortfall_bps} bps</span>
          </div>
        </div>

        <div>
          <span className="text-[10px] uppercase block tracking-wider">VWAP Deviation</span>
          <span className="block text-warningCustom font-mono mt-1">{telemetry.vwap_deviation_bps} bps</span>
        </div>
      </div>
    </div>
  );
};

export default BrokerPanel;
