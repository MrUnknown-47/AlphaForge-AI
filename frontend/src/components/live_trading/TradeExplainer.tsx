"use client";

import React from "react";
import { ProgressBar } from "../ui/ProgressBar";

export const TradeExplainer = ({ ticker }: { ticker: string }) => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Explainability & SHAP Diagnoses: {ticker}</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs">
        <div>
          <span className="block font-bold text-accentCustom uppercase mb-1">Decision Attribution</span>
          <p className="text-mutedCustom leading-relaxed">
            The ensemble model predicts a long expansion signal. Multi-timeframe trend metrics align with macro momentum regimes.
          </p>
        </div>

        <div className="space-y-2 border-t border-borderCustom pt-3">
          <span className="block font-bold text-white uppercase text-[10px] tracking-wider mb-1">SHAP Feature Weights</span>
          
          <div className="space-y-1.5 text-[10px] uppercase text-mutedCustom font-bold">
            <div className="flex justify-between">
              <span>EMA10 / EMA200 crossover</span>
              <span className="text-white">+0.24</span>
            </div>
            <ProgressBar value={70} />
          </div>

          <div className="space-y-1.5 text-[10px] uppercase text-mutedCustom font-bold">
            <div className="flex justify-between">
              <span>VWAP deviation ratio</span>
              <span className="text-white">+0.18</span>
            </div>
            <ProgressBar value={50} />
          </div>

          <div className="space-y-1.5 text-[10px] uppercase text-mutedCustom font-bold">
            <div className="flex justify-between">
              <span>ATR Volatility index level</span>
              <span className="text-white">-0.05</span>
            </div>
            <ProgressBar value={15} />
          </div>
        </div>
      </div>
    </div>
  );
};
export default TradeExplainer;
