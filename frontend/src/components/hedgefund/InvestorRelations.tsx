"use client";

import React from "react";
import { Button } from "../ui/Button";

export const InvestorRelations = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Investor Relations & reporting center</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <p className="leading-relaxed">
          Generate standard factsheets, investor briefings, and monthly tear sheets for institutional partners.
        </p>

        <div className="flex gap-2">
          <Button variant="secondary" size="sm">Generate Factsheet</Button>
          <Button variant="secondary" size="sm">Download Monthly Report</Button>
        </div>
      </div>
    </div>
  );
};
export default InvestorRelations;
