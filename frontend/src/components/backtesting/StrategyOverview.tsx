"use client";

import React from "react";

export const StrategyOverview = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Strategy Details Overview</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-3 text-xs font-semibold text-mutedCustom">
        <div className="flex justify-between border-b border-borderCustom pb-2">
          <span>Strategy Name:</span>
          <span className="text-white">AlphaForge Ensemble v1</span>
        </div>
        <div className="flex justify-between border-b border-borderCustom pb-2">
          <span>Software Release:</span>
          <span className="text-accentCustom">v1.0.4-LTS</span>
        </div>
        <div className="flex justify-between border-b border-borderCustom pb-2">
          <span>Total Executed Signals:</span>
          <span className="text-white">1,452 Signals</span>
        </div>
        <div className="flex justify-between border-b border-borderCustom pb-2">
          <span>Holding Period Average:</span>
          <span className="text-white">1.8 Days</span>
        </div>
        <div className="flex justify-between">
          <span>Annual Portfolio Turnover:</span>
          <span className="text-white">12.4x</span>
        </div>
      </div>
    </div>
  );
};
export default StrategyOverview;
