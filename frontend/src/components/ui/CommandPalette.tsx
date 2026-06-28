import React, { useState, useEffect } from "react";
import clsx from "clsx";

interface CommandOption {
  category: string;
  label: string;
  action: () => void;
}

interface CommandPaletteProps {
  isOpen: boolean;
  onClose: () => void;
  options: CommandOption[];
}

export const CommandPalette: React.FC<CommandPaletteProps> = ({ isOpen, onClose, options }) => {
  const [search, setSearch] = useState("");

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "k" && (e.metaKey || e.ctrlKey)) {
        e.preventDefault();
        if (isOpen) onClose();
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  const filtered = options.filter(
    (opt) =>
      opt.label.toLowerCase().includes(search.toLowerCase()) ||
      opt.category.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center bg-black bg-opacity-75 p-4 pt-20">
      <div className="w-full max-w-lg bg-cardBg border border-borderCustom rounded-lg shadow-2xl overflow-hidden">
        <input
          type="text"
          placeholder="Search commands (e.g. 'execute trade')..."
          className="w-full bg-secondaryBg border-b border-borderCustom text-white placeholder-mutedCustom px-4 py-3 text-sm focus:outline-none"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          autoFocus
        />
        <div className="max-h-60 overflow-y-auto divide-y divide-borderCustom text-sm">
          {filtered.length === 0 ? (
            <div className="px-4 py-3 text-mutedCustom text-center">No commands found.</div>
          ) : (
            filtered.map((opt, idx) => (
              <button
                key={idx}
                onClick={() => {
                  opt.action();
                  onClose();
                }}
                className="w-full text-left px-4 py-2.5 hover:bg-secondaryBg hover:bg-opacity-50 text-white flex justify-between items-center transition-colors"
              >
                <span>{opt.label}</span>
                <span className="text-[10px] uppercase font-semibold text-mutedCustom bg-secondaryBg px-2 py-0.5 rounded border border-borderCustom">
                  {opt.category}
                </span>
              </button>
            ))
          )}
        </div>
      </div>
    </div>
  );
};
