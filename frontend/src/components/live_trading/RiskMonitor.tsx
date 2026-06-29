"use client";

import React from "react";
import { useTradingStore } from "../../store/tradingStore";
import { ProgressBar } from "../ui/ProgressBar";
import { Button } from "../ui/Button";
import { Badge } from "../ui/Badge";

export const RiskMonitor: React.FC = () => {
  const { risk, toggleKillSwitch, flattenPositions } = useTradingStore();

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Risk Controls & Limits</h4>
        <Badge variant={risk.kill_switch_active ? "danger" : "success"}>
          {risk.kill_switch_active ? "HALTED" : "ONLINE"}
        </Badge>
      </div>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="grid grid-cols-2 gap-4">
          <div className="border-b border-borderCustom pb-2">
            <span className="text-[10px] uppercase block tracking-wider">Max Position Exposure</span>
            <span className="block text-white font-mono mt-1">{risk.max_position_exposure}%</span>
            <ProgressBar value={risk.max_position_exposure * 2} className="mt-1" />
          </div>
          <div className="border-b border-borderCustom pb-2">
            <span className="text-[10px] uppercase block tracking-wider">Current Exposure</span>
            <span className="block text-white font-mono mt-1">{risk.current_exposure}%</span>
            <ProgressBar value={risk.current_exposure * 2} className="mt-1" />
          </div>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div>
            <span className="text-[10px] uppercase block tracking-wider">Daily Drawdown</span>
            <span className="block text-white font-mono mt-1">{risk.daily_drawdown}%</span>
            <ProgressBar value={risk.daily_drawdown * 33} className="mt-1" />
          </div>
          <div>
            <span className="text-[10px] uppercase block tracking-wider">Kill Switch Status</span>
            <span className={`block font-mono mt-1 ${risk.kill_switch_active ? "text-dangerCustom" : "text-successCustom"}`}>
              {risk.kill_switch_active ? "ACTIVE" : "INACTIVE"}
            </span>
          </div>
        </div>

        {/* Emergency Trigger buttons */}
        <div className="grid grid-cols-2 gap-2 pt-2">
          <Button
            variant="danger"
            size="sm"
            onClick={() => toggleKillSwitch(!risk.kill_switch_active)}
            className="w-full text-[10px] uppercase font-bold"
          >
            {risk.kill_switch_active ? "Deactivate Kill Switch" : "Emergency Kill Switch"}
          </Button>
          <Button
            variant="secondary"
            size="sm"
            onClick={flattenPositions}
            className="w-full text-[10px] uppercase font-bold"
          >
            Emergency Flatten
          </Button>
        </div>
      </div>
    </div>
  );
};

export default RiskMonitor;
