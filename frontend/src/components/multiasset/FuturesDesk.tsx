"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { Button } from "../ui/Button";

const contracts = [
  { symbol: "ES_U26", multiplier: 50, maintMargin: "$12,000", rollover: "Sep 18, 2026" },
  { symbol: "NQ_U26", multiplier: 20, maintMargin: "$18,000", rollover: "Sep 18, 2026" },
  { symbol: "CL_V26", multiplier: 1000, maintMargin: "$7,500", rollover: "Oct 21, 2026" }
];

export const FuturesDesk: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Futures Contracts & Rollover Monitor</h4>
        <Badge variant="info">SPAN MARGIN ENFORCED</Badge>
      </div>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Symbol</th>
              <th className="px-3 py-2.5">Multiplier</th>
              <th className="px-3 py-2.5">Maint. Margin</th>
              <th className="px-3 py-2.5 text-right">Expiration Roll</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {contracts.map((c) => (
              <tr key={c.symbol} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-bold">{c.symbol}</td>
                <td className="px-3 py-2.5 text-mutedCustom">{c.multiplier}x</td>
                <td className="px-3 py-2.5 text-accentCustom font-mono">{c.maintMargin}</td>
                <td className="px-3 py-2.5 text-right text-white font-mono">{c.rollover}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="flex justify-end pt-1">
        <Button variant="secondary" size="sm">INITIATE CALENDAR ROLLOVER</Button>
      </div>
    </div>
  );
};

export default FuturesDesk;
