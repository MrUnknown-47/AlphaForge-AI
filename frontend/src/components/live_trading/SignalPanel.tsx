"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { ProgressBar } from "../ui/ProgressBar";

export const SignalPanel = ({ ticker }: { ticker: string }) => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Signal Engine Diagnostic: {ticker}</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4">
        <div className="flex justify-between items-center text-xs font-bold">
          <span>CLASSIFICATION DIRECTION:</span>
          <Badge variant="success">BUY / LONG</Badge>
        </div>

        <div className="grid grid-cols-2 gap-4 text-xs font-semibold text-mutedCustom">
          <div className="border-b border-borderCustom pb-2">
            <span>XGBoost Probability:</span>
            <span className="block text-white font-mono mt-1">75.0%</span>
          </div>
          <div className="border-b border-borderCustom pb-2">
            <span>LSTM Probability:</span>
            <span className="block text-white font-mono mt-1">65.0%</span>
          </div>
          <div>
            <span>Ensemble Output:</span>
            <span className="block text-accentCustom font-mono mt-1">72.0%</span>
          </div>
          <div>
            <span>System Regime:</span>
            <span className="block text-white font-mono mt-1">BULL</span>
          </div>
        </div>

        <div className="space-y-1">
          <div className="flex justify-between text-[10px] uppercase font-bold text-mutedCustom">
            <span>Signal Confidence Gauge</span>
            <span className="text-white font-mono">82%</span>
          </div>
          <ProgressBar value={82} />
        </div>
      </div>
    </div>
  );
};
export default SignalPanel;
