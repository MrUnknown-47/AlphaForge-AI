"use client";

import React, { useState } from "react";
import { Badge } from "../ui/Badge";

interface Scenario {
  name: string;
  drawdown: string;
  pnl: string;
  recovery: string;
}

const mockScenarios: Record<string, Scenario[]> = {
  "Rate Hikes": [
    { name: "2022 Interest Rate Shock", drawdown: "-3.12%", pnl: "-$312K", recovery: "12 Days" },
    { name: "2018 Fed Tightening Cycle", drawdown: "-2.15%", pnl: "-$215K", recovery: "8 Days" }
  ],
  "Black Swan": [
    { name: "2020 COVID Market Crash", drawdown: "-4.85%", pnl: "-$485K", recovery: "18 Days" },
    { name: "2008 Lehman Liquidity Crisis", drawdown: "-8.42%", pnl: "-$842K", recovery: "45 Days" }
  ]
};

export const ScenarioSimulator = () => {
  const [target, setTarget] = useState("Rate Hikes");
  const data = mockScenarios[target] || mockScenarios["Rate Hikes"];

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Historical Macro Scenario Stress Tests</h4>
        <div className="flex gap-1.5">
          {["Rate Hikes", "Black Swan"].map((s) => (
            <button
              key={s}
              onClick={() => setTarget(s)}
              className={`px-2 py-0.5 text-[10px] font-bold rounded uppercase tracking-wider border ${
                target === s
                  ? "bg-accentCustom text-terminal border-accentCustom"
                  : "bg-secondaryBg text-mutedCustom border-borderCustom hover:text-white"
              }`}
            >
              {s}
            </button>
          ))}
        </div>
      </div>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Stress Scenario</th>
              <th className="px-3 py-2.5">Simulated Drawdown</th>
              <th className="px-3 py-2.5">Simulated PnL</th>
              <th className="px-3 py-2.5">Recovery Days</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium font-mono text-white">
            {data.map((row) => (
              <tr key={row.name} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-sans font-bold">{row.name}</td>
                <td className="px-3 py-2.5 text-dangerCustom">{row.drawdown}</td>
                <td className="px-3 py-2.5 text-dangerCustom">{row.pnl}</td>
                <td className="px-3 py-2.5">{row.recovery}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
export default ScenarioSimulator;
