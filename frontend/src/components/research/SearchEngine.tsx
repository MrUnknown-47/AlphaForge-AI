"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const SearchEngine = ({ query }: { query: string }) => {
  const mockResults = [
    { title: "NVIDIA Corp. Q1 2026 Earnings Call Transcript", type: "EARNINGS", score: 94 },
    { title: "SEC Form 10-Q Apple Inc. (Quarterly report Mar 2026)", type: "SEC FILING", score: 91 }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Multi-Source Retrieval results</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        {query ? (
          <div className="space-y-3">
            <span className="block text-[10px] text-mutedCustom uppercase">Search query: &quot;{query}&quot;</span>
            {mockResults.map((row, idx) => (
              <div key={idx} className="flex justify-between items-start border-b border-borderCustom pb-3 last:border-0 last:pb-0">
                <div className="space-y-1">
                  <div className="flex items-center gap-2">
                    <Badge variant="info">{row.type}</Badge>
                    <span className="text-white font-medium">{row.title}</span>
                  </div>
                </div>
                <span className="text-[10px] text-accentCustom font-bold">{row.score}% Match</span>
              </div>
            ))}
          </div>
        ) : (
          <div className="py-6 text-center text-mutedCustom">Enter a research query above to index vector embeddings database.</div>
        )}
      </div>
    </div>
  );
};
export default SearchEngine;
