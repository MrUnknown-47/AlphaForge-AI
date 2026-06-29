"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const RiskAgent: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Risk Agent Card</h4>
        <Badge variant="warning">HEDGE</Badge>
      </div>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-3 text-xs font-semibold text-mutedCustom">
        <div className="grid grid-cols-2 gap-4">
          <div>
            <span className="text-[10px] uppercase block tracking-wider">Confidence</span>
            <span className="block text-white font-mono mt-0.5">88%</span>
          </div>
          <div>
            <span className="text-[10px] uppercase block tracking-wider">Score</span>
            <span className="block text-accentCustom font-mono mt-0.5">8.8 / 10</span>
          </div>
        </div>

        <div className="border-t border-borderCustom pt-2">
          <span className="text-[10px] uppercase block tracking-wider mb-1">Reasoning</span>
          <p className="text-white font-normal text-[11px] leading-relaxed">
            Overall portfolio beta (0.88) remains aligned but high tech sector concentrations trigger hedge alerts. Index puts should be loaded as tail hedge protection.
          </p>
        </div>
      </div>
    </div>
  );
};

export default RiskAgent;
