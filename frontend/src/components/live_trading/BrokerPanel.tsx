"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const BrokerPanel = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Broker Bridge Gateway</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="flex justify-between items-center">
          <span>Active Gateway:</span>
          <Badge variant="success">ALPACA PAPER TRADING</Badge>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div className="border-b border-borderCustom pb-2">
            <span>Available Cash:</span>
            <span className="block text-white font-mono mt-1">$500,000.00</span>
          </div>
          <div className="border-b border-borderCustom pb-2">
            <span>Buying Power (4x Margin):</span>
            <span className="block text-white font-mono mt-1">$2,000,000.00</span>
          </div>
          <div>
            <span>Websocket Latency:</span>
            <span className="block text-accentCustom font-mono mt-1">45ms</span>
          </div>
          <div>
            <span>Shadow Sync Mode:</span>
            <span className="block text-successCustom font-mono mt-1">SYNCHRONIZED</span>
          </div>
        </div>
      </div>
    </div>
  );
};
export default BrokerPanel;
