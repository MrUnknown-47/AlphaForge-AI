"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { Button } from "../ui/Button";

interface Agent {
  name: string;
  health: "HEALTHY" | "DEGRADED" | "CRITICAL";
  latency: number;
  memory: string;
  cost: string;
}

const activeAgents: Agent[] = [
  { name: "CIO Agent", health: "HEALTHY", latency: 120, memory: "128MB", cost: "$0.09" },
  { name: "Quant Agent", health: "HEALTHY", latency: 95, memory: "256MB", cost: "$0.12" },
  { name: "Market Agent", health: "HEALTHY", latency: 142, memory: "192MB", cost: "$0.15" },
  { name: "Risk Agent", health: "HEALTHY", latency: 85, memory: "64MB", cost: "$0.06" }
];

export const AgentCommandCenter = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Autonomous Agent Orchestra Command</h4>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Agent Instance</th>
              <th className="px-3 py-2.5">Health</th>
              <th className="px-3 py-2.5">Latency</th>
              <th className="px-3 py-2.5">Memory Usage</th>
              <th className="px-3 py-2.5">Daily Cost</th>
              <th className="px-3 py-2.5">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {activeAgents.map((agent) => (
              <tr key={agent.name} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-bold">{agent.name}</td>
                <td className="px-3 py-2.5">
                  <Badge variant="success">{agent.health}</Badge>
                </td>
                <td className="px-3 py-2.5 font-mono text-accentCustom">{agent.latency}ms</td>
                <td className="px-3 py-2.5 font-mono text-white">{agent.memory}</td>
                <td className="px-3 py-2.5 font-mono text-successCustom">{agent.cost}</td>
                <td className="px-3 py-2.5">
                  <div className="flex gap-1.5">
                    <Button variant="ghost" size="sm">Pause</Button>
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
export default AgentCommandCenter;
