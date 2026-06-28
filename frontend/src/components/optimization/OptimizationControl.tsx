"use client";

import React, { useState } from "react";
import { Button } from "../ui/Button";

export const OptimizationControl = ({ onStart }: { onStart: () => void }) => {
  const [optimizer, setOptimizer] = useState("Bayesian (Optuna)");
  const [objective, setObjective] = useState("Max Sharpe Ratio");
  const [iterations, setIterations] = useState(100);

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">AI Optimization Controller</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-[10px] text-mutedCustom font-bold uppercase mb-1">Optimizer Algorithm</label>
            <select
              className="w-full bg-cardBg border border-borderCustom rounded px-3 py-1.5 focus:outline-none text-white font-bold"
              value={optimizer}
              onChange={(e) => setOptimizer(e.target.value)}
            >
              <option value="Bayesian (Optuna)">Bayesian (Optuna)</option>
              <option value="Genetic Algorithm">Genetic Algorithm</option>
              <option value="Reinforcement Learning">Reinforcement Learning</option>
            </select>
          </div>
          <div>
            <label className="block text-[10px] text-mutedCustom font-bold uppercase mb-1">Objective Target</label>
            <select
              className="w-full bg-cardBg border border-borderCustom rounded px-3 py-1.5 focus:outline-none text-white font-bold"
              value={objective}
              onChange={(e) => setObjective(e.target.value)}
            >
              <option value="Max Sharpe Ratio">Max Sharpe Ratio</option>
              <option value="Min Volatility">Min Volatility</option>
              <option value="Max Profit Factor">Max Profit Factor</option>
            </select>
          </div>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-[10px] text-mutedCustom font-bold uppercase mb-1">Max Iterations</label>
            <input
              type="number"
              className="w-full bg-cardBg border border-borderCustom rounded px-3 py-1.5 focus:outline-none text-white font-mono"
              value={iterations}
              onChange={(e) => setIterations(Number(e.target.value))}
            />
          </div>
          <div>
            <label className="block text-[10px] text-mutedCustom font-bold uppercase mb-1">Validation Mode</label>
            <span className="block text-white mt-1.5">K-Fold TimeSeries Split</span>
          </div>
        </div>

        <div className="flex gap-3 justify-end pt-2">
          <Button variant="secondary" size="sm">Pause</Button>
          <Button variant="primary" size="sm" onClick={onStart}>Start Optimization</Button>
        </div>
      </div>
    </div>
  );
};
export default OptimizationControl;
