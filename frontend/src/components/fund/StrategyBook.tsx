"use client";

import React from "react";
import { Badge } from "../ui/Badge";

const strategies = [
  { symbol: "MOMENTUM", name: "Cross-Sectional Momentum", capacity: "$50M", sharpe: 1.85 },
  { symbol: "MEAN_REVERSION", name: "Stat-Arb Mean Reversion", capacity: "$25M", sharpe: 2.45 },
  { symbol: "TREND_FOLLOWING", name: "CTA Trend Follower", capacity: "$100M", sharpe: 1.15 },
  { symbol: "FACTOR_INVESTING", name: "Multi-Factor Quality/Value/Growth", capacity: "$200M", sharpe: 1.45 },
  { symbol: "MACRO", name: "Global Macro Rate Cycles", capacity: "$500M", sharpe: 1.25 }
];

export const StrategyBook: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Fund Active Strategy Registry Book</h4>
        <span className="text-[10px] text-mutedCustom font-semibold uppercase">5 Strategies Registered</span>
      </div>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Strategy Code</th>
              <th className="px-3 py-2.5">Description</th>
              <th className="px-3 py-2.5">Capacity Cap</th>
              <th className="px-3 py-2.5 text-right">Target Sharpe</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {strategies.map((s) => (
              <tr key={s.symbol} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-bold">{s.symbol}</td>
                <td className="px-3 py-2.5 text-mutedCustom">{s.name}</td>
                <td className="px-3 py-2.5 text-white font-mono">{s.capacity}</td>
                <td className="px-3 py-2.5 text-right font-mono text-accentCustom">{s.sharpe.toFixed(2)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default StrategyBook;
