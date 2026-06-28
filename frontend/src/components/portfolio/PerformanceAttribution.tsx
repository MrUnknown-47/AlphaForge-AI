"use client";

import React from "react";

export const PerformanceAttribution = () => {
  const attributions = [
    { factor: "Market Momentum", return: 4.85, alpha: 1.25, risk: 2.14 },
    { factor: "Size Bias (SMID)", return: 1.12, alpha: 0.15, risk: 0.85 },
    { factor: "Tech Sector Rotation", return: 6.84, alpha: 3.42, risk: 4.12 },
    { factor: "Model Alpha (XGB/LSTM)", return: 2.04, alpha: 2.04, risk: 0.25 }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Performance Factor Attribution (Brinson Model)</h4>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Attribution Factor</th>
              <th className="px-3 py-2.5">Total Return</th>
              <th className="px-3 py-2.5">Active Alpha</th>
              <th className="px-3 py-2.5">Active Risk Contribution</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {attributions.map((attr) => (
              <tr key={attr.factor} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-bold">{attr.factor}</td>
                <td className="px-3 py-2.5 font-mono text-successCustom">+{attr.return.toFixed(2)}%</td>
                <td className="px-3 py-2.5 font-mono text-accentCustom">+{attr.alpha.toFixed(2)}%</td>
                <td className="px-3 py-2.5 font-mono text-warningCustom">{attr.risk.toFixed(2)}%</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
export default PerformanceAttribution;
