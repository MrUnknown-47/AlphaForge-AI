"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { ResponsiveContainer, PieChart, Pie, Cell, Tooltip, Legend } from "recharts";

const data = [
  { name: "Equities", value: 40, color: "#00D4FF" },
  { name: "Options", value: 10, color: "#3B82F6" },
  { name: "Futures", value: 15, color: "#10B981" },
  { name: "Forex", value: 10, color: "#F59E0B" },
  { name: "Crypto", value: 5, color: "#EF4444" },
  { name: "Bonds", value: 15, color: "#8B5CF6" },
  { name: "Commodities", value: 5, color: "#EC4899" }
];

export const MacroAllocation: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Cross-Asset Macro Portfolio Allocation</h4>
        <Badge variant="success">OPTIMAL RATIOS</Badge>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {/* Pie chart */}
        <div className="h-44 w-full bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-3 flex justify-center items-center">
          <ResponsiveContainer width="100%" height="100%">
            <PieChart>
              <Pie
                data={data}
                cx="50%"
                cy="50%"
                innerRadius={35}
                outerRadius={55}
                paddingAngle={2}
                dataKey="value"
              >
                {data.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.color} />
                ))}
              </Pie>
              <Tooltip
                contentStyle={{
                  backgroundColor: "#111827",
                  borderColor: "#1F2937",
                  borderRadius: "4px",
                  fontSize: "10px",
                  color: "#FFFFFF"
                }}
              />
            </PieChart>
          </ResponsiveContainer>
        </div>

        {/* Legend listing weights */}
        <div className="p-3 border border-borderCustom rounded bg-cardBg text-xs space-y-1.5 overflow-y-auto max-h-44">
          {data.map((d) => (
            <div key={d.name} className="flex justify-between items-center">
              <div className="flex items-center gap-2">
                <span className="w-2.5 h-2.5 rounded-full" style={{ backgroundColor: d.color }} />
                <span className="text-white font-semibold">{d.name}</span>
              </div>
              <span className="font-mono text-accentCustom">{d.value.toFixed(1)}%</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default MacroAllocation;
