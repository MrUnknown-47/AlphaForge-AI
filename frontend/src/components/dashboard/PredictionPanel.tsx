"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { ProgressBar } from "../ui/ProgressBar";

interface Prediction {
  ticker: string;
  xgboost: number;
  lstm: number;
  ensemble: number;
  confidence: number;
  action: "BUY" | "SELL" | "HOLD";
}

const mockPredictions: Prediction[] = [
  { ticker: "AAPL", xgboost: 0.75, lstm: 0.65, ensemble: 0.72, confidence: 82, action: "BUY" },
  { ticker: "MSFT", xgboost: -0.12, lstm: -0.32, ensemble: -0.18, confidence: 71, action: "SELL" },
  { ticker: "TSLA", xgboost: 0.15, lstm: 0.05, ensemble: 0.12, confidence: 65, action: "HOLD" },
  { ticker: "NVDA", xgboost: 0.88, lstm: 0.92, ensemble: 0.89, confidence: 91, action: "BUY" }
];

export const PredictionPanel = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">XGBoost & LSTM Prediction Signals</h4>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {mockPredictions.map((pred) => (
          <div key={pred.ticker} className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-3">
            <div className="flex justify-between items-center">
              <span className="text-sm font-bold text-white">{pred.ticker}</span>
              <Badge variant={pred.action === "BUY" ? "success" : pred.action === "SELL" ? "danger" : "warning"}>
                {pred.action}
              </Badge>
            </div>

            <div className="grid grid-cols-3 gap-2 text-[10px] text-mutedCustom font-semibold uppercase">
              <div>
                <span>XGBoost</span>
                <span className="block text-white font-mono mt-0.5">{(pred.xgboost * 100).toFixed(0)}%</span>
              </div>
              <div>
                <span>LSTM</span>
                <span className="block text-white font-mono mt-0.5">{(pred.lstm * 100).toFixed(0)}%</span>
              </div>
              <div>
                <span>Ensemble</span>
                <span className="block text-accentCustom font-mono mt-0.5">{(pred.ensemble * 100).toFixed(0)}%</span>
              </div>
            </div>

            <div className="space-y-1">
              <div className="flex justify-between text-[10px] uppercase font-bold text-mutedCustom">
                <span>Signal Confidence</span>
                <span className="text-white font-mono">{pred.confidence}%</span>
              </div>
              <ProgressBar value={pred.confidence} />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
export default PredictionPanel;
