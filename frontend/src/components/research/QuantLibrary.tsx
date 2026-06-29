"use client";

import React, { useState } from "react";
import { Badge } from "../ui/Badge";
import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ScatterChart,
  Scatter,
  ZAxis
} from "recharts";

const shapData = [
  { feature: "Tech Momentum 10d", shap: 0.42 },
  { feature: "Macro Yield Spread", shap: 0.28 },
  { feature: "VIX Volatility Rank", shap: -0.15 },
  { feature: "Net Asset Allocation", shap: 0.08 },
  { feature: "Daily Drawdown Vol", shap: -0.05 }
];

const clusterData = [
  { x: 1.2, y: 2.3, z: 1, name: "Cluster 1 (KMeans-High Vol)" },
  { x: 1.5, y: 1.8, z: 1, name: "Cluster 1 (KMeans-High Vol)" },
  { x: -0.8, y: -0.5, z: 2, name: "Cluster 2 (KMeans-Low Vol)" },
  { x: -0.5, y: -1.0, z: 2, name: "Cluster 2 (KMeans-Low Vol)" },
  { x: 2.5, y: 0.2, z: 3, name: "DBSCAN Noise/Outliers" }
];

const factorExposure = [
  { factor: "Market Beta", loading: 0.88 },
  { factor: "Momentum", loading: 1.45 },
  { factor: "Value", loading: 0.65 },
  { factor: "Size", loading: 1.10 },
  { factor: "Quality", loading: 1.35 }
];

export const QuantLibrary: React.FC = () => {
  const [activeTab, setActiveTab] = useState<"STATS" | "CLUSTERING" | "EXPOSURE">("STATS");

  return (
    <div className="space-y-4">
      {/* Header Tabs */}
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Quantitative Research Validation Workspace</h4>
        <div className="flex gap-2">
          {["STATS", "CLUSTERING", "EXPOSURE"].map((tab) => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab as any)}
              className={`px-2 py-1 text-[10px] font-bold rounded uppercase tracking-wider transition-colors ${
                activeTab === tab
                  ? "bg-accentCustom bg-opacity-25 text-accentCustom border border-accentCustom"
                  : "text-mutedCustom hover:text-white"
              }`}
            >
              {tab} Profile
            </button>
          ))}
        </div>
      </div>

      {activeTab === "STATS" ? (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs font-semibold text-mutedCustom bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
          <div className="space-y-2 border-r border-borderCustom pr-4">
            <span className="text-[10px] uppercase block tracking-wider text-accentCustom">Stationarity & Normality Tests</span>
            <div className="flex justify-between py-1 border-b border-borderCustom border-opacity-40">
              <span>ADF (Augmented Dickey-Fuller)</span>
              <span className="text-white font-mono">-4.12 (p-value: 0.001)</span>
            </div>
            <div className="flex justify-between py-1 border-b border-borderCustom border-opacity-40">
              <span>KPSS Test</span>
              <span className="text-white font-mono">0.32 (Critical: 0.46)</span>
            </div>
            <div className="flex justify-between py-1">
              <span>Jarque-Bera (Normality)</span>
              <span className="text-white font-mono">142.5 (p-value: &lt; 0.001)</span>
            </div>
          </div>
          <div className="space-y-2 pl-2">
            <span className="text-[10px] uppercase block tracking-wider text-accentCustom">Memory & Regime Diagnostics</span>
            <div className="flex justify-between py-1 border-b border-borderCustom border-opacity-40">
              <span>Hurst Exponent</span>
              <span className="text-successCustom font-mono">0.68 (Trending)</span>
            </div>
            <div className="flex justify-between py-1 border-b border-borderCustom border-opacity-40">
              <span>Regime Detection State</span>
              <span className="text-white font-mono">Markov Regime: Low Vol Expansion</span>
            </div>
            <div className="flex justify-between py-1">
              <span>Regime Shift Prob</span>
              <span className="text-white font-mono">12.4%</span>
            </div>
          </div>
        </div>
      ) : activeTab === "CLUSTERING" ? (
        <div className="space-y-4">
          {/* Clustering plots description */}
          <div className="grid grid-cols-2 gap-4 text-xs font-semibold text-mutedCustom bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
            <div>
              <span className="text-[10px] uppercase block tracking-wider">KMeans Clustering Profiles</span>
              <span className="block text-white font-mono mt-1">k=4 (Silhouette Score: 0.62)</span>
            </div>
            <div>
              <span className="text-[10px] uppercase block tracking-wider">DBSCAN Profiles</span>
              <span className="block text-white font-mono mt-1">eps=0.5, min_samples=5 (Noise Pct: 4.8%)</span>
            </div>
          </div>

          <div className="h-56 w-full bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
            <ResponsiveContainer width="100%" height="100%">
              <ScatterChart>
                <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
                <XAxis type="number" dataKey="x" name="Dimension 1 (PCA)" stroke="#94A3B8" fontSize={9} />
                <YAxis type="number" dataKey="y" name="Dimension 2 (PCA)" stroke="#94A3B8" fontSize={9} />
                <ZAxis type="number" dataKey="z" range={[60, 400]} />
                <Tooltip
                  cursor={{ strokeDasharray: "3 3" }}
                  contentStyle={{
                    backgroundColor: "#111827",
                    borderColor: "#1F2937",
                    borderRadius: "4px",
                    fontSize: "10px",
                    color: "#FFFFFF"
                  }}
                />
                <Scatter name="KMeans & DBSCAN Clusters" data={clusterData} fill="#00D4FF" />
              </ScatterChart>
            </ResponsiveContainer>
          </div>
        </div>
      ) : (
        <div className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {/* Factor Exposures */}
            <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-2">
              <span className="text-[10px] uppercase block tracking-wider text-mutedCustom">Factor Exposure Loadings</span>
              <div className="space-y-1.5 text-xs font-semibold">
                {factorExposure.map((f) => (
                  <div key={f.factor} className="flex justify-between border-b border-borderCustom border-opacity-40 pb-1 last:border-0">
                    <span>{f.factor}</span>
                    <span className="text-white font-mono">{f.loading.toFixed(2)}</span>
                  </div>
                ))}
              </div>
            </div>

            {/* SHAP attributions */}
            <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-2">
              <span className="text-[10px] uppercase block tracking-wider text-mutedCustom">SHAP Feature Attributions</span>
              <div className="h-32 w-full">
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={shapData} layout="vertical">
                    <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
                    <XAxis type="number" stroke="#94A3B8" fontSize={8} />
                    <YAxis dataKey="feature" type="category" stroke="#94A3B8" fontSize={8} width={75} />
                    <Tooltip
                      contentStyle={{
                        backgroundColor: "#111827",
                        borderColor: "#1F2937",
                        borderRadius: "4px",
                        fontSize: "9px",
                        color: "#FFFFFF"
                      }}
                    />
                    <Bar dataKey="shap" fill="#10B981" name="SHAP attribution" />
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </div>
          </div>

          {/* Correlation matrix */}
          <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-2 text-xs font-semibold">
            <span className="text-[10px] uppercase block tracking-wider text-mutedCustom">Feature Correlation Heatmap</span>
            <div className="grid grid-cols-4 gap-1 text-[10px] text-center font-bold font-mono text-white">
              <div className="bg-black bg-opacity-40 p-2">Tech Mom (1.00)</div>
              <div className="bg-black bg-opacity-40 p-2 text-accentCustom">Yield Spread (0.62)</div>
              <div className="bg-black bg-opacity-40 p-2 text-warningCustom">Vol Rank (-0.45)</div>
              <div className="bg-black bg-opacity-40 p-2 text-successCustom">SHAP Weight (0.75)</div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default QuantLibrary;
