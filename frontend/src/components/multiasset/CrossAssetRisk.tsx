"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid } from "recharts";

const riskData = [
  { name: "VaR 95%", value: 5.4 },
  { name: "Cross Gamma", value: 0.12 },
  { name: "Cross Vega", value: 0.45 },
  { name: "Duration (yrs)", value: 4.8 },
  { name: "Convexity", value: 0.24 }
];

export const CrossAssetRisk: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Cross-Asset Risk Metrics & Correlation</h4>
        <Badge variant="info">PORTFOLIO VALUE AT RISK</Badge>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {/* Risk parameters bar chart */}
        <div className="h-44 w-full bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-3">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={riskData}>
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
              <Bar dataKey="value" fill="#FF5E62" name="Risk Metrics" />
            </BarChart>
          </ResponsiveContainer>
        </div>

        {/* Matrix display */}
        <div className="p-4 bg-secondaryBg bg-opacity-20 border border-borderCustom rounded text-xs font-semibold text-mutedCustom space-y-2">
          <span className="text-[10px] text-accentCustom font-bold uppercase">Cross Asset Correlation Matrix</span>
          <div className="flex justify-between border-b border-borderCustom border-opacity-40 pb-1">
            <span>EQUITY-BOND:</span>
            <span className="text-white font-mono">-0.15</span>
          </div>
          <div className="flex justify-between border-b border-borderCustom border-opacity-40 pb-1">
            <span>EQUITY-CRYPTO:</span>
            <span className="text-white font-mono">0.62</span>
          </div>
          <div className="flex justify-between border-b border-borderCustom border-opacity-40 pb-1">
            <span>BOND-CRYPTO:</span>
            <span className="text-white font-mono">-0.22</span>
          </div>
          <div className="flex justify-between pt-1">
            <span>Contagion Spreads risk:</span>
            <span className="text-successCustom font-mono">MODERATE</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CrossAssetRisk;
