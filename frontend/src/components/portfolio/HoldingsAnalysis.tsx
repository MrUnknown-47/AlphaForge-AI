"use client";

import React, { useState } from "react";
import { SearchBar } from "../ui/SearchBar";

interface Holding {
  symbol: string;
  weight: number;
  quantity: number;
  market_value: number;
  unrealized_pnl: number;
  return_pct: number;
  sector: string;
}

const mockHoldings: Holding[] = [
  { symbol: "AAPL", weight: 24.5, quantity: 1395, market_value: 258286.00, unrealized_pnl: 2500.00, return_pct: 1.39, sector: "Technology" },
  { symbol: "NVDA", weight: 41.2, quantity: 496, market_value: 434343.00, unrealized_pnl: 12500.00, return_pct: 2.94, sector: "Technology" },
  { symbol: "MSFT", quantity: 472, weight: 18.5, market_value: 195032.00, unrealized_pnl: 600.00, return_pct: 0.48, sector: "Technology" },
  { symbol: "TSLA", quantity: 950, weight: 15.8, market_value: 166570.00, unrealized_pnl: -1440.00, return_pct: -1.03, sector: "Automotive" }
];

export const HoldingsAnalysis: React.FC = () => {
  const [search, setSearch] = useState("");

  const filtered = mockHoldings.filter((h) =>
    h.symbol.toLowerCase().includes(search.toLowerCase()) ||
    h.sector.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Portfolio Holdings Table</h4>
        <SearchBar placeholder="Filter symbol..." onSearch={setSearch} />
      </div>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Symbol</th>
              <th className="px-3 py-2.5">Weight</th>
              <th className="px-3 py-2.5">Quantity</th>
              <th className="px-3 py-2.5">Market Value</th>
              <th className="px-3 py-2.5">Unrealized PnL</th>
              <th className="px-3 py-2.5">Sector</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {filtered.map((pos) => {
              const isPositive = pos.unrealized_pnl >= 0;
              return (
                <tr key={pos.symbol} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                  <td className="px-3 py-2.5 text-white font-bold">{pos.symbol}</td>
                  <td className="px-3 py-2.5 font-mono text-accentCustom">{pos.weight}%</td>
                  <td className="px-3 py-2.5 font-mono text-white">{pos.quantity.toLocaleString()}</td>
                  <td className="px-3 py-2.5 font-mono text-white">${pos.market_value.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
                  <td className={`px-3 py-2.5 font-mono ${isPositive ? "text-successCustom" : "text-dangerCustom"}`}>
                    ${pos.unrealized_pnl.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })} ({isPositive ? "+" : ""}{pos.return_pct.toFixed(2)}%)
                  </td>
                  <td className="px-3 py-2.5 text-mutedCustom">{pos.sector}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default HoldingsAnalysis;
