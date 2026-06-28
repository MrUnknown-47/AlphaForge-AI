"use client";

import React from "react";

export const ExperimentGraph = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Quant Experiment Strategy Lineage Tree</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 text-xs font-semibold text-mutedCustom">
        <div className="space-y-3">
          <div className="flex items-center gap-2">
            <span className="text-accentCustom font-bold">[Parent Strategy]</span>
            <span className="text-white">AlphaForge Base Model v1.0.0</span>
          </div>
          <div className="pl-6 border-l border-borderCustom space-y-3">
            <div className="flex items-center gap-2">
              <span className="text-successCustom">└── [Derived]</span>
              <span className="text-white">Optuna HPO Learning Rate Run (EXP_401)</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="text-successCustom">└── [Derived]</span>
              <span className="text-white">Genetic Evolution Fitness Run (EXP_402)</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
export default ExperimentGraph;
