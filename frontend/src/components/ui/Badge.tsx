import React from "react";
import clsx from "clsx";

interface BadgeProps {
  variant?: "success" | "danger" | "warning" | "info";
  children: React.ReactNode;
  className?: string;
}

export const Badge: React.FC<BadgeProps> = ({ variant = "info", children, className }) => {
  return (
    <span
      className={clsx(
        "inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-semibold uppercase tracking-wider",
        {
          "bg-successCustom bg-opacity-20 text-successCustom": variant === "success",
          "bg-dangerCustom bg-opacity-20 text-dangerCustom": variant === "danger",
          "bg-warningCustom bg-opacity-20 text-warningCustom": variant === "warning",
          "bg-accentCustom bg-opacity-20 text-accentCustom": variant === "info"
        },
        className
      )}
    >
      {children}
    </span>
  );
};
