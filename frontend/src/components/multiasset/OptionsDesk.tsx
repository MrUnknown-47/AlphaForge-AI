"use client";

import React, { useState } from "react";
import { Badge } from "../ui/Badge";
import { Button } from "../ui/Button";

const strategies = [
  "Long Call", "Long Put", "Covered Call", "Cash Secured Put",
  "Vertical Spread", "Iron Condor", "Straddle", "Strangle", "Collar", "Protective Put"
];

export const OptionsDesk: React.FC = () => {
  const [selectedStrat, setSelectedStrat] = useState("Iron Condor");

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Derivatives Options Strategy Desk</h4>
        <Badge variant="success">OPRA FEED LIVE</Badge>
      </div>

      <div className="grid grid-cols-2 md:grid-cols-5 gap-2">
        {strategies.map((strat) => (
          <button
            key={strat}
            onClick={() => setSelectedStrat(strat)}
            className={`px-2 py-1.5 rounded text-[9px] font-bold uppercase tracking-wider transition-colors border ${
              selectedStrat === strat
                ? "bg-accentCustom bg-opacity-25 border-accentCustom text-accentCustom"
                : "bg-secondaryBg border-borderCustom text-mutedCustom hover:text-white"
            }`}
          >
            {strat}
          </button>
        ))}
      </div>

      <div className="p-4 bg-secondaryBg bg-opacity-20 border border-borderCustom rounded space-y-3 text-xs">
        <div className="flex justify-between items-center">
          <span className="font-bold text-white">Active Strategy Setup:</span>
          <Badge variant="info">{selectedStrat}</Badge>
        </div>

        <div className="grid grid-cols-2 gap-4 font-semibold text-mutedCustom pt-2 border-t border-borderCustom border-opacity-40">
          <div>
            <span>Max Profit:</span>
            <span className="block text-successCustom font-mono mt-1">$450.00</span>
          </div>
          <div>
            <span>Max Loss:</span>
            <span className="block text-dangerCustom font-mono mt-1">$550.00</span>
          </div>
        </div>
      </div>

      <div className="flex justify-end pt-1">
        <Button variant="primary" size="sm">TRANSMIT OPTIONS ORDER</Button>
      </div>
    </div>
  );
};

export default OptionsDesk;
