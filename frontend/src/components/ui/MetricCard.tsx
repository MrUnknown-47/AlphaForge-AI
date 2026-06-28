import React from "react";
import clsx from "clsx";
import { Card } from "./Card";

interface MetricCardProps {
  label: string;
  value: string | number;
  delta?: number;
  prefix?: string;
  suffix?: string;
  className?: string;
}

export const MetricCard: React.FC<MetricCardProps> = ({
  label,
  value,
  delta,
  prefix,
  suffix,
  className
}) => {
  const isPositive = delta !== undefined && delta >= 0;

  return (
    <Card className={clsx("flex flex-col justify-between min-w-[200px]", className)}>
      <div>
        <p className="text-xs font-semibold text-mutedCustom tracking-wider uppercase">{label}</p>
        <div className="flex items-baseline mt-2 gap-1">
          {prefix && <span className="text-sm font-semibold text-mutedCustom">{prefix}</span>}
          <span className="text-2xl font-bold text-white tracking-tight">{value}</span>
          {suffix && <span className="text-sm font-semibold text-mutedCustom">{suffix}</span>}
        </div>
      </div>
      {delta !== undefined && (
        <div className="mt-3 flex items-center gap-1">
          <span
            className={clsx("text-xs font-semibold px-2 py-0.5 rounded", {
              "bg-successCustom bg-opacity-20 text-successCustom": isPositive,
              "bg-dangerCustom bg-opacity-20 text-dangerCustom": !isPositive
            })}
          >
            {isPositive ? "+" : ""}
            {delta.toFixed(2)}%
          </span>
          <span className="text-[10px] text-mutedCustom">vs last session</span>
        </div>
      )}
    </Card>
  );
};
