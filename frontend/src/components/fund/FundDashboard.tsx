"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const FundDashboard: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Autonomous Hedge Fund Master Console</h4>
        <Badge variant="success">FUND ACTIVE</Badge>
      </div>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 text-center">
          <span className="text-[10px] text-mutedCustom font-bold uppercase block">Assets Under Management</span>
          <span className="text-xl font-extrabold text-white font-mono mt-1 block">$250,000,000</span>
        </div>
        <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 text-center">
          <span className="text-[10px] text-mutedCustom font-bold uppercase block">Net Asset Value (NAV)</span>
          <span className="text-xl font-extrabold text-accentCustom font-mono mt-1 block">$105.42</span>
        </div>
        <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 text-center">
          <span className="text-[10px] text-mutedCustom font-bold uppercase block">Fund Target Leverage</span>
          <span className="text-xl font-extrabold text-white font-mono mt-1 block">1.35x</span>
        </div>
        <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 text-center">
          <span className="text-[10px] text-mutedCustom font-bold uppercase block">Hurdle Rate / Carry Fee</span>
          <span className="text-xl font-extrabold text-white font-mono mt-1 block">5.0% / 20%</span>
        </div>
      </div>
    </div>
  );
};

export default FundDashboard;
