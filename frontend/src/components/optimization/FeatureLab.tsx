"use client";

import React from "react";
import { ProgressBar } from "../ui/ProgressBar";
import { Badge } from "../ui/Badge";

export const FeatureLab = () => {
  const features = [
    { name: "EMA crossover (10/200)", shap: 0.24, psi: 0.02, status: "STABLE" },
    { name: "VWAP deviation ratio", shap: 0.18, psi: 0.05, status: "STABLE" },
    { name: "ATR volatility index", shap: 0.12, psi: 0.08, status: "STABLE" },
    { name: "Sentiment index momentum", shap: 0.08, psi: 0.14, status: "DRIFT ALERT" }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Feature Engineering & Drift Monitor</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="flex justify-between items-center text-xs font-bold text-mutedCustom border-b border-borderCustom pb-2 uppercase">
          <span>Feature Symbol</span>
          <div className="flex gap-12 font-mono text-[10px]">
            <span>SHAP Importance</span>
            <span>PSI Index</span>
          </div>
        </div>

        <div className="space-y-3">
          {features.map((f) => (
            <div key={f.name} className="flex justify-between items-center text-xs font-semibold">
              <span className="text-white uppercase">{f.name}</span>
              <div className="flex items-center gap-12 font-mono text-[10px]">
                <span className="text-accentCustom font-bold">+{f.shap.toFixed(2)}</span>
                <span className="text-white">{f.psi.toFixed(2)}</span>
                <Badge variant={f.status === "STABLE" ? "success" : "warning"}>{f.status}</Badge>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
export default FeatureLab;
