"use client";

import React, { useState } from "react";
import { Badge } from "../ui/Badge";
import { Button } from "../ui/Button";

interface Incident {
  id: string;
  title: string;
  severity: "P0" | "P1" | "P2";
  status: "OPEN" | "ACKNOWLEDGED" | "RESOLVED" | "ESCALATED";
  age: string;
}

const mockIncidents: Incident[] = [
  { id: "inc_001", title: "ML prediction worker divergence", severity: "P1", status: "OPEN", age: "5 mins ago" },
  { id: "inc_002", title: "Websocket subscription connection jitter", severity: "P2", status: "ACKNOWLEDGED", age: "12 mins ago" }
];

export const IncidentCenter: React.FC = () => {
  const [incidents, setIncidents] = useState<Incident[]>(mockIncidents);

  const handleAction = (id: string, action: "ACK" | "ESCALATE" | "RESOLVE") => {
    setIncidents((prev) =>
      prev.map((inc) => {
        if (inc.id !== id) return inc;
        let newStatus = inc.status;
        if (action === "ACK") newStatus = "ACKNOWLEDGED";
        if (action === "ESCALATE") newStatus = "ESCALATED";
        if (action === "RESOLVE") newStatus = "RESOLVED";
        return { ...inc, status: newStatus };
      })
    );
  };

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">NOC Operational Incidents Command</h4>
        <span className="text-[10px] text-mutedCustom font-semibold uppercase">Active: {incidents.filter(i => i.status !== "RESOLVED").length}</span>
      </div>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Incident ID</th>
              <th className="px-3 py-2.5">Title</th>
              <th className="px-3 py-2.5">Severity</th>
              <th className="px-3 py-2.5">Status</th>
              <th className="px-3 py-2.5">Age</th>
              <th className="px-3 py-2.5 text-right">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {incidents.map((inc) => (
              <tr key={inc.id} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-mono">{inc.id}</td>
                <td className="px-3 py-2.5 text-white font-semibold">{inc.title}</td>
                <td className="px-3 py-2.5">
                  <Badge variant={inc.severity === "P0" ? "danger" : inc.severity === "P1" ? "warning" : "info"}>
                    {inc.severity}
                  </Badge>
                </td>
                <td className="px-3 py-2.5 font-mono">
                  <Badge variant={inc.status === "RESOLVED" ? "success" : inc.status === "OPEN" ? "danger" : "warning"}>
                    {inc.status}
                  </Badge>
                </td>
                <td className="px-3 py-2.5 text-mutedCustom font-mono">{inc.age}</td>
                <td className="px-3 py-2.5 text-right">
                  <div className="flex gap-1.5 justify-end">
                    <Button variant="secondary" size="sm" onClick={() => handleAction(inc.id, "ACK")}>
                      ACK
                    </Button>
                    <Button variant="danger" size="sm" onClick={() => handleAction(inc.id, "ESCALATE")}>
                      ESCALATE
                    </Button>
                    <Button variant="primary" size="sm" onClick={() => handleAction(inc.id, "RESOLVE")}>
                      RESOLVE
                    </Button>
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

export default IncidentCenter;
