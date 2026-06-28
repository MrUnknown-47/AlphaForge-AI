import React from "react";
import clsx from "clsx";
import { Button } from "./Button";

interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  title: string;
  children: React.ReactNode;
}

export const Modal: React.FC<ModalProps> = ({ isOpen, onClose, title, children }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-75 p-4 animate-fade-in">
      <div className="relative w-full max-w-lg rounded-lg border border-borderCustom bg-cardBg p-6 shadow-2xl">
        <div className="flex items-center justify-between mb-4 border-b border-borderCustom pb-3">
          <h3 className="text-lg font-bold text-white">{title}</h3>
          <Button variant="ghost" size="sm" onClick={onClose} className="text-mutedCustom hover:text-white">
            ✕
          </Button>
        </div>
        <div className="text-sm text-white">{children}</div>
      </div>
    </div>
  );
};
