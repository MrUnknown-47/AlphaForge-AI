import React from "react";
import clsx from "clsx";

interface AlertProps {
  variant?: "success" | "danger" | "warning" | "info";
  title: string;
  description?: string;
  className?: string;
}

export const Alert: React.FC<AlertProps> = ({ variant = "info", title, description, className }) => {
  return (
    <div
      className={clsx(
        "rounded border-l-4 p-4 bg-cardBg shadow-md",
        {
          "border-successCustom bg-successCustom bg-opacity-5": variant === "success",
          "border-dangerCustom bg-dangerCustom bg-opacity-5": variant === "danger",
          "border-warningCustom bg-warningCustom bg-opacity-5": variant === "warning",
          "border-accentCustom bg-accentCustom bg-opacity-5": variant === "info"
        },
        className
      )}
    >
      <div className="flex flex-col gap-1">
        <h4
          className={clsx("text-sm font-bold", {
            "text-successCustom": variant === "success",
            "text-dangerCustom": variant === "danger",
            "text-warningCustom": variant === "warning",
            "text-accentCustom": variant === "info"
          })}
        >
          {title}
        </h4>
        {description && <p className="text-xs text-mutedCustom">{description}</p>}
      </div>
    </div>
  );
};
