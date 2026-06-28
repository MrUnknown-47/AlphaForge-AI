import React from "react";
import clsx from "clsx";

interface EmptyStateProps {
  title: string;
  description: string;
  icon?: string;
  className?: string;
}

export const EmptyState: React.FC<EmptyStateProps> = ({ title, description, icon = "🔍", className }) => {
  return (
    <div className={clsx("flex flex-col items-center justify-center p-8 bg-cardBg border border-borderCustom border-dashed rounded text-center", className)}>
      <span className="text-4xl mb-3">{icon}</span>
      <h4 className="text-sm font-bold text-white uppercase tracking-wider">{title}</h4>
      <p className="text-xs text-mutedCustom mt-1 max-w-xs">{description}</p>
    </div>
  );
};
