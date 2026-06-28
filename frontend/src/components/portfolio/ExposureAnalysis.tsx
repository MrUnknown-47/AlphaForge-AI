"use client";

import React from "react";
import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";

const exposureData = [
  { name: "Technology", Long: 84.2, Short: 0, Net: 84.2 },
  { name: "Automotive", Long: 15.8, Short: 0, Net: 15.8 },
  { name: "Indices", Long: 10.0, Short: -12.5, Net: -2.5 }
];

export const ExposureAnalysis = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Sector & Net Factor Exposures</h4>

      <div className="h-60 w-full bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={exposureData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
            <XAxis dataKey="name" stroke="#94A3B8" fontSize={10} />
            <YAxis stroke="#94A3B8" fontSize={10} />
            <Tooltip
              contentStyle={{
                backgroundColor: "#111827",
                borderColor: "#1F2937",
                borderRadius: "4px",
                fontSize: "10px",
                color: "#FFFFFF"
              }}
            />
            <Bar dataKey="Long" fill="#10B981" name="Long Exposure %" />
            <Bar dataKey="Short" fill="#EF4444" name="Short Exposure %" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};
export default ExposureAnalysis;
