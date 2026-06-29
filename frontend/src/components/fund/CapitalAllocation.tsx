"use client";

import React, { useState } from "react";
import { Badge } from "../ui/Badge";
import { ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid } from "recharts";

const data = [
  { name: "Quant Equity", weight: 40 },
  { name: "CTA Trend", weight: 30 },
  { name: "Global Macro", weight: 30 }
];

export const CapitalAllocation: React.FC = () => {
  const [method, setMethod] = useState<"ERC" | "HRP" | "KELLY" | "BLACK_LITTERMAN">("ERC");

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Strategy Capital Allocation Optimizer</h4>
        <Badge variant="info">SOLVER: {method}</Badge>
      </div>

      <div className="grid grid-cols-4 gap-2">
        {["ERC", "HRP", "KELLY", "BLACK_LITTERMAN"].map((m) => (
          <button
            key={m}
            onClick={() => setMethod(m as any)}
            className={`px-2 py-1.5 rounded text-[8px] font-bold uppercase tracking-wider transition-colors border ${
              method === m
                ? "bg-accentCustom bg-opacity-25 border-accentCustom text-accentCustom"
                : "bg-secondaryBg border-borderCustom text-mutedCustom hover:text-white"
            }`}
          >
            {m.replace("_", " ")}
          </button>
        ))}
      </div>

      <div className="h-40 w-full bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-3">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
            <XAxis dataKey="name" stroke="#94A3B8" fontSize={9} />
            <YAxis stroke="#94A3B8" fontSize={9} />
            <Tooltip
              contentStyle={{
                backgroundColor: "#111827",
                borderColor: "#1F2937",
                borderRadius: "4px",
                fontSize: "10px",
                color: "#FFFFFF"
              }}
            />
            <Bar dataKey="weight" fill="#10B981" name="Allocated Weight %" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default CapitalAllocation;
