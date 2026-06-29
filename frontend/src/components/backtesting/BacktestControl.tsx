"use client";

import React, { useState } from "react";
import { Button } from "../ui/Button";

interface BacktestControlProps {
  onRunBacktest: () => void;
}

export const BacktestControl: React.FC<BacktestControlProps> = ({ onRunBacktest }) => {
  const [strategy, setStrategy] = useState("AlphaForge Ensemble v1");
  const [strategyCode, setStrategyCode] = useState(
    `# Define AlphaForge custom trading strategy logic\ndef initialize(context):\n    context.security = symbol('AAPL')\n    schedule_function(rebalance, date_rules.every_day())\n\ndef rebalance(context, data):\n    score = context.models.predict(data)\n    if score > 0.65:\n        order_target_percent(context.security, 0.40)\n    elif score < 0.35:\n        order_target_percent(context.security, 0.0)`
  );
  const [capital, setCapital] = useState(1000000);
  const [commission, setCommission] = useState(0.0005);
  const [slippage, setSlippage] = useState(0.01);

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Backtest Strategy Lab & Controls</h4>
        <span className="text-[10px] text-mutedCustom font-semibold uppercase">v3.0.0</span>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
        {/* Left: Strategy Editor */}
        <div className="space-y-2">
          <label className="block text-[10px] text-mutedCustom font-bold uppercase">Python Strategy Code Editor</label>
          <textarea
            className="w-full h-48 bg-black bg-opacity-40 border border-borderCustom rounded p-3 focus:outline-none text-[10px] text-successCustom font-mono leading-relaxed resize-none"
            value={strategyCode}
            onChange={(e) => setStrategyCode(e.target.value)}
          />
        </div>

        {/* Right: Parameter Panel & Run Controls */}
        <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
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
              <label className="block text-[10px] text-mutedCustom font-bold uppercase mb-1">Commission Rate</label>
              <input
                type="number"
                step={0.0001}
                className="w-full bg-cardBg border border-borderCustom rounded px-3 py-1.5 focus:outline-none text-white font-mono"
                value={commission}
                onChange={(e) => setCommission(Number(e.target.value))}
              />
            </div>
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

          <div className="flex gap-3 justify-end pt-2">
            <Button variant="secondary" size="sm">Walk Forward Matrix</Button>
            <Button variant="primary" size="sm" onClick={onRunBacktest}>Run Simulator</Button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default BacktestControl;
