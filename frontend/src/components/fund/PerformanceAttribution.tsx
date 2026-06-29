"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid } from "recharts";

const data = [
  { name: "Market", value: 8.2 },
  { name: "Size", value: -1.2 },
  { name: "Value", value: 2.4 },
  { name: "Momentum", value: 4.5 },
  { name: "Alpha", value: 0.6 }
];

export const PerformanceAttribution: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Performance Factor Attribution (annualized)</h4>
        <Badge variant="success">ALPHA GENERATIVE</Badge>
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
            <Bar dataKey="value" fill="#00D4FF" name="Factor Return Contribution %" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default PerformanceAttribution;
