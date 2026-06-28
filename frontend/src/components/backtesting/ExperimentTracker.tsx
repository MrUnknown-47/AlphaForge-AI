"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { Button } from "../ui/Button";

interface Experiment {
  id: string;
  model: string;
  parameters: string;
  sharpe: number;
  hit_ratio: number;
  drawdown: number;
  status: string;
}

const experiments: Experiment[] = [
  { id: "EXP_402", model: "XGBoost + LSTM", parameters: "Cap: 1M, Comm: 0.05%", sharpe: 1.85, hit_ratio: 62.4, drawdown: 3.12, status: "COMPLETE" },
  { id: "EXP_401", model: "XGBoost Momentum", parameters: "Cap: 1M, Comm: 0.05%", sharpe: 1.54, hit_ratio: 58.2, drawdown: 4.85, status: "SAVED" }
];

export const ExperimentTracker = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Quant Experiment Laboratory Log</h4>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Experiment ID</th>
              <th className="px-3 py-2.5">Model</th>
              <th className="px-3 py-2.5">Sharpe</th>
              <th className="px-3 py-2.5">Hit Ratio</th>
              <th className="px-3 py-2.5">Max Drawdown</th>
              <th className="px-3 py-2.5">Status</th>
              <th className="px-3 py-2.5">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {experiments.map((exp) => (
              <tr key={exp.id} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-mono font-bold">{exp.id}</td>
                <td className="px-3 py-2.5 text-mutedCustom">{exp.model}</td>
                <td className="px-3 py-2.5 font-mono text-accentCustom">{exp.sharpe.toFixed(2)}</td>
                <td className="px-3 py-2.5 font-mono text-white">{exp.hit_ratio}%</td>
                <td className="px-3 py-2.5 font-mono text-dangerCustom">-{exp.drawdown}%</td>
                <td className="px-3 py-2.5">
                  <Badge variant="success">{exp.status}</Badge>
                </td>
                <td className="px-3 py-2.5">
                  <Button variant="ghost" size="sm">Compare</Button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
export default ExperimentTracker;
