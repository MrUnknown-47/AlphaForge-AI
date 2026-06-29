"use client";

import React from "react";
import { Badge } from "../ui/Badge";

const committees = [
  { name: "Investment Committee", decision: "APPROVED", details: "BUY 40% Weight in US Growth" },
  { name: "Risk Committee", decision: "APPROVED", details: "Leverage cap set at 2.5x" },
  { name: "Execution Committee", decision: "APPROVED", details: "Limit execution latency under 12ms" },
  { name: "Governance Committee", decision: "APPROVED", details: "Zero surveillance alarms triggered" }
];

export const CommitteeBoard: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Hedge Fund Governance Committee Board</h4>
        <Badge variant="success">ALL SYSTEMS GO</Badge>
      </div>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Committee Panel</th>
              <th className="px-3 py-2.5">Status</th>
              <th className="px-3 py-2.5 text-right">Governing Resolution</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {committees.map((c) => (
              <tr key={c.name} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-bold">{c.name}</td>
                <td className="px-3 py-2.5">
                  <Badge variant="success">{c.decision}</Badge>
                </td>
                <td className="px-3 py-2.5 text-right text-mutedCustom">{c.details}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default CommitteeBoard;
