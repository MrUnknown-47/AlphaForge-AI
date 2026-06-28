"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { Button } from "../ui/Button";

interface Run {
  id: string;
  model: string;
  sharpe: number;
  hit_ratio: number;
  drawdown: number;
  cagr: number;
  status: string;
}

const leaderboardHistory: Run[] = [
  { id: "OPT_RUN_702", model: "TFT Transformer", sharpe: 2.05, hit_ratio: 65.4, drawdown: 2.85, cagr: 22.40, status: "DEPLOYABLE" },
  { id: "OPT_RUN_701", model: "XGBoost + LSTM", sharpe: 1.85, hit_ratio: 62.4, drawdown: 3.12, cagr: 18.54, status: "ACTIVE" }
];

export const Leaderboard = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">AI Optimization Runs Leaderboard</h4>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Run ID</th>
              <th className="px-3 py-2.5">Model</th>
              <th className="px-3 py-2.5">Sharpe</th>
              <th className="px-3 py-2.5">Hit Ratio</th>
              <th className="px-3 py-2.5">Max Drawdown</th>
              <th className="px-3 py-2.5">CAGR %</th>
              <th className="px-3 py-2.5">Status</th>
              <th className="px-3 py-2.5">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {leaderboardHistory.map((row) => (
              <tr key={row.id} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-mono font-bold">{row.id}</td>
                <td className="px-3 py-2.5 text-mutedCustom">{row.model}</td>
                <td className="px-3 py-2.5 font-mono text-accentCustom">{row.sharpe.toFixed(2)}</td>
                <td className="px-3 py-2.5 font-mono text-white">{row.hit_ratio}%</td>
                <td className="px-3 py-2.5 font-mono text-dangerCustom">-{row.drawdown}%</td>
                <td className="px-3 py-2.5 font-mono text-successCustom">+{row.cagr}%</td>
                <td className="px-3 py-2.5">
                  <Badge variant={row.status === "DEPLOYABLE" ? "info" : "success"}>{row.status}</Badge>
                </td>
                <td className="px-3 py-2.5">
                  <Button variant="primary" size="sm">Deploy</Button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
export default Leaderboard;
