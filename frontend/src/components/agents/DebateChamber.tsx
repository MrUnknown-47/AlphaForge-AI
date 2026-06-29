"use client";

import React from "react";

export const DebateChamber: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">AI Debate Board</h4>
        <span className="text-[10px] text-mutedCustom font-semibold uppercase">Realtime Multi-Agent Debate</span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {/* Bull Thesis */}
        <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-2 text-xs font-semibold">
          <span className="text-successCustom uppercase font-bold text-[10px] tracking-wider">● Bull Thesis</span>
          <p className="text-white leading-relaxed font-normal">
            Macro liquidity expansion and index sector rotations strongly support momentum in high-beta tech holdings. Realized alpha targets 15.4% annualized.
          </p>
        </div>

        {/* Bear Thesis */}
        <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-2 text-xs font-semibold">
          <span className="text-dangerCustom uppercase font-bold text-[10px] tracking-wider">● Bear Thesis</span>
          <p className="text-white leading-relaxed font-normal">
            Yield curves remain inverted, indicating contractionary pressures. Consumer confidence indices showing minor divergence from price momentum.
          </p>
        </div>

        {/* Risk Thesis */}
        <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-2 text-xs font-semibold">
          <span className="text-warningCustom uppercase font-bold text-[10px] tracking-wider">● Risk Thesis</span>
          <p className="text-white leading-relaxed font-normal">
            Daily drawdown risk profile requires hedging targets. Leverage should be capped at 1.2x until volatility index retreats under 14.5.
          </p>
        </div>

        {/* Execution Thesis */}
        <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-2 text-xs font-semibold">
          <span className="text-accentCustom uppercase font-bold text-[10px] tracking-wider">● Execution Thesis</span>
          <p className="text-white leading-relaxed font-normal">
            Orders should be routed using dynamic VWAP execution to avoid market impact. Current average slippage index remains under 1.2 bps.
          </p>
        </div>
      </div>
    </div>
  );
};

export default DebateChamber;
