"use client";

import React from "react";
import { Badge } from "../ui/Badge";

export const WalkForwardPanel = () => {
  const splits = [
    { window: "WFO Split 1 (2020-2021)", train: "PASS", val: "PASS", test: "PASS", sharpe: 1.82 },
    { window: "WFO Split 2 (2021-2022)", train: "PASS", val: "PASS", test: "PASS", sharpe: 1.74 },
    { window: "WFO Split 3 (2022-2023)", train: "PASS", val: "PASS", test: "PASS", sharpe: 1.88 }
  ];

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Walk Forward Optimization (WFO) splits</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold">
        <div className="flex justify-between items-center text-xs font-bold text-mutedCustom border-b border-borderCustom pb-2 uppercase">
          <span>Split Target Window</span>
          <div className="flex gap-12 font-mono text-[10px]">
            <span>Status</span>
            <span>Test Sharpe</span>
          </div>
        </div>

        <div className="space-y-3">
          {splits.map((row) => (
            <div key={row.window} className="flex justify-between items-center">
              <span className="text-white uppercase">{row.window}</span>
              <div className="flex items-center gap-12 font-mono text-[10px]">
                <Badge variant="success">{row.train}</Badge>
                <span className="text-accentCustom font-bold">{row.sharpe.toFixed(2)}</span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
export default WalkForwardPanel;
