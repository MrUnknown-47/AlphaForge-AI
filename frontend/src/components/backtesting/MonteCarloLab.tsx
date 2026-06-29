"use client";

import React from "react";
import {
  ResponsiveContainer,
  AreaChart,
  Area,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Legend
} from "recharts";

const simulations = [
  { step: "0d", p10: 1000000, p30: 1000000, p50: 1000000, p70: 1000000, p90: 1000000 },
  { step: "10d", p10: 975000, p30: 990000, p50: 1010000, p70: 1025000, p90: 1045000 },
  { step: "20d", p10: 955000, p30: 980000, p50: 1030000, p70: 1055000, p90: 1090000 },
  { step: "30d", p10: 940000, p30: 975000, p50: 1045000, p70: 1080000, p90: 1140000 },
  { step: "40d", p10: 925000, p30: 965000, p50: 1060000, p70: 1110000, p90: 1195000 }
];

export const MonteCarloLab: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Monte Carlo Fan Chart (1000 Iterations)</h4>
        <span className="text-[10px] text-mutedCustom font-semibold uppercase">Confidence bands</span>
      </div>

      <div className="h-56 w-full bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={simulations}>
            <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
            <XAxis dataKey="step" stroke="#94A3B8" fontSize={9} />
            <YAxis stroke="#94A3B8" fontSize={9} domain={["auto", "auto"]} />
            <Tooltip
              contentStyle={{
                backgroundColor: "#111827",
                borderColor: "#1F2937",
                borderRadius: "4px",
                fontSize: "10px",
                color: "#FFFFFF"
              }}
            />
            <Legend verticalAlign="top" height={36} wrapperStyle={{ fontSize: "10px" }} />
            
            {/* Area bands representing probability distributions */}
            <Area type="monotone" dataKey="p90" stroke="#10B981" fill="#10B981" fillOpacity={0.05} name="90th Percentile" />
            <Area type="monotone" dataKey="p70" stroke="#00D4FF" fill="#00D4FF" fillOpacity={0.1} name="70th Percentile" />
            <Area type="monotone" dataKey="p50" stroke="#F59E0B" fill="#F59E0B" fillOpacity={0.15} name="50th Percentile (Median)" />
            <Area type="monotone" dataKey="p30" stroke="#94A3B8" fill="#94A3B8" fillOpacity={0.1} name="30th Percentile" />
            <Area type="monotone" dataKey="p10" stroke="#EF4444" fill="#EF4444" fillOpacity={0.05} name="10th Percentile" />
          </AreaChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default MonteCarloLab;
