"use client";

import React, { useState } from "react";
import { Badge } from "../ui/Badge";
import { SearchBar } from "../ui/SearchBar";

interface Asset {
  ticker: string;
  price: number;
  change: number;
  volume: string;
  spread: number;
  atr: number;
  regime: string;
  signal: string;
  confidence: number;
}

const initialAssets: Asset[] = [
  { ticker: "AAPL", price: 182.50, change: 1.39, volume: "52.4M", spread: 0.02, atr: 3.12, regime: "BULL", signal: "BUY", confidence: 82 },
  { ticker: "MSFT", price: 418.00, change: -0.48, volume: "22.8M", spread: 0.05, atr: 7.45, regime: "BULL", signal: "SELL", confidence: 71 },
  { ticker: "NVDA", price: 875.00, change: 2.94, volume: "42.1M", spread: 0.12, atr: 24.50, regime: "BULL", signal: "BUY", confidence: 91 },
  { ticker: "GOOGL", price: 151.60, change: 0.22, volume: "28.5M", spread: 0.01, atr: 2.10, regime: "BULL", signal: "HOLD", confidence: 60 },
  { ticker: "AMZN", price: 178.40, change: 0.85, volume: "31.2M", spread: 0.03, atr: 3.80, regime: "BULL", signal: "BUY", confidence: 78 },
  { ticker: "META", price: 485.20, change: -1.12, volume: "18.4M", spread: 0.08, atr: 11.20, regime: "BULL", signal: "SELL", confidence: 73 },
  { ticker: "TSLA", price: 173.20, change: -1.03, volume: "84.2M", spread: 0.04, atr: 6.85, regime: "BULL", signal: "HOLD", confidence: 65 }
];

export const MarketWatch = ({ onSelectTicker }: { onSelectTicker: (t: string) => void }) => {
  const [search, setSearch] = useState("");

  const filtered = initialAssets.filter((asset) =>
    asset.ticker.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Live Market Watchlist</h4>
        <SearchBar placeholder="Search assets..." onSearch={setSearch} />
      </div>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Ticker</th>
              <th className="px-3 py-2.5">Price</th>
              <th className="px-3 py-2.5">Change %</th>
              <th className="px-3 py-2.5">Spread</th>
              <th className="px-3 py-2.5">ATR</th>
              <th className="px-3 py-2.5">Signal</th>
              <th className="px-3 py-2.5">Conf</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {filtered.map((asset) => {
              const isPositive = asset.change >= 0;
              return (
                <tr
                  key={asset.ticker}
                  onClick={() => onSelectTicker(asset.ticker)}
                  className="hover:bg-secondaryBg hover:bg-opacity-50 cursor-pointer transition-colors"
                >
                  <td className="px-3 py-2.5 text-white font-bold">{asset.ticker}</td>
                  <td className="px-3 py-2.5 font-mono">${asset.price.toFixed(2)}</td>
                  <td className={`px-3 py-2.5 font-mono ${isPositive ? "text-successCustom" : "text-dangerCustom"}`}>
                    {isPositive ? "+" : ""}{asset.change.toFixed(2)}%
                  </td>
                  <td className="px-3 py-2.5 font-mono">${asset.spread.toFixed(2)}</td>
                  <td className="px-3 py-2.5 font-mono">{asset.atr.toFixed(2)}</td>
                  <td className="px-3 py-2.5">
                    <Badge variant={asset.signal === "BUY" ? "success" : asset.signal === "SELL" ? "danger" : "warning"}>
                      {asset.signal}
                    </Badge>
                  </td>
                  <td className="px-3 py-2.5 font-mono text-accentCustom">{asset.confidence}%</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
};
export default MarketWatch;
