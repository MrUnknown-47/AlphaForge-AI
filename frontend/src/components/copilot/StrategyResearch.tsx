"use client";

import React from "react";

export const StrategyResearch = () => {
  const ideas = [
    { name: "Temporal Transformer Multi-Timeframe", sharpe: 2.05, cagr: 22.4, drawdown: 2.85 },
    { name: "Mean-Reversion Volatility Filtered", sharpe: 1.65, cagr: 14.5, drawdown: 3.50 }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Strategy Sandbox Candidates</h4>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Strategy Name</th>
              <th className="px-3 py-2.5">Expected Sharpe</th>
              <th className="px-3 py-2.5">Expected CAGR %</th>
              <th className="px-3 py-2.5">Max Drawdown</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {ideas.map((row) => (
              <tr key={row.name} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-bold">{row.name}</td>
                <td className="px-3 py-2.5 font-mono text-accentCustom">{row.sharpe.toFixed(2)}</td>
                <td className="px-3 py-2.5 font-mono text-successCustom">+{row.cagr}%</td>
                <td className="px-3 py-2.5 font-mono text-dangerCustom">-{row.drawdown}%</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
export default StrategyResearch;
