"use client";

import React from "react";

interface PMRecord {
  name: string;
  sharpe: number;
  cagr: number;
  hit: number;
  drawdown: number;
  capacity: string;
}

const pmRecords: PMRecord[] = [
  { name: "Quant Alpha Model Agent", sharpe: 2.05, cagr: 22.4, hit: 65.4, drawdown: 2.85, capacity: "$50M" },
  { name: "Portfolio Optimizer Agent", sharpe: 1.85, cagr: 18.5, hit: 62.4, drawdown: 3.12, capacity: "$100M" }
];

export const PMScorecard = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Sub-Agent Portfolio Manager Scorecard</h4>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Sub-Agent Manager</th>
              <th className="px-3 py-2.5">Sharpe</th>
              <th className="px-3 py-2.5">CAGR %</th>
              <th className="px-3 py-2.5">Hit Ratio</th>
              <th className="px-3 py-2.5">Max Drawdown</th>
              <th className="px-3 py-2.5">Capacity Limit</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {pmRecords.map((row) => (
              <tr key={row.name} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-bold">{row.name}</td>
                <td className="px-3 py-2.5 font-mono text-accentCustom">{row.sharpe.toFixed(2)}</td>
                <td className="px-3 py-2.5 font-mono text-successCustom">+{row.cagr}%</td>
                <td className="px-3 py-2.5 font-mono text-white">{row.hit}%</td>
                <td className="px-3 py-2.5 font-mono text-dangerCustom">-{row.drawdown}%</td>
                <td className="px-3 py-2.5 font-mono text-white">{row.capacity}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
export default PMScorecard;
