"use client";

import React from "react";

export const PerformanceAttribution: React.FC = () => {
  const attributions = [
    { source: "Tech Sector Attribution", return: 4.85, alpha: 1.25, transaction_cost: 0.12 },
    { source: "Automotive Sector Attribution", return: 1.12, alpha: 0.15, transaction_cost: 0.05 },
    { source: "AAPL Asset Allocation", return: 2.14, alpha: 0.95, transaction_cost: 0.04 },
    { source: "NVDA Asset Allocation", return: 5.60, alpha: 3.12, transaction_cost: 0.08 },
    { source: "Execution Slippage Cost", return: -0.32, alpha: -0.32, transaction_cost: 0.15 },
    { source: "Broker Fees & Commissions", return: -0.15, alpha: -0.15, transaction_cost: 0.15 }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Performance Attribution (Sector, Asset & Costs)</h4>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Attribution Source</th>
              <th className="px-3 py-2.5">Total Return Contribution</th>
              <th className="px-3 py-2.5">Active Alpha Contribution</th>
              <th className="px-3 py-2.5">Fees & Slippage Drag</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {attributions.map((attr) => (
              <tr key={attr.source} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-bold">{attr.source}</td>
                <td className={`px-3 py-2.5 font-mono ${attr.return >= 0 ? "text-successCustom" : "text-dangerCustom"}`}>
                  {attr.return >= 0 ? "+" : ""}{attr.return.toFixed(2)}%
                </td>
                <td className={`px-3 py-2.5 font-mono ${attr.alpha >= 0 ? "text-accentCustom" : "text-dangerCustom"}`}>
                  {attr.alpha >= 0 ? "+" : ""}{attr.alpha.toFixed(2)}%
                </td>
                <td className="px-3 py-2.5 font-mono text-warningCustom">
                  {attr.transaction_cost > 0 ? `-${attr.transaction_cost.toFixed(2)}%` : "0.00%"}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default PerformanceAttribution;
