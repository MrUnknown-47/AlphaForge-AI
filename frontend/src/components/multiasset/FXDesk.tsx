"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { Button } from "../ui/Button";

const fxPairs = [
  { pair: "EURUSD", yield: "-1.00%", leverage: "50:1", action: "HEDGE" },
  { pair: "USDJPY", yield: "+5.00%", leverage: "50:1", action: "BUY" },
  { pair: "GBPUSD", yield: "+0.25%", leverage: "50:1", action: "HOLD" }
];

export const FXDesk: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Forex Carry & Cross Currency Hedging</h4>
        <Badge variant="success">FX FEED ACTIVE</Badge>
      </div>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Pair</th>
              <th className="px-3 py-2.5">Carry Yield (Annual)</th>
              <th className="px-3 py-2.5">Max Leverage</th>
              <th className="px-3 py-2.5 text-right">Hedging Override</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {fxPairs.map((fx) => (
              <tr key={fx.pair} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-bold">{fx.pair}</td>
                <td className={`px-3 py-2.5 font-mono ${parseFloat(fx.yield) > 0 ? "text-successCustom" : "text-dangerCustom"}`}>{fx.yield}</td>
                <td className="px-3 py-2.5 text-mutedCustom">{fx.leverage}</td>
                <td className="px-3 py-2.5 text-right">
                  <Badge variant="info">{fx.action}</Badge>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="flex justify-end pt-1">
        <Button variant="primary" size="sm">DEPLOY FX CASH HEDGE</Button>
      </div>
    </div>
  );
};

export default FXDesk;
