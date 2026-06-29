"use client";

import React from "react";
import { ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid } from "recharts";

const data = [
  { ticker: "AAPL", weight: 35.0 },
  { ticker: "NVDA", weight: 28.0 },
  { ticker: "MSFT", weight: 22.0 },
  { ticker: "GOOGL", weight: 15.0 }
];

export const AllocationMatrix: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Target Optimal Allocation Matrix</h4>
        <span className="text-[10px] text-mutedCustom font-semibold uppercase">Total Sum: 100.0%</span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {/* Table */}
        <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
          <table className="w-full text-left text-xs border-collapse">
            <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
              <tr>
                <th className="px-3 py-2">Symbol</th>
                <th className="px-3 py-2 text-right">Optimal Weight</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-borderCustom font-medium">
              {data.map((row) => (
                <tr key={row.ticker} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                  <td className="px-3 py-2 text-white font-bold">{row.ticker}</td>
                  <td className="px-3 py-2 text-right font-mono text-accentCustom">{row.weight.toFixed(1)}%</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* Bar chart representation */}
        <div className="h-40 w-full bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-3">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={data}>
              <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
              <XAxis dataKey="ticker" stroke="#94A3B8" fontSize={9} />
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
              <Bar dataKey="weight" fill="#00D4FF" name="Target Weight %" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
};

export default AllocationMatrix;
