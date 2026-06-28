"use client";

import React, { useState } from "react";
import {
  ResponsiveContainer,
  ComposedChart,
  Line,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Legend
} from "recharts";

const chartData = [
  { name: "09:30", price: 180.00, high: 181.20, low: 179.80, vwap: 180.20, volume: 120000 },
  { name: "10:00", price: 181.50, high: 182.00, low: 180.50, vwap: 181.10, volume: 150000 },
  { name: "10:30", price: 182.10, high: 182.80, low: 181.30, vwap: 181.80, volume: 90000 },
  { name: "11:00", price: 181.20, high: 182.30, low: 180.80, vwap: 181.70, volume: 110000 },
  { name: "11:30", price: 182.50, high: 183.00, low: 181.00, vwap: 182.10, volume: 130000 }
];

export const TradingChart = ({ ticker }: { ticker: string }) => {
  const [timeframe, setTimeframe] = useState("5m");

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">
          TradingView Interactive Chart: <span className="text-accentCustom">{ticker}</span>
        </h4>
        <div className="flex gap-1">
          {["1m", "5m", "15m", "1h", "1d"].map((tf) => (
            <button
              key={tf}
              onClick={() => setTimeframe(tf)}
              className={`px-1.5 py-0.5 text-[10px] font-bold rounded uppercase tracking-wider border ${
                timeframe === tf
                  ? "bg-accentCustom text-terminal border-accentCustom"
                  : "bg-secondaryBg text-mutedCustom border-borderCustom hover:text-white"
              }`}
            >
              {tf}
            </button>
          ))}
        </div>
      </div>

      <div className="h-64 w-full bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
        <ResponsiveContainer width="100%" height="100%">
          <ComposedChart data={chartData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
            <XAxis dataKey="name" stroke="#94A3B8" fontSize={10} />
            <YAxis stroke="#94A3B8" fontSize={10} domain={["auto", "auto"]} />
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
            <Line
              type="monotone"
              dataKey="price"
              name={`${ticker} Price`}
              stroke="#00D4FF"
              strokeWidth={2}
              dot={false}
            />
            <Line
              type="monotone"
              dataKey="vwap"
              name="VWAP (Intraday)"
              stroke="#F59E0B"
              strokeWidth={1}
              strokeDasharray="3 3"
              dot={false}
            />
            <Bar dataKey="volume" name="Volume" fill="#1F2937" yAxisId="right" opacity={0.25} />
          </ComposedChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};
export default TradingChart;
