"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const RAGAnswer = ({ query }: { query: string }) => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">AI RAG Synthesized Answer</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
        {query ? (
          <div className="space-y-3">
            <div>
              <span className="block text-accentCustom text-[10px] uppercase font-bold mb-1">Response Summary</span>
              <p className="text-white leading-relaxed font-normal">
                Analysis of NVDA Q1 metrics reveals strong margin expansions matching 75% target thresholds. Factor risk metrics indicate minor sector concentration warning triggers.
              </p>
            </div>

            <div className="border-t border-borderCustom pt-3">
              <span className="block text-accentCustom text-[10px] uppercase font-bold mb-1">Citations Sources</span>
              <ul className="space-y-1 font-mono text-[9px] text-mutedCustom uppercase">
                <li>[1] NVIDIA Corp. Q1 Earnings Call Transcript (94% confidence match)</li>
                <li>[2] Apple SEC Form 10-Q filing notes (91% confidence match)</li>
              </ul>
            </div>
          </div>
        ) : (
          <div className="py-6 text-center text-mutedCustom">Awaiting query to synthesize vector context response.</div>
        )}
      </div>
    </div>
  );
};
export default RAGAnswer;
