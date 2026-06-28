"use client";

import React from "react";
import { Badge } from "../ui/Badge";

interface Execution {
  id: string;
  ticker: string;
  side: "BUY" | "SELL";
  price: number;
  qty: number;
  latency: number; // ms
  slippage: number; // cents
  status: "FILLED" | "PARTIAL" | "PENDING" | "REJECTED";
}

const mockExecutions: Execution[] = [
  { id: "ord_1024", ticker: "AAPL", side: "BUY", price: 182.50, qty: 100, latency: 45, slippage: 0.01, status: "FILLED" },
  { id: "ord_1025", ticker: "NVDA", side: "BUY", price: 875.00, qty: 50, latency: 52, slippage: 0.05, status: "FILLED" }
];

export const ExecutionMonitor = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Execution Telemetry Logs</h4>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2">Order ID</th>
              <th className="px-3 py-2">Ticker</th>
              <th className="px-3 py-2">Side</th>
              <th className="px-3 py-2">Fill Price</th>
              <th className="px-3 py-2">Qty</th>
              <th className="px-3 py-2">Latency</th>
              <th className="px-3 py-2">Slippage</th>
              <th className="px-3 py-2">Status</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {mockExecutions.map((exec) => (
              <tr key={exec.id} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2 text-white font-mono">{exec.id}</td>
                <td className="px-3 py-2 text-white font-bold">{exec.ticker}</td>
                <td className="px-3 py-2">
                  <Badge variant={exec.side === "BUY" ? "success" : "danger"}>
                    {exec.side}
                  </Badge>
                </td>
                <td className="px-3 py-2 font-mono">${exec.price.toFixed(2)}</td>
                <td className="px-3 py-2 font-mono">{exec.qty}</td>
                <td className="px-3 py-2 font-mono text-accentCustom">{exec.latency}ms</td>
                <td className="px-3 py-2 font-mono text-warningCustom">${exec.slippage.toFixed(2)}</td>
                <td className="px-3 py-2">
                  <Badge variant="success">{exec.status}</Badge>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
export default ExecutionMonitor;
