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

const generationData = [
  { gen: 1, max_fitness: 1.15, avg_fitness: 0.85 },
  { gen: 5, max_fitness: 1.34, avg_fitness: 1.05 },
  { gen: 10, max_fitness: 1.56, avg_fitness: 1.22 },
  { gen: 15, max_fitness: 1.78, avg_fitness: 1.45 },
  { gen: 20, max_fitness: 1.85, avg_fitness: 1.62 }
];

export const EvolutionaryLab = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Genetic Algorithm Fitness Landscaping</h4>

      <div className="h-48 w-full bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={generationData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
            <XAxis dataKey="gen" stroke="#94A3B8" fontSize={10} name="Generations" />
            <YAxis stroke="#94A3B8" fontSize={10} domain={["auto", "auto"]} name="Fitness" />
            <Tooltip
              contentStyle={{
                backgroundColor: "#111827",
                borderColor: "#1F2937",
                borderRadius: "4px",
                fontSize: "10px",
                color: "#FFFFFF"
              }}
            />
            <Line type="monotone" dataKey="max_fitness" name="Max Fitness (Sharpe)" stroke="#00D4FF" strokeWidth={2} dot={false} />
            <Line type="monotone" dataKey="avg_fitness" name="Average Fitness" stroke="#94A3B8" strokeWidth={1} dot={false} />
          </LineChart>
        </ResponsiveContainer>
      </div>

      <div className="grid grid-cols-3 gap-2 text-[10px] text-mutedCustom uppercase font-bold text-center border border-borderCustom rounded p-3 bg-cardBg">
        <div>
          <span>Crossover Rate:</span>
          <span className="block text-white font-mono mt-0.5">80%</span>
        </div>
        <div>
          <span>Mutation Probability:</span>
          <span className="block text-white font-mono mt-0.5">5%</span>
        </div>
        <div>
          <span>Generations Limit:</span>
          <span className="block text-successCustom font-mono mt-0.5">20 Gens</span>
        </div>
      </div>
    </div>
  );
};
export default EvolutionaryLab;
