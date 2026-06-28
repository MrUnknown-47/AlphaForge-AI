"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const RAGResearch = () => {
  const sources = [
    { title: "NVIDIA Corp. Q1 Earnings Call Transcript", type: "EARNINGS", confidence: 94 },
    { title: "SEC Form 10-Q Apple Inc. (Quarter ended Mar 2026)", type: "SEC FILINGS", confidence: 91 }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">RAG Citations Search Terminal</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4">
        {sources.map((src, idx) => (
          <div key={idx} className="flex justify-between items-start text-xs border-b border-borderCustom pb-3 last:border-0 last:pb-0">
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <Badge variant="info">{src.type}</Badge>
                <span className="text-white font-medium">{src.title}</span>
              </div>
            </div>
            <span className="text-[10px] text-accentCustom font-bold">{src.confidence}% Match</span>
          </div>
        ))}
      </div>
    </div>
  );
};
export default RAGResearch;
