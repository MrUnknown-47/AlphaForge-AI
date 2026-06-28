import React from "react";
import clsx from "clsx";

interface LoadingScreenProps {
  message?: string;
  className?: string;
}

export const LoadingScreen: React.FC<LoadingScreenProps> = ({ message = "Synthesizing AlphaForge terminal UI...", className }) => {
  return (
    <div className={clsx("fixed inset-0 z-50 flex flex-col items-center justify-center bg-terminal bg-opacity-95", className)}>
      <div className="relative w-12 h-12">
        <div className="absolute inset-0 rounded-full border-4 border-secondaryBg" />
        <div className="absolute inset-0 rounded-full border-4 border-accentCustom border-t-transparent animate-spin" />
      </div>
      <p className="mt-4 text-xs font-semibold text-mutedCustom tracking-wider uppercase">{message}</p>
    </div>
  );
};
export default LoadingScreen;
