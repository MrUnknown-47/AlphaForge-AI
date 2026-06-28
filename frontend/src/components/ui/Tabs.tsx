import React from "react";
import clsx from "clsx";

interface TabItem {
  id: string;
  label: string;
}

interface TabsProps {
  tabs: TabItem[];
  activeTab: string;
  onChange: (tabId: string) => void;
  className?: string;
}

export const Tabs: React.FC<TabsProps> = ({ tabs, activeTab, onChange, className }) => {
  return (
    <div className={clsx("flex border-b border-borderCustom bg-secondaryBg bg-opacity-20 px-2 rounded-t", className)}>
      {tabs.map((tab) => {
        const isActive = tab.id === activeTab;
        return (
          <button
            key={tab.id}
            onClick={() => onChange(tab.id)}
            className={clsx(
              "px-4 py-2.5 text-xs font-semibold uppercase tracking-wider transition-colors focus:outline-none border-b-2 -mb-px",
              {
                "border-accentCustom text-accentCustom": isActive,
                "border-transparent text-mutedCustom hover:text-white": !isActive
              }
            )}
          >
            {tab.label}
          </button>
        );
      })}
    </div>
  );
};
