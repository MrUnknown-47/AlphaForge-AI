"use client";

import React from "react";
import { Badge } from "../ui/Badge";

const assets = [
  { symbol: "AAPL", type: "EQUITY", exchange: "NASDAQ", margin: "50%" },
  { symbol: "AAPL_260717_C150", type: "OPTION", exchange: "OPRA", margin: "20%" },
  { symbol: "ES_U26", type: "FUTURE", exchange: "CME", margin: "8%" },
  { symbol: "EURUSD", type: "FOREX", exchange: "ICE", margin: "2%" },
  { symbol: "BTCUSD", type: "CRYPTO", exchange: "COINBASE", margin: "50%" },
  { symbol: "US10Y", type: "BOND", exchange: "CANTOR", margin: "1%" },
  { symbol: "GLD", type: "COMMODITY", exchange: "NYSE_ARCA", margin: "10%" }
];

export const AssetUniverse: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Multi-Asset Security Master Universe</h4>
        <Badge variant="info">7 ACTIVE CLASSES</Badge>
      </div>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Symbol</th>
              <th className="px-3 py-2.5">Asset Type</th>
              <th className="px-3 py-2.5">Exchange</th>
              <th className="px-3 py-2.5 text-right">Margin Requirement</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {assets.map((item) => (
              <tr key={item.symbol} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-bold">{item.symbol}</td>
                <td className="px-3 py-2.5">
                  <Badge variant="info">{item.type}</Badge>
                </td>
                <td className="px-3 py-2.5 text-mutedCustom">{item.exchange}</td>
                <td className="px-3 py-2.5 text-right font-mono text-accentCustom">{item.margin}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default AssetUniverse;
