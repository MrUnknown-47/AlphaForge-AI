"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const ExecutiveControlTower = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Executive Control Tower</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="flex justify-between border-b border-borderCustom pb-2">
          <span>SOFTWARE_COMPLETE:</span>
          <Badge variant="success">TRUE</Badge>
        </div>
        <div className="flex justify-between border-b border-borderCustom pb-2">
          <span>ENGINEERING_COMPLETE:</span>
          <Badge variant="success">TRUE</Badge>
        </div>
        <div className="flex justify-between border-b border-borderCustom pb-2">
          <span>VALIDATION_RUNNING:</span>
          <Badge variant="success">TRUE</Badge>
        </div>
        <div className="flex justify-between border-b border-borderCustom pb-2">
          <span>READY_FOR_REAL_CAPITAL:</span>
          <Badge variant="danger">FALSE</Badge>
        </div>
        <div className="flex justify-between pb-2">
          <span>REQUIRES_90_DAY_SHADOW:</span>
          <Badge variant="warning">TRUE</Badge>
        </div>
      </div>
    </div>
  );
};
export default ExecutiveControlTower;
