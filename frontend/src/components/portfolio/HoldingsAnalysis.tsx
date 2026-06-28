"use client";

import React, { useState } from "react";
import { Badge } from "../ui/Badge";
import { SearchBar } from "../ui/SearchBar";

interface Holding {
  ticker: string;
  weight: number;
  market_value: number;
  pnl: number;
  return_pct: number;
  beta: number;
  risk_contribution: number;
  sector: string;
}

const mockHoldings: Holding[] = [
  { ticker: "AAPL", weight: 24.5, market_value: 258286.00, pnl: 2500.00, return_pct: 1.39, beta: 1.05, risk_contribution: 22.4, sector: "Technology" },
  { ticker: "NVDA", weight: 41.2, market_value: 434343.00, pnl: 12500.00, return_pct: 2.94, beta: 1.85, risk_contribution: 48.5, sector: "Technology" },
  { ticker: "MSFT", weight: 18.5, market_value: 195032.00, pnl: 600.00, return_pct: 0.48, beta: 0.95, risk_contribution: 15.2, sector: "Technology" },
  { ticker: "TSLA", weight: 15.8, market_value: 166570.00, pnl: -1440.00, return_pct: -1.03, beta: 1.45, risk_contribution: 13.9, sector: "Automotive" }
];

export const HoldingsAnalysis = () => {
  const [search, setSearch] = useState("");

  const filtered = mockHoldings.filter((h) =>
    h.ticker.toLowerCase().includes(search.toLowerCase()) ||
    h.sector.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Portfolio Asset Holdings Allocation</h4>
        <SearchBar placeholder="Filter holdings..." onSearch={setSearch} />
      </div>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Ticker</th>
              <th className="px-3 py-2.5">Sector</th>
              <th className="px-3 py-2.5">Weight</th>
              <th className="px-3 py-2.5">Market Value</th>
              <th className="px-3 py-2.5">PnL</th>
              <th className="px-3 py-2.5">Return %</th>
              <th className="px-3 py-2.5">Beta</th>
              <th className="px-3 py-2.5">Risk Contribution</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {filtered.map((pos) => {
              const isPositive = pos.pnl >= 0;
              return (
                <tr key={pos.ticker} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                  <td className="px-3 py-2.5 text-white font-bold">{pos.ticker}</td>
                  <td className="px-3 py-2.5 text-mutedCustom">{pos.sector}</td>
                  <td className="px-3 py-2.5 font-mono text-accentCustom">{pos.weight}%</td>
                  <td className="px-3 py-2.5 font-mono text-white">${pos.market_value.toLocaleString()}</td>
                  <td className={`px-3 py-2.5 font-mono ${isPositive ? "text-successCustom" : "text-dangerCustom"}`}>
                    ${pos.pnl.toFixed(2)}
                  </td>
                  <td className={`px-3 py-2.5 font-mono ${isPositive ? "text-successCustom" : "text-dangerCustom"}`}>
                    {isPositive ? "+" : ""}{pos.return_pct.toFixed(2)}%
                  </td>
                  <td className="px-3 py-2.5 font-mono text-white">{pos.beta.toFixed(2)}</td>
                  <td className="px-3 py-2.5 font-mono text-warningCustom">{pos.risk_contribution}%</td>
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
