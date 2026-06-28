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

const rewardHistory = [
  { episode: 10, reward: -150, loss: 0.85 },
  { episode: 20, reward: -80, loss: 0.62 },
  { episode: 30, reward: 20, loss: 0.45 },
  { episode: 40, reward: 85, loss: 0.32 },
  { episode: 50, reward: 142, loss: 0.21 }
];

export const RLLab = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Proximal Policy Optimization (PPO) Rewards</h4>

      <div className="h-48 w-full bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={rewardHistory}>
            <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
            <XAxis dataKey="episode" stroke="#94A3B8" fontSize={10} name="Episodes" />
            <YAxis stroke="#94A3B8" fontSize={10} domain={["auto", "auto"]} name="Episode Reward" />
            <Tooltip
              contentStyle={{
                backgroundColor: "#111827",
                borderColor: "#1F2937",
                borderRadius: "4px",
                fontSize: "10px",
                color: "#FFFFFF"
              }}
            />
            <Line type="monotone" dataKey="reward" name="Average Reward" stroke="#10B981" strokeWidth={2} dot={false} />
          </LineChart>
        </ResponsiveContainer>
      </div>

      <div className="grid grid-cols-2 gap-4 text-xs font-semibold text-mutedCustom uppercase font-mono border-t border-borderCustom pt-2">
        <div>
          <span>Policy Loss Target:</span>
          <span className="block text-white font-bold mt-0.5">0.0142</span>
        </div>
        <div>
          <span>Discount Factor (Gamma):</span>
          <span className="block text-white font-bold mt-0.5">0.99</span>
        </div>
      </div>
    </div>
  );
};
export default RLLab;
