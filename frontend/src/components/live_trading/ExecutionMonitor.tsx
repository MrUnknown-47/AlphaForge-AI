"use client";

import React from "react";
import { useTradingStore } from "../../store/tradingStore";
import { Badge } from "../ui/Badge";

export const ExecutionMonitor: React.FC = () => {
  const { orders, fills } = useTradingStore();

  return (
    <div className="space-y-6">
      {/* SECTION 2: ACTIVE ORDERS PANEL */}
      <div className="space-y-3">
        <div className="flex justify-between items-center border-b border-borderCustom pb-2">
          <h4 className="text-xs font-bold uppercase tracking-wider text-white">Active Orders</h4>
          <span className="text-[10px] text-mutedCustom font-semibold uppercase">Pending: {orders.length}</span>
        </div>

        {orders.length === 0 ? (
          <div className="py-6 text-center text-xs text-mutedCustom border border-dashed border-borderCustom rounded bg-cardBg">
            No active orders.
          </div>
        ) : (
          <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
            <table className="w-full text-left text-xs border-collapse">
              <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
                <tr>
                  <th className="px-3 py-2">Order ID</th>
                  <th className="px-3 py-2">Symbol</th>
                  <th className="px-3 py-2">Side</th>
                  <th className="px-3 py-2">Order Type</th>
                  <th className="px-3 py-2">Quantity</th>
                  <th className="px-3 py-2">Limit Price</th>
                  <th className="px-3 py-2">Status</th>
                  <th className="px-3 py-2">Submitted Time</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-borderCustom font-medium">
                {orders.map((ord) => (
                  <tr key={ord.id} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                    <td className="px-3 py-2 text-white font-mono">{ord.id}</td>
                    <td className="px-3 py-2 text-white font-bold">{ord.ticker}</td>
                    <td className="px-3 py-2">
                      <Badge variant={ord.side === "BUY" ? "success" : "danger"}>
                        {ord.side}
                      </Badge>
                    </td>
                    <td className="px-3 py-2 text-mutedCustom uppercase">{ord.type}</td>
                    <td className="px-3 py-2 font-mono text-white">{ord.quantity}</td>
                    <td className="px-3 py-2 font-mono">
                      {ord.price ? `$${ord.price.toFixed(2)}` : "MKT"}
                    </td>
                    <td className="px-3 py-2">
                      <Badge variant={ord.status === "PENDING" ? "warning" : ord.status === "FILLED" ? "success" : "danger"}>
                        {ord.status}
                      </Badge>
                    </td>
                    <td className="px-3 py-2 text-[10px] text-mutedCustom font-mono">
                      {new Date(ord.timestamp).toLocaleTimeString()}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>

      {/* SECTION 3: FILLS PANEL */}
      <div className="space-y-3">
        <div className="flex justify-between items-center border-b border-borderCustom pb-2">
          <h4 className="text-xs font-bold uppercase tracking-wider text-white">Execution Fills</h4>
          <span className="text-[10px] text-mutedCustom font-semibold uppercase">Count: {fills.length}</span>
        </div>

        {fills.length === 0 ? (
          <div className="py-6 text-center text-xs text-mutedCustom border border-dashed border-borderCustom rounded bg-cardBg">
            No executions registered.
          </div>
        ) : (
          <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
            <table className="w-full text-left text-xs border-collapse">
              <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
                <tr>
                  <th className="px-3 py-2">Fill ID</th>
                  <th className="px-3 py-2">Symbol</th>
                  <th className="px-3 py-2">Side</th>
                  <th className="px-3 py-2">Executed Price</th>
                  <th className="px-3 py-2">Quantity</th>
                  <th className="px-3 py-2">Commission</th>
                  <th className="px-3 py-2">Slippage (bps)</th>
                  <th className="px-3 py-2">Latency</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-borderCustom font-medium">
                {fills.map((fill) => (
                  <tr key={fill.id} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                    <td className="px-3 py-2 text-white font-mono">{fill.id}</td>
                    <td className="px-3 py-2 text-white font-bold">{fill.ticker}</td>
                    <td className="px-3 py-2">
                      <Badge variant={fill.side === "BUY" ? "success" : "danger"}>
                        {fill.side}
                      </Badge>
                    </td>
                    <td className="px-3 py-2 font-mono">${fill.price.toFixed(2)}</td>
                    <td className="px-3 py-2 font-mono text-white">{fill.quantity}</td>
                    <td className="px-3 py-2 font-mono text-mutedCustom">${fill.commission.toFixed(2)}</td>
                    <td className="px-3 py-2 font-mono text-warningCustom">{fill.slippage_bps} bps</td>
                    <td className="px-3 py-2 font-mono text-accentCustom">{fill.latency_ms}ms</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
};

export default ExecutionMonitor;
