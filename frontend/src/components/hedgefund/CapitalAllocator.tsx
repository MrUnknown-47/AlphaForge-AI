"use client";

import React, { useState } from "react";
import { Button } from "../ui/Button";

interface AllocRow {
  book: string;
  weight: number;
  risk: number;
}

const allocations: Record<string, AllocRow[]> = {
  "Risk Parity": [
    { book: "Long Short Equities", weight: 50.0, risk: 42.1 },
    { book: "Statistical Arbitrage", weight: 30.0, risk: 36.5 },
    { book: "Macro & Currencies", weight: 20.0, risk: 21.4 }
  ],
  "Equal Weight": [
    { book: "Long Short Equities", weight: 33.3, risk: 52.4 },
    { book: "Statistical Arbitrage", weight: 33.3, risk: 28.5 },
    { book: "Macro & Currencies", weight: 33.3, risk: 19.1 }
  ]
};

export const CapitalAllocator = () => {
  const [method, setMethod] = useState("Risk Parity");
  const data = allocations[method] || allocations["Risk Parity"];

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Capital Allocation & Risk Budgeting</h4>
        <div className="flex gap-1.5">
          {["Risk Parity", "Equal Weight"].map((m) => (
            <button
              key={m}
              onClick={() => setMethod(m)}
              className={`px-2 py-0.5 text-[10px] font-bold rounded uppercase tracking-wider border ${
                method === m
                  ? "bg-accentCustom text-terminal border-accentCustom"
                  : "bg-secondaryBg text-mutedCustom border-borderCustom hover:text-white"
              }`}
            >
              {m}
            </button>
          ))}
        </div>
      </div>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
        <div className="flex justify-between items-center text-xs font-bold text-mutedCustom border-b border-borderCustom pb-2 uppercase">
          <span>Portfolio Sub-Book</span>
          <div className="flex gap-12 font-mono text-[10px]">
            <span>Capital Weight</span>
            <span>Risk Budget %</span>
          </div>
        </div>

        <div className="space-y-3 font-semibold text-white">
          {data.map((row) => (
            <div key={row.book} className="flex justify-between items-center">
              <span className="font-bold">{row.book}</span>
              <div className="flex gap-16 font-mono text-[10px]">
                <span className="text-mutedCustom">{row.weight}%</span>
                <span className="text-accentCustom font-bold">{row.risk}%</span>
              </div>
            </div>
          ))}
        </div>

        <div className="flex justify-end pt-2">
          <Button variant="primary" size="sm">REALLOCATE FUND AUM</Button>
        </div>
      </div>
    </div>
  );
};
export default CapitalAllocator;
