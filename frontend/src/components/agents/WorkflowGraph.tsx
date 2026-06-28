"use client";

import React from "react";

export const WorkflowGraph = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Multi-Agent Workflow DAG Dependencies</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 text-xs font-semibold text-mutedCustom">
        <div className="space-y-3">
          <div className="flex items-center gap-2">
            <span className="text-accentCustom font-bold">[Trigger Event]</span>
            <span className="text-white">Earnings call transcript parsed</span>
          </div>
          <div className="pl-6 border-l border-borderCustom space-y-3">
            <div className="flex items-center gap-2">
              <span className="text-successCustom">└── [Dependency]</span>
              <span className="text-white">Sentiment Agent scores inputs</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="text-successCustom">└── [Dependency]</span>
              <span className="text-white">Quant Agent discovered factors</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
export default WorkflowGraph;
