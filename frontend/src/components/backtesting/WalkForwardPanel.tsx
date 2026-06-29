"use client";

import React from "react";
import { Badge } from "../ui/Badge";

interface WFOSplit {
  window: string;
  trainSharpe: number;
  valSharpe: number;
  testSharpe: number;
  status: "PASS" | "FAIL" | "WARNING";
}

const mockMatrix: WFOSplit[] = [
  { window: "Split 1 (2021-2022)", trainSharpe: 2.10, valSharpe: 1.95, testSharpe: 1.82, status: "PASS" },
  { window: "Split 2 (2022-2023)", trainSharpe: 1.98, valSharpe: 1.88, testSharpe: 1.74, status: "PASS" },
  { window: "Split 3 (2023-2024)", trainSharpe: 2.25, valSharpe: 2.05, testSharpe: 1.88, status: "PASS" },
  { window: "Split 4 (2024-2025)", trainSharpe: 2.02, valSharpe: 1.90, testSharpe: 1.80, status: "PASS" }
];

export const WalkForwardPanel: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Walk Forward Matrix</h4>
        <span className="text-[10px] text-mutedCustom font-semibold uppercase">Cross-Validation splits</span>
      </div>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2">Split Window</th>
              <th className="px-3 py-2">Train Sharpe</th>
              <th className="px-3 py-2">Val Sharpe</th>
              <th className="px-3 py-2">Test Sharpe</th>
              <th className="px-3 py-2">Status</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {mockMatrix.map((row) => (
              <tr key={row.window} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2 text-white font-bold">{row.window}</td>
                <td className="px-3 py-2 font-mono text-mutedCustom">{row.trainSharpe.toFixed(2)}</td>
                <td className="px-3 py-2 font-mono text-mutedCustom">{row.valSharpe.toFixed(2)}</td>
                <td className="px-3 py-2 font-mono text-accentCustom font-bold">{row.testSharpe.toFixed(2)}</td>
                <td className="px-3 py-2">
                  <Badge variant="success">{row.status}</Badge>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default WalkForwardPanel;
