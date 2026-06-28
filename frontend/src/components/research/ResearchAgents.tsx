"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const ResearchAgents = () => {
  const agents = [
    { name: "Macro Research", role: "MACRO", latency: 120, cost: "$0.09" },
    { name: "Quant Research", role: "FACTOR ANALYSIS", latency: 95, cost: "$0.12" },
    { name: "Risk Manager", role: "TAIL RISK LIMITS", latency: 82, cost: "$0.06" }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">AI Research Agent Team</h4>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Agent Role</th>
              <th className="px-3 py-2.5">Scope</th>
              <th className="px-3 py-2.5">Latency</th>
              <th className="px-3 py-2.5">Cost</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {agents.map((row) => (
              <tr key={row.name} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-bold">{row.name} Agent</td>
                <td className="px-3 py-2.5 text-mutedCustom uppercase text-[10px]">{row.role}</td>
                <td className="px-3 py-2.5 font-mono text-accentCustom">{row.latency}ms</td>
                <td className="px-3 py-2.5 font-mono text-successCustom">{row.cost}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
export default ResearchAgents;
