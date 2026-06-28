"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const CapitalProtection = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Capital Protection status</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="flex justify-between border-b border-borderCustom pb-2">
          <span>TRADING_HALTED:</span>
          <Badge variant="danger">FALSE</Badge>
        </div>
        <div className="flex justify-between pb-2">
          <span>SAFE_TO_DEPLOY:</span>
          <Badge variant="warning">FALSE (Requires 90-Day Shadow)</Badge>
        </div>
      </div>
    </div>
  );
};
export default CapitalProtection;
