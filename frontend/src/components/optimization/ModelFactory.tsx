"use client";

import React from "react";
import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";

const lossHistory = [
  { epoch: 10, train: 0.85, validation: 0.88 },
  { epoch: 20, train: 0.62, validation: 0.65 },
  { epoch: 30, train: 0.45, validation: 0.49 },
  { epoch: 40, train: 0.32, validation: 0.38 },
  { epoch: 50, train: 0.21, validation: 0.29 }
];

export const ModelFactory = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Loss Convergence Curve (Transformer vs XGBoost)</h4>

      <div className="h-48 w-full bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={lossHistory}>
            <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
            <XAxis dataKey="epoch" stroke="#94A3B8" fontSize={10} name="Epochs" />
            <YAxis stroke="#94A3B8" fontSize={10} domain={[0, 1]} name="Loss" />
            <Tooltip
              contentStyle={{
                backgroundColor: "#111827",
                borderColor: "#1F2937",
                borderRadius: "4px",
                fontSize: "10px",
                color: "#FFFFFF"
              }}
            />
            <Line type="monotone" dataKey="train" name="Training Loss" stroke="#10B981" strokeWidth={1.5} dot={false} />
            <Line type="monotone" dataKey="validation" name="Validation Loss" stroke="#EF4444" strokeWidth={1.5} dot={false} />
          </LineChart>
        </ResponsiveContainer>
      </div>

      <div className="grid grid-cols-3 gap-2 text-[10px] text-mutedCustom uppercase font-bold text-center border border-borderCustom rounded p-3 bg-cardBg">
        <div>
          <span>Selected Model:</span>
          <span className="block text-white font-mono mt-0.5">XGBoost+LSTM</span>
        </div>
        <div>
          <span>Epochs Limit:</span>
          <span className="block text-white font-mono mt-0.5">50 Epochs</span>
        </div>
        <div>
          <span>Early Stop:</span>
          <span className="block text-successCustom font-mono mt-0.5">TRUE (EP 42)</span>
        </div>
      </div>
    </div>
  );
};
export default ModelFactory;
