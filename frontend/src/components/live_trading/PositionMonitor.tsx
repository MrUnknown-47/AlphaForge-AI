"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { Button } from "../ui/Button";

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
  status: string;
}

const mockPositions: Position[] = [
  { ticker: "AAPL", direction: "LONG", quantity: 100, entry: 180.00, current: 182.50, pnl: 250.00, pnl_pct: 1.39, stop_loss: 174.60, take_profit: 198.00, status: "ACTIVE" },
  { ticker: "NVDA", direction: "LONG", quantity: 50, entry: 850.00, current: 875.00, pnl: 1250.00, pnl_pct: 2.94, stop_loss: 824.50, take_profit: 950.00, status: "ACTIVE" }
];

export const PositionMonitor = ({ onClosePosition }: { onClosePosition: (ticker: string) => void }) => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Active Positions Monitor</h4>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2">Ticker</th>
              <th className="px-3 py-2">Direction</th>
              <th className="px-3 py-2">Qty</th>
              <th className="px-3 py-2">Entry</th>
              <th className="px-3 py-2">Current</th>
              <th className="px-3 py-2">PnL</th>
              <th className="px-3 py-2">Stop Loss</th>
              <th className="px-3 py-2">Take Profit</th>
              <th className="px-3 py-2">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {mockPositions.map((pos) => {
              const isPositive = pos.pnl >= 0;
              return (
                <tr key={pos.ticker} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                  <td className="px-3 py-2 text-white font-bold">{pos.ticker}</td>
                  <td className="px-3 py-2">
                    <Badge variant={pos.direction === "LONG" ? "success" : "danger"}>
                      {pos.direction}
                    </Badge>
                  </td>
                  <td className="px-3 py-2 text-white font-mono">{pos.quantity}</td>
                  <td className="px-3 py-2 font-mono">${pos.entry.toFixed(2)}</td>
                  <td className="px-3 py-2 font-mono">${pos.current.toFixed(2)}</td>
                  <td className={`px-3 py-2 font-mono ${isPositive ? "text-successCustom" : "text-dangerCustom"}`}>
                    ${pos.pnl.toFixed(2)} ({isPositive ? "+" : ""}{pos.pnl_pct.toFixed(2)}%)
                  </td>
                  <td className="px-3 py-2 font-mono text-warningCustom">${pos.stop_loss.toFixed(2)}</td>
                  <td className="px-3 py-2 font-mono text-accentCustom">${pos.take_profit.toFixed(2)}</td>
                  <td className="px-3 py-2">
                    <Button variant="danger" size="sm" onClick={() => onClosePosition(pos.ticker)}>
                      CLOSE
                    </Button>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
};
export default PositionMonitor;
