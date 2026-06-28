import React from "react";
import clsx from "clsx";

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  title?: string;
  subtitle?: string;
}

export const Card: React.FC<CardProps> = ({ children, title, subtitle, className, ...props }) => {
  return (
    <div
      className={clsx(
        "rounded bg-cardBg border border-borderCustom p-5 shadow-lg transition-shadow duration-150",
        className
      )}
      {...props}
    >
      {title && (
        <div className="mb-4">
          <h3 className="text-lg font-semibold text-white">{title}</h3>
          {subtitle && <p className="text-xs text-mutedCustom mt-1">{subtitle}</p>}
        </div>
      )}
      {children}
    </div>
  );
};
