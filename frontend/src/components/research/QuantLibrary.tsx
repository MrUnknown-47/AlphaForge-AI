"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const QuantLibrary = () => {
  const assets = [
    { title: "Time-series Momentum Factors", type: "ALPHA FACTOR", sharpe: 1.82 },
    { title: "XGBoost Trend Classification v1", type: "STRATEGY", sharpe: 1.55 }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Quantitative Research Library</h4>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Asset Title</th>
              <th className="px-3 py-2.5">Category</th>
              <th className="px-3 py-2.5">Backtest Sharpe</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {assets.map((row) => (
              <tr key={row.title} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-bold">{row.title}</td>
                <td className="px-3 py-2.5 text-mutedCustom uppercase text-[10px]">
                  <Badge variant="info">{row.type}</Badge>
                </td>
                <td className="px-3 py-2.5 font-mono text-accentCustom">{row.sharpe.toFixed(2)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
export default QuantLibrary;
