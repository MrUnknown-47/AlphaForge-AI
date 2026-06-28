"use client";

import React, { useState } from "react";
import { Button } from "../ui/Button";

export const BacktestControl = ({ onRunBacktest }: { onRunBacktest: () => void }) => {
  const [strategy, setStrategy] = useState("AlphaForge Ensemble v1");
  const [model, setModel] = useState("XGBoost + LSTM");
  const [universe, setUniverse] = useState("US Equities Top 10");
  const [capital, setCapital] = useState(1000000);
  const [commission, setCommission] = useState(0.0005);
  const [slippage, setSlippage] = useState(0.01);

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Backtesting Simulator Parameters</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-[10px] text-mutedCustom font-bold uppercase mb-1">Strategy Name</label>
            <select
              className="w-full bg-cardBg border border-borderCustom rounded px-3 py-1.5 focus:outline-none text-white font-bold"
              value={strategy}
              onChange={(e) => setStrategy(e.target.value)}
            >
              <option value="AlphaForge Ensemble v1">AlphaForge Ensemble v1</option>
              <option value="XGBoost Momentum v1">XGBoost Momentum v1</option>
            </select>
          </div>
          <div>
            <label className="block text-[10px] text-mutedCustom font-bold uppercase mb-1">Execution Model</label>
            <input
              type="text"
              className="w-full bg-cardBg border border-borderCustom rounded px-3 py-1.5 focus:outline-none text-white"
              value={model}
              readOnly
            />
          </div>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-[10px] text-mutedCustom font-bold uppercase mb-1">Capital Allocation</label>
            <input
              type="number"
              className="w-full bg-cardBg border border-borderCustom rounded px-3 py-1.5 focus:outline-none text-white font-mono"
              value={capital}
              onChange={(e) => setCapital(Number(e.target.value))}
            />
          </div>
          <div>
            <label className="block text-[10px] text-mutedCustom font-bold uppercase mb-1">Asset Universe</label>
            <input
              type="text"
              className="w-full bg-cardBg border border-borderCustom rounded px-3 py-1.5 focus:outline-none text-white"
              value={universe}
              readOnly
            />
          </div>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-[10px] text-mutedCustom font-bold uppercase mb-1">Commission Rate</label>
            <input
              type="number"
              step={0.0001}
              className="w-full bg-cardBg border border-borderCustom rounded px-3 py-1.5 focus:outline-none text-white font-mono"
              value={commission}
              onChange={(e) => setCommission(Number(e.target.value))}
            />
          </div>
          <div>
            <label className="block text-[10px] text-mutedCustom font-bold uppercase mb-1">Estimated Slippage</label>
            <input
              type="number"
              step={0.005}
              className="w-full bg-cardBg border border-borderCustom rounded px-3 py-1.5 focus:outline-none text-white font-mono"
              value={slippage}
              onChange={(e) => setSlippage(Number(e.target.value))}
            />
          </div>
        </div>

        <div className="flex gap-3 justify-end pt-2">
          <Button variant="secondary" size="sm">Walk Forward</Button>
          <Button variant="primary" size="sm" onClick={onRunBacktest}>Run Simulator</Button>
        </div>
      </div>
    </div>
  );
};
export default BacktestControl;
