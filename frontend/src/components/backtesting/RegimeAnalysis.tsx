"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const RegimeAnalysis = () => {
  const regimes = [
    { regime: "Bullish Expansion", return: "+24.5%", drawdown: "-1.05%", sharpe: 2.14 },
    { regime: "Bearish Contraction", return: "-2.12%", drawdown: "-3.12%", sharpe: 0.85 },
    { regime: "High Volatility Spikes", return: "+12.80%", drawdown: "-2.85%", sharpe: 1.45 },
    { regime: "Low Volatility Sideways", return: "+4.12%", drawdown: "-0.50%", sharpe: 1.12 }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Regime Performance Diagnostics Matrix</h4>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Volatility Regime</th>
              <th className="px-3 py-2.5">Total Return</th>
              <th className="px-3 py-2.5">Max Drawdown</th>
              <th className="px-3 py-2.5">Sharpe Ratio</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {regimes.map((row) => (
              <tr key={row.regime} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-bold">{row.regime}</td>
                <td className="px-3 py-2.5 font-mono text-successCustom">{row.return}</td>
                <td className="px-3 py-2.5 font-mono text-dangerCustom">{row.drawdown}</td>
                <td className="px-3 py-2.5 font-mono text-accentCustom">{row.sharpe.toFixed(2)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
export default RegimeAnalysis;
