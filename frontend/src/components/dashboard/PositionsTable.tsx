"use client";

import React, { useState } from "react";
import { Badge } from "../ui/Badge";
import { SearchBar } from "../ui/SearchBar";

interface Position {
  ticker: string;
  direction: "LONG" | "SHORT";
  quantity: number;
  entry: number;
  current: number;
  pnl: number;
  pnl_pct: number;
  stop_loss: number;
  take_profit: number;
  confidence: number;
  status: string;
}

const mockPositions: Position[] = [
  { ticker: "AAPL", direction: "LONG", quantity: 100, entry: 180.00, current: 182.50, pnl: 250.00, pnl_pct: 1.39, stop_loss: 174.60, take_profit: 198.00, confidence: 82, status: "ACTIVE" },
  { ticker: "NVDA", direction: "LONG", quantity: 50, entry: 850.00, current: 875.00, pnl: 1250.00, pnl_pct: 2.94, stop_loss: 824.50, take_profit: 950.00, confidence: 91, status: "ACTIVE" },
  { ticker: "MSFT", direction: "SHORT", quantity: 30, entry: 420.00, current: 418.00, pnl: 60.00, pnl_pct: 0.48, stop_loss: 432.60, take_profit: 395.00, confidence: 71, status: "ACTIVE" },
  { ticker: "TSLA", direction: "LONG", quantity: 80, entry: 175.00, current: 173.20, pnl: -144.00, pnl_pct: -1.03, stop_loss: 169.75, take_profit: 192.50, confidence: 65, status: "ACTIVE" }
];

export const PositionsTable = () => {
  const [search, setSearch] = useState("");
  const [expandedRow, setExpandedRow] = useState<string | null>(null);

  const filtered = mockPositions.filter((pos) =>
    pos.ticker.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Live Reconciled Positions</h4>
        <SearchBar placeholder="Filter positions..." onSearch={setSearch} />
      </div>

      <div className="w-full overflow-x-auto rounded border border-borderCustom bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] uppercase text-mutedCustom tracking-wider">
            <tr>
              <th className="px-4 py-3 font-semibold">Ticker</th>
              <th className="px-4 py-3 font-semibold">Direction</th>
              <th className="px-4 py-3 font-semibold">Quantity</th>
              <th className="px-4 py-3 font-semibold">Entry</th>
              <th className="px-4 py-3 font-semibold">Current</th>
              <th className="px-4 py-3 font-semibold">PnL</th>
              <th className="px-4 py-3 font-semibold">PnL %</th>
              <th className="px-4 py-3 font-semibold">Confidence</th>
              <th className="px-4 py-3 font-semibold">Status</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {filtered.map((pos) => {
              const isExpanded = expandedRow === pos.ticker;
              const isPositive = pos.pnl >= 0;
              return (
                <React.Fragment key={pos.ticker}>
                  <tr
                    onClick={() => setExpandedRow(isExpanded ? null : pos.ticker)}
                    className="hover:bg-secondaryBg hover:bg-opacity-50 cursor-pointer transition-colors"
                  >
                    <td className="px-4 py-3 text-white font-bold">{pos.ticker}</td>
                    <td className="px-4 py-3">
                      <Badge variant={pos.direction === "LONG" ? "success" : "danger"}>
                        {pos.direction}
                      </Badge>
                    </td>
                    <td className="px-4 py-3 text-white font-mono">{pos.quantity}</td>
                    <td className="px-4 py-3 font-mono">${pos.entry.toFixed(2)}</td>
                    <td className="px-4 py-3 font-mono">${pos.current.toFixed(2)}</td>
                    <td className={`px-4 py-3 font-mono ${isPositive ? "text-successCustom" : "text-dangerCustom"}`}>
                      ${pos.pnl.toFixed(2)}
                    </td>
                    <td className={`px-4 py-3 font-mono ${isPositive ? "text-successCustom" : "text-dangerCustom"}`}>
                      {isPositive ? "+" : ""}{pos.pnl_pct.toFixed(2)}%
                    </td>
                    <td className="px-4 py-3 font-mono text-accentCustom">{pos.confidence}%</td>
                    <td className="px-4 py-3">
                      <Badge variant="info">{pos.status}</Badge>
                    </td>
                  </tr>
                  {isExpanded && (
                    <tr className="bg-secondaryBg bg-opacity-20 text-[10px] text-mutedCustom font-semibold uppercase">
                      <td colSpan={9} className="px-4 py-3">
                        <div className="grid grid-cols-4 gap-4">
                          <div>
                            <span className="block text-mutedCustom">Stop Loss:</span>
                            <span className="text-white font-mono">${pos.stop_loss.toFixed(2)}</span>
                          </div>
                          <div>
                            <span className="block text-mutedCustom">Take Profit:</span>
                            <span className="text-white font-mono">${pos.take_profit.toFixed(2)}</span>
                          </div>
                          <div>
                            <span className="block text-mutedCustom">Risk Ratio:</span>
                            <span className="text-white font-mono">1:2.4</span>
                          </div>
                          <div>
                            <span className="block text-mutedCustom">Execution Engine:</span>
                            <span className="text-white font-mono">Alpaca Gate</span>
                          </div>
                        </div>
                      </td>
                    </tr>
                  )}
                </React.Fragment>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
};
export default PositionsTable;
