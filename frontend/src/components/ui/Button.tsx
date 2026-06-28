import React from "react";
import clsx from "clsx";

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary" | "danger" | "ghost";
  size?: "sm" | "md" | "lg";
}

export const Button: React.FC<ButtonProps> = ({
  children,
  variant = "primary",
  size = "md",
  className,
  ...props
}) => {
  return (
    <button
      className={clsx(
        "rounded font-semibold transition-colors duration-150 focus:outline-none focus:ring-2 focus:ring-offset-2",
        {
          "bg-accentCustom text-terminal hover:bg-opacity-90": variant === "primary",
          "bg-secondaryBg text-white border border-borderCustom hover:bg-opacity-80": variant === "secondary",
          "bg-dangerCustom text-white hover:bg-opacity-90": variant === "danger",
          "bg-transparent text-white hover:bg-borderCustom": variant === "ghost",
          "px-3 py-1 text-xs": size === "sm",
          "px-4 py-2 text-sm": size === "md",
          "px-6 py-3 text-base": size === "lg",
        },
        className
      )}
      {...props}
    >
      {children}
    </button>
  );
};
