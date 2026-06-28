"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { Button } from "../ui/Button";

interface Agent {
  name: string;
  status: "ACTIVE" | "IDLE" | "OFFLINE";
  latency: number;
  tokens: string;
  cost: string;
}

const initialAgents: Agent[] = [
  { name: "Chief Investment Officer", status: "ACTIVE", latency: 120, tokens: "4.5K", cost: "$0.09" },
  { name: "Portfolio Manager", status: "ACTIVE", latency: 95, tokens: "8.2K", cost: "$0.16" },
  { name: "Macro Research", status: "ACTIVE", latency: 150, tokens: "12.4K", cost: "$0.25" },
  { name: "Quant Analyst", status: "ACTIVE", latency: 110, tokens: "6.8K", cost: "$0.14" },
  { name: "Risk Manager", status: "ACTIVE", latency: 85, tokens: "3.2K", cost: "$0.06" }
];

export const AgentControlCenter = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Multi-Agent Analyst Team Controller</h4>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Agent Role</th>
              <th className="px-3 py-2.5">Status</th>
              <th className="px-3 py-2.5">Latency</th>
              <th className="px-3 py-2.5">Token usage</th>
              <th className="px-3 py-2.5">Cost</th>
              <th className="px-3 py-2.5">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {initialAgents.map((agent) => (
              <tr key={agent.name} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-bold">{agent.name} Agent</td>
                <td className="px-3 py-2.5">
                  <Badge variant={agent.status === "ACTIVE" ? "success" : "warning"}>{agent.status}</Badge>
                </td>
                <td className="px-3 py-2.5 font-mono text-accentCustom">{agent.latency}ms</td>
                <td className="px-3 py-2.5 font-mono text-white">{agent.tokens}</td>
                <td className="px-3 py-2.5 font-mono text-successCustom">{agent.cost}</td>
                <td className="px-3 py-2.5">
                  <div className="flex gap-1.5">
                    <Button variant="ghost" size="sm">Inspect</Button>
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
export default AgentControlCenter;
