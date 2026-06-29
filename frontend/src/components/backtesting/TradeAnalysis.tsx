"use client";

import React, { useState } from "react";
import { Badge } from "../ui/Badge";
import { SearchBar } from "../ui/SearchBar";

interface Trade {
  id: string;
  symbol: string;
  side: "BUY" | "SELL";
  price: number;
  qty: number;
  pnl: number;
  pnl_pct: number;
  timestamp: string;
}

const mockBlotter: Trade[] = [
  { id: "trd_2001", symbol: "AAPL", side: "BUY", price: 182.40, qty: 100, pnl: 270.00, pnl_pct: 1.48, timestamp: "2026-06-25 10:15:30" },
  { id: "trd_2002", symbol: "NVDA", side: "BUY", price: 920.00, qty: 50, pnl: 1250.00, pnl_pct: 2.72, timestamp: "2026-06-25 11:32:00" },
  { id: "trd_2003", symbol: "MSFT", side: "SELL", price: 415.00, qty: 80, pnl: -240.00, pnl_pct: -0.72, timestamp: "2026-06-26 14:02:15" },
  { id: "trd_2004", symbol: "TSLA", side: "BUY", price: 178.50, qty: 120, pnl: 480.00, pnl_pct: 2.24, timestamp: "2026-06-26 15:45:00" }
];

export const TradeAnalysis: React.FC = () => {
  const [search, setSearch] = useState("");

  const filtered = mockBlotter.filter((t) =>
    t.symbol.toLowerCase().includes(search.toLowerCase()) ||
    t.side.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Backtest Historical Trade Blotter</h4>
        <SearchBar placeholder="Filter symbol..." onSearch={setSearch} />
      </div>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Trade ID</th>
              <th className="px-3 py-2.5">Symbol</th>
              <th className="px-3 py-2.5">Side</th>
              <th className="px-3 py-2.5">Price</th>
              <th className="px-3 py-2.5">Quantity</th>
              <th className="px-3 py-2.5">Realized PnL</th>
              <th className="px-3 py-2.5">Execution Time</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {filtered.map((t) => {
              const isPositive = t.pnl >= 0;
              return (
                <tr key={t.id} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                  <td className="px-3 py-2.5 text-white font-mono">{t.id}</td>
                  <td className="px-3 py-2.5 text-white font-bold">{t.symbol}</td>
                  <td className="px-3 py-2.5">
                    <Badge variant={t.side === "BUY" ? "success" : "danger"}>
                      {t.side}
                    </Badge>
                  </td>
                  <td className="px-3 py-2.5 font-mono">${t.price.toFixed(2)}</td>
                  <td className="px-3 py-2.5 font-mono text-white">{t.qty}</td>
                  <td className={`px-3 py-2.5 font-mono ${isPositive ? "text-successCustom" : "text-dangerCustom"}`}>
                    ${t.pnl.toFixed(2)} ({isPositive ? "+" : ""}{t.pnl_pct.toFixed(2)}%)
                  </td>
                  <td className="px-3 py-2.5 font-mono text-mutedCustom">{t.timestamp}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default TradeAnalysis;
