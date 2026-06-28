"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const InstitutionalScorecard = () => {
  const requirements = [
    { target: "System Audits Configured", current: "YES", status: "PASS" },
    { target: "RBAC Policies Active", current: "YES", status: "PASS" },
    { target: "Slippage Monitoring Active", current: "YES", status: "PASS" }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Institutional scorecards requirements</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
        <div className="flex justify-between items-center text-xs font-bold text-mutedCustom border-b border-borderCustom pb-2 uppercase">
          <span>Readiness Checklist</span>
          <div className="flex gap-12 font-mono text-[10px]">
            <span>Current</span>
            <span>Status</span>
          </div>
        </div>

        <div className="space-y-3">
          {requirements.map((row) => (
            <div key={row.target} className="flex justify-between items-center">
              <span className="text-white uppercase">{row.target}</span>
              <div className="flex items-center gap-12 font-mono text-[10px]">
                <span className="text-accentCustom font-bold">{row.current}</span>
                <Badge variant="success">{row.status}</Badge>
              </div>
            </div>
          ))}
        </div>

        <div className="border-t border-borderCustom pt-3 flex justify-between items-center uppercase">
          <span className="text-mutedCustom text-[10px]">Overall compliance:</span>
          <Badge variant="success">INSTITUTIONAL READY</Badge>
        </div>
      </div>
    </div>
  );
};
export default InstitutionalScorecard;
