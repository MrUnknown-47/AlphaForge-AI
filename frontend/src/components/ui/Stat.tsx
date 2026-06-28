import React from "react";
import clsx from "clsx";

interface StatProps {
  label: string;
  value: string | number;
  subValue?: string;
  className?: string;
}

export const Stat: React.FC<StatProps> = ({ label, value, subValue, className }) => {
  return (
    <div className={clsx("flex flex-col p-4 bg-cardBg border border-borderCustom rounded", className)}>
      <span className="text-[10px] uppercase tracking-wider font-semibold text-mutedCustom">{label}</span>
      <span className="text-xl font-bold text-white mt-1 tracking-tight">{value}</span>
      {subValue && <span className="text-[10px] text-mutedCustom mt-1">{subValue}</span>}
    </div>
  );
};
