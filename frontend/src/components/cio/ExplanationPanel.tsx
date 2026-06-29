"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const ExplanationPanel: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">CIO Decision Explainability Rationale</h4>
        <span className="text-[10px] text-mutedCustom font-semibold uppercase">SHAP Attribution</span>
      </div>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-3 text-xs leading-relaxed text-mutedCustom">
        <div>
          <span className="text-[10px] font-bold text-accentCustom uppercase block">Portfolio Rationale:</span>
          <p className="text-white mt-0.5">Allocations optimized via MVO regularized using shrinkage. Regime detected as: BULL.</p>
        </div>
        
        <div className="border-t border-borderCustom border-opacity-40 pt-2">
          <span className="text-[10px] font-bold text-accentCustom uppercase block">Risk Rationale:</span>
          <p className="text-white mt-0.5">Position sizes limited under 25% single-asset caps to bound tracking error.</p>
        </div>

        <div className="border-t border-borderCustom border-opacity-40 pt-2">
          <span className="text-[10px] font-bold text-accentCustom uppercase block">Macro Rationale:</span>
          <p className="text-white mt-0.5">GS10 treasury yield cycles indicate asset class accumulation phase holds optimal support.</p>
        </div>
      </div>
    </div>
  );
};

export default ExplanationPanel;
