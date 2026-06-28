"use client";

import React, { useState } from "react";
import { Button } from "../ui/Button";

export const ResearchCommand = ({ onSearch }: { onSearch: (val: string) => void }) => {
  const [query, setQuery] = useState("");
  const [mode, setMode] = useState("Search");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!query.trim()) return;
    onSearch(query);
  };

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">RAG Deep Research Command Center</h4>

      <form onSubmit={handleSubmit} className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
        <div className="flex gap-2">
          <input
            type="text"
            placeholder="Type research queries (e.g. 'Analyze NVDA Q1 tail risk')..."
            className="flex-1 bg-cardBg border border-borderCustom rounded px-3 py-2 text-white focus:outline-none focus:border-accentCustom"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
          <Button type="submit" variant="primary" size="sm">RESEARCH</Button>
        </div>

        <div className="flex gap-1.5">
          {["Search", "Summarize", "Compare", "Forecast"].map((m) => (
            <button
              key={m}
              type="button"
              onClick={() => setMode(m)}
              className={`px-2 py-0.5 text-[10px] font-bold rounded uppercase tracking-wider border ${
                mode === m
                  ? "bg-accentCustom text-terminal border-accentCustom"
                  : "bg-secondaryBg text-mutedCustom border-borderCustom hover:text-white"
              }`}
            >
              {m}
            </button>
          ))}
        </div>
      </form>
    </div>
  );
};
export default ResearchCommand;
