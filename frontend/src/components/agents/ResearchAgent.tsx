"use client";

import React, { useState } from "react";
import { Badge } from "../ui/Badge";
import { SearchBar } from "../ui/SearchBar";

export const ResearchAgent: React.FC = () => {
  const [query, setQuery] = useState("");
  const [searching, setSearching] = useState(false);

  const mockCitations = [
    { title: "FOMC Statement on Rate Cuts & Inflation Measures", source: "Federal Reserve Board", type: "MACRO", date: "June 2026" },
    { title: "GPU Architecture Advancements and Blackwell Yield Targets", source: "NVIDIA Corp Research", type: "SECTOR", date: "May 2026" },
    { title: "Cross-sectional Momentum Factor Covariances", source: "Journal of Quantitative Finance", type: "ACADEMIC", date: "2025" }
  ];

  const mockNews = [
    { headline: "NVIDIA suppliers confirm Blackwell shipments rising", source: "Bloomberg", timestamp: "1 hour ago" },
    { headline: "Tech indices slide on inflation print fear", source: "Reuters", timestamp: "3 hours ago" }
  ];

  const handleSearch = (q: string) => {
    setSearching(true);
    setQuery(q);
    setTimeout(() => setSearching(false), 800);
  };

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">RAG Research Desk</h4>
        <span className="text-[10px] text-mutedCustom font-semibold uppercase">Knowledge base</span>
      </div>

      {/* RAG Search Panel */}
      <div className="space-y-2">
        <SearchBar placeholder="Ask AI Knowledge Base..." onSearch={handleSearch} />
        {searching && <span className="text-[10px] text-accentCustom animate-pulse">Running semantic RAG query...</span>}
      </div>

      {/* Research Citations */}
      <div className="space-y-2">
        <span className="text-[10px] text-mutedCustom font-bold uppercase tracking-wider block">Citations & References</span>
        <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-3 space-y-3">
          {mockCitations.map((cit, idx) => (
            <div key={idx} className="text-xs border-b border-borderCustom border-opacity-40 pb-2 last:border-0 last:pb-0">
              <div className="flex justify-between items-start">
                <span className="text-white font-bold block">{cit.title}</span>
                <Badge variant="info">{cit.type}</Badge>
              </div>
              <span className="text-[9px] text-mutedCustom block mt-1">Source: {cit.source} ({cit.date})</span>
            </div>
          ))}
        </div>
      </div>

      {/* News Context */}
      <div className="space-y-2">
        <span className="text-[10px] text-mutedCustom font-bold uppercase tracking-wider block">Realtime News Context</span>
        <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-3 space-y-3">
          {mockNews.map((news, idx) => (
            <div key={idx} className="text-xs border-b border-borderCustom border-opacity-40 pb-2 last:border-0 last:pb-0">
              <span className="text-white font-medium block">{news.headline}</span>
              <span className="text-[9px] text-accentCustom block mt-1">{news.source} • {news.timestamp}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default ResearchAgent;
