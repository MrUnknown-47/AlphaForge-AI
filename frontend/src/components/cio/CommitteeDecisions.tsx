"use client";

import React from "react";
import { Badge } from "../ui/Badge";

const votes = [
  { agent: "Macro Agent", vote: "BUY", score: 0.82 },
  { agent: "Technical Agent", vote: "BUY", score: 0.78 },
  { agent: "Risk Agent", vote: "HOLD", score: 0.85 },
  { agent: "Derivatives Agent", vote: "HOLD", score: 0.69 }
];

export const CommitteeDecisions: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">CIO Committee Allocation Decisions</h4>
        <Badge variant="success">CONSENSUS BUY</Badge>
      </div>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Committee Member</th>
              <th className="px-3 py-2.5">Vote Action</th>
              <th className="px-3 py-2.5 text-right">Confidence Score</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {votes.map((v) => (
              <tr key={v.agent} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-bold">{v.agent}</td>
                <td className="px-3 py-2.5">
                  <Badge variant={v.vote === "BUY" ? "success" : "info"}>
                    {v.vote}
                  </Badge>
                </td>
                <td className="px-3 py-2.5 text-right font-mono text-accentCustom">{v.score.toFixed(2)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default CommitteeDecisions;
