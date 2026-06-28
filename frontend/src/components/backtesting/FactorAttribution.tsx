"use client";

import React from "react";

export const FactorAttribution = () => {
  const factors = [
    { name: "Market Beta", beta: 0.88, alpha: 1.25, risk: 2.14 },
    { name: "Momentum Factor", beta: 1.12, alpha: 3.42, risk: 4.12 },
    { name: "Value Bias", beta: -0.15, alpha: 0.15, risk: 0.85 },
    { name: "ML Signal Attribution", beta: 0.42, alpha: 2.04, risk: 0.25 }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Strategy Factor Attribution (Brinson attribution model)</h4>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Factor Exposure</th>
              <th className="px-3 py-2.5">Factor Loading (Beta)</th>
              <th className="px-3 py-2.5">Active Alpha contribution</th>
              <th className="px-3 py-2.5">Risk Contribution</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {factors.map((fact) => (
              <tr key={fact.name} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-bold">{fact.name}</td>
                <td className="px-3 py-2.5 font-mono text-white">{fact.beta.toFixed(2)}</td>
                <td className="px-3 py-2.5 font-mono text-successCustom">+{fact.alpha.toFixed(2)}%</td>
                <td className="px-3 py-2.5 font-mono text-warningCustom">{fact.risk.toFixed(2)}%</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
export default FactorAttribution;
