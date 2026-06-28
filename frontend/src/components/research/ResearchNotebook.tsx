"use client";

import React, { useState } from "react";
import { Button } from "../ui/Button";

export const ResearchNotebook = () => {
  const [note, setNote] = useState("# NVDA Earnings Study\n- Strong growth momentum\n- Suggest hedging tail-risk using index puts.");

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Quant Research Notebook</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
        <textarea
          className="w-full h-32 bg-cardBg border border-borderCustom rounded p-3 text-white focus:outline-none font-mono text-[11px]"
          value={note}
          onChange={(e) => setNote(e.target.value)}
        />
        <div className="flex justify-end">
          <Button variant="secondary" size="sm">EXPORT NOTEBOOK</Button>
        </div>
      </div>
    </div>
  );
};
export default ResearchNotebook;
