"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const InstitutionalScorecard = () => {
  const gates = [
    { metric: "Sharpe Index Target (> 1.50)", current: "1.85", status: "PASS" },
    { metric: "Max Drawdown Cap (< 20%)", current: "3.12%", status: "PASS" },
    { metric: "AUM Capacity threshold (> $10M)", current: "$50.0M", status: "PASS" },
    { metric: "Drift Stability Index", current: "0.08", status: "PASS" }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Institutional Readiness Scorecard</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
        <div className="flex justify-between items-center text-xs font-bold text-mutedCustom border-b border-borderCustom pb-2 uppercase">
          <span>Readiness metric</span>
          <div className="flex gap-12 font-mono text-[10px]">
            <span>Current</span>
            <span>Status</span>
          </div>
        </div>

        <div className="space-y-3">
          {gates.map((row) => (
            <div key={row.metric} className="flex justify-between items-center">
              <span className="text-white uppercase">{row.metric}</span>
              <div className="flex items-center gap-12 font-mono text-[10px]">
                <span className="text-accentCustom font-bold">{row.current}</span>
                <Badge variant="success">{row.status}</Badge>
              </div>
            </div>
          ))}
        </div>

        <div className="border-t border-borderCustom pt-3 flex justify-between items-center uppercase">
          <span className="text-mutedCustom text-[10px]">Overall Readiness Rating:</span>
          <Badge variant="success">INSTITUTIONAL GRADE</Badge>
        </div>
      </div>
    </div>
  );
};
export default InstitutionalScorecard;
