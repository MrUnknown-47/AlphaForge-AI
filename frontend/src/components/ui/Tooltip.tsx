import React from "react";
import clsx from "clsx";

interface TooltipProps {
  content: string;
  children: React.ReactNode;
  className?: string;
}

export const Tooltip: React.FC<TooltipProps> = ({ content, children, className }) => {
  return (
    <div className={clsx("relative group inline-block", className)}>
      {children}
      <div className="absolute z-10 bottom-full left-1/2 transform -translate-x-1/2 mb-2 hidden group-hover:block bg-secondaryBg border border-borderCustom text-white text-[10px] font-medium py-1 px-2 rounded shadow-xl whitespace-nowrap">
        {content}
        <div className="absolute top-full left-1/2 transform -translate-x-1/2 border-width-[5px] border-style-solid border-color-transparent border-t-secondaryBg" />
      </div>
    </div>
  );
};
