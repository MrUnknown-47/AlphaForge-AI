import React from "react";
import clsx from "clsx";

interface SearchBarProps extends React.InputHTMLAttributes<HTMLInputElement> {
  onSearch?: (val: string) => void;
}

export const SearchBar: React.FC<SearchBarProps> = ({ onSearch, className, ...props }) => {
  return (
    <div className={clsx("relative w-full max-w-sm", className)}>
      <input
        type="text"
        className="w-full bg-secondaryBg text-white placeholder-mutedCustom border border-borderCustom rounded px-3 py-1.5 pl-8 text-sm focus:outline-none focus:border-accentCustom focus:ring-1 focus:ring-accentCustom transition-colors"
        onChange={(e) => onSearch && onSearch(e.target.value)}
        {...props}
      />
      <span className="absolute left-2.5 top-2 text-xs text-mutedCustom pointer-events-none">🔍</span>
    </div>
  );
};
