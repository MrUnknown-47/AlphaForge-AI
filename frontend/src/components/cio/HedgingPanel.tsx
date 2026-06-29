"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { Button } from "../ui/Button";

export const HedgingPanel: React.FC = () => {
  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-2">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Options & Hedging Overlay Engine</h4>
        <Badge variant="info">HEDGING STANDBY</Badge>
      </div>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="flex justify-between items-center pb-2 border-b border-borderCustom border-opacity-40">
          <span>Active Delta Offset Protection:</span>
          <span className="text-white font-mono">-120 Shares offset</span>
        </div>
        <div className="flex justify-between items-center pb-2 border-b border-borderCustom border-opacity-40">
          <span>Protective Put Strike target:</span>
          <span className="text-dangerCustom font-mono">$142.50 (5% OTM)</span>
        </div>
        <div className="flex justify-between items-center">
          <span>Covered Call Strike target:</span>
          <span className="text-successCustom font-mono">$157.50 (5% OTM)</span>
        </div>
      </div>

      <div className="flex justify-end gap-2">
        <Button variant="secondary" size="sm">DEPLOY DELTA NEUTRAL</Button>
        <Button variant="primary" size="sm">DEPLOY ZERO-COST COLLAR</Button>
      </div>
    </div>
  );
};

export default HedgingPanel;
