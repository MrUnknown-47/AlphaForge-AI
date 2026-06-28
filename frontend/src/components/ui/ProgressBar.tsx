import React from "react";
import clsx from "clsx";

interface ProgressBarProps {
  value: number; // percentage 0 - 100
  max?: number;
  className?: string;
}

export const ProgressBar: React.FC<ProgressBarProps> = ({ value, max = 100, className }) => {
  const percentage = Math.min(100, Math.max(0, (value / max) * 100));

  return (
    <div className={clsx("w-full bg-secondaryBg h-2.5 rounded-full overflow-hidden border border-borderCustom", className)}>
      <div
        className="bg-accentCustom h-full rounded-full transition-all duration-300"
        style={{ width: `${percentage}%` }}
      />
    </div>
  );
};
