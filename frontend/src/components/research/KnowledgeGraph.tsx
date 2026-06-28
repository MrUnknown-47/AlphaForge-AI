"use client";

import React from "react";

export const KnowledgeGraph = () => {
  const links = [
    { source: "AAPL", rel: "MEMBER_OF", target: "Tech Sector" },
    { source: "NVDA", rel: "MEMBER_OF", target: "Tech Sector" },
    { source: "Tech Sector", rel: "LEADER_OF", target: "Market Momentum" },
    { source: "XGBoost Model", rel: "PREDICTS", target: "AAPL" }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Institutional Knowledge Graph Relationships</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 text-xs font-semibold text-mutedCustom">
        <div className="space-y-3">
          {links.map((link, idx) => (
            <div key={idx} className="flex justify-between items-center bg-cardBg border border-borderCustom p-2.5 rounded">
              <span className="text-white uppercase">{link.source}</span>
              <span className="text-[10px] uppercase font-bold text-accentCustom">{link.rel}</span>
              <span className="text-white uppercase">{link.target}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
export default KnowledgeGraph;
