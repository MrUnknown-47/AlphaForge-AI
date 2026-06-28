import React from "react";
import clsx from "clsx";
import { Button } from "./Button";

interface DrawerProps {
  isOpen: boolean;
  onClose: () => void;
  title: string;
  children: React.ReactNode;
}

export const Drawer: React.FC<DrawerProps> = ({ isOpen, onClose, title, children }) => {
  return (
    <div
      className={clsx("fixed inset-0 z-50 overflow-hidden transition-opacity duration-300", {
        "pointer-events-auto opacity-100": isOpen,
        "pointer-events-none opacity-0": !isOpen
      })}
    >
      <div className="absolute inset-0 bg-black bg-opacity-75" onClick={onClose} />
      <div
        className={clsx(
          "absolute right-0 top-0 bottom-0 w-full max-w-md bg-cardBg border-l border-borderCustom p-6 shadow-2xl transition-transform duration-300 transform",
          {
            "translate-x-0": isOpen,
            "translate-x-full": !isOpen
          }
        )}
      >
        <div className="flex items-center justify-between mb-4 border-b border-borderCustom pb-3">
          <h3 className="text-lg font-bold text-white">{title}</h3>
          <Button variant="ghost" size="sm" onClick={onClose} className="text-mutedCustom hover:text-white">
            ✕
          </Button>
        </div>
        <div className="text-sm text-white overflow-y-auto h-[calc(100vh-120px)]">{children}</div>
      </div>
    </div>
  );
};
