"use client";

import React from "react";
import { useTradingStore } from "../../store/tradingStore";
import { Badge } from "../ui/Badge";
import { Button } from "../ui/Button";

interface PositionMonitorProps {
  onClosePosition: (ticker: string) => void;
}

export const PositionMonitor: React.FC<PositionMonitorProps> = ({ onClosePosition }) => {
  const { positions } = useTradingStore();

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Live Positions Monitor</h4>
        <span className="text-[10px] text-mutedCustom font-semibold uppercase">Count: {positions.length}</span>
      </div>

      {positions.length === 0 ? (
        <div className="py-8 text-center text-xs text-mutedCustom border border-dashed border-borderCustom rounded">
          No active positions. Open new positions via order execution.
        </div>
      ) : (
        <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
          <table className="w-full text-left text-xs border-collapse">
            <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
              <tr>
                <th className="px-3 py-2.5">Symbol</th>
                <th className="px-3 py-2.5">Side</th>
                <th className="px-3 py-2.5">Quantity</th>
                <th className="px-3 py-2.5">Entry Price</th>
                <th className="px-3 py-2.5">Current Price</th>
                <th className="px-3 py-2.5">Unrealized PnL</th>
                <th className="px-3 py-2.5">Realized PnL</th>
                <th className="px-3 py-2.5">Exposure %</th>
                <th className="px-3 py-2.5">Status</th>
                <th className="px-3 py-2.5 text-right">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-borderCustom font-medium">
              {positions.map((pos) => {
                const isPositive = pos.pnl >= 0;
                return (
                  <tr key={pos.ticker} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                    <td className="px-3 py-2.5 text-white font-bold">{pos.ticker}</td>
                    <td className="px-3 py-2.5">
                      <Badge variant={pos.side === "LONG" ? "success" : "danger"}>
                        {pos.side}
                      </Badge>
                    </td>
                    <td className="px-3 py-2.5 text-white font-mono">{pos.quantity}</td>
                    <td className="px-3 py-2.5 font-mono">${pos.entry.toFixed(2)}</td>
                    <td className="px-3 py-2.5 font-mono">${pos.current.toFixed(2)}</td>
                    <td className={`px-3 py-2.5 font-mono ${isPositive ? "text-successCustom" : "text-dangerCustom"}`}>
                      ${pos.pnl.toFixed(2)} ({isPositive ? "+" : ""}{pos.pnl_pct.toFixed(2)}%)
                    </td>
                    <td className="px-3 py-2.5 font-mono text-mutedCustom">
                      $0.00
                    </td>
                    <td className="px-3 py-2.5 font-mono text-accentCustom">{pos.exposure_pct}%</td>
                    <td className="px-3 py-2.5">
                      <span className="text-[10px] text-successCustom font-bold tracking-wider">{pos.status}</span>
                    </td>
                    <td className="px-3 py-2.5 text-right">
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
      )}
    </div>
  );
};

export default PositionMonitor;
