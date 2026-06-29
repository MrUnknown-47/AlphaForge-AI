"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { Button } from "../ui/Button";

const perps = [
  { symbol: "BTC-PERP", fundingRate: "0.0120%", openInterest: "$420M", liqPrice: "$61,420" },
  { symbol: "ETH-PERP", fundingRate: "0.0150%", openInterest: "$180M", liqPrice: "$3,110" },
  { symbol: "SOL-PERP", fundingRate: "0.0220%", openInterest: "$85M", liqPrice: "$124" }
];

export const CryptoDesk: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Crypto Spot & Perpetual Contracts</h4>
        <Badge variant="info">LIQUIDATION SAFETY AUTO</Badge>
      </div>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Symbol</th>
              <th className="px-3 py-2.5">8h Funding Rate</th>
              <th className="px-3 py-2.5">Open Interest</th>
              <th className="px-3 py-2.5 text-right">Est. Liq Price</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {perps.map((p) => (
              <tr key={p.symbol} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-bold">{p.symbol}</td>
                <td className="px-3 py-2.5 text-successCustom font-mono">{p.fundingRate}</td>
                <td className="px-3 py-2.5 text-mutedCustom">{p.openInterest}</td>
                <td className="px-3 py-2.5 text-right text-dangerCustom font-mono">{p.liqPrice}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="flex justify-end pt-1">
        <Button variant="primary" size="sm">REBALANCE COIN WEIGHTS</Button>
      </div>
    </div>
  );
};

export default CryptoDesk;
