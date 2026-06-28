"use client";

import React from "react";

export const TradeAnalysis = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Historical Trade Breakdown Analytics</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div className="border-b border-borderCustom pb-2">
            <span>Total Executions:</span>
            <span className="block text-white font-mono mt-1">1,452 Trades</span>
          </div>
          <div className="border-b border-borderCustom pb-2">
            <span>Long/Short Ratio:</span>
            <span className="block text-white font-mono mt-1">72% / 28%</span>
          </div>
          <div className="border-b border-borderCustom pb-2">
            <span>Average Win size:</span>
            <span className="block text-successCustom font-mono mt-1">+$420.50</span>
          </div>
          <div className="border-b border-borderCustom pb-2">
            <span>Average Loss size:</span>
            <span className="block text-dangerCustom font-mono mt-1">-$210.30</span>
          </div>
        </div>

        <div className="grid grid-cols-3 gap-4 uppercase font-bold text-[10px]">
          <div>
            <span>Largest Win</span>
            <span className="block text-successCustom font-mono mt-0.5">+$5,820.00</span>
          </div>
          <div>
            <span>Largest Loss</span>
            <span className="block text-dangerCustom font-mono mt-0.5">-$2,140.00</span>
          </div>
          <div>
            <span>Mathematical Expectancy</span>
            <span className="block text-accentCustom font-mono mt-0.5">+$182.40</span>
          </div>
        </div>
      </div>
    </div>
  );
};
export default TradeAnalysis;
