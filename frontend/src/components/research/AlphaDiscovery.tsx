"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const AlphaDiscovery = () => {
  const factors = [
    { factor: "Transformer Multi-Timeframe Trend", type: "MOMENTUM", sharpe: 2.05, capacity: "$50M" },
    { factor: "VWAP Cross-Regime Mean Reversion", type: "REVERSION", sharpe: 1.65, capacity: "$20M" }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Alpha discovery Engine candidates</h4>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Alpha Factor Candidate</th>
              <th className="px-3 py-2.5">Type</th>
              <th className="px-3 py-2.5">Forecast Sharpe</th>
              <th className="px-3 py-2.5">Capacity Limit</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {factors.map((row) => (
              <tr key={row.factor} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-bold">{row.factor}</td>
                <td className="px-3 py-2.5">
                  <Badge variant="info">{row.type}</Badge>
                </td>
                <td className="px-3 py-2.5 font-mono text-successCustom">{row.sharpe.toFixed(2)}</td>
                <td className="px-3 py-2.5 font-mono text-white">{row.capacity}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
export default AlphaDiscovery;
