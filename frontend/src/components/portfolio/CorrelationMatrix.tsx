"use client";

import React from "react";

const tickers = ["AAPL", "MSFT", "NVDA", "GOOGL", "SPY"];
const matrix: Record<string, Record<string, number>> = {
  AAPL: { AAPL: 1.0, MSFT: 0.72, NVDA: 0.54, GOOGL: 0.65, SPY: 0.85 },
  MSFT: { AAPL: 0.72, MSFT: 1.0, NVDA: 0.58, GOOGL: 0.75, SPY: 0.88 },
  NVDA: { AAPL: 0.54, MSFT: 0.58, NVDA: 1.0, GOOGL: 0.51, SPY: 0.72 },
  GOOGL: { AAPL: 0.65, MSFT: 0.75, NVDA: 0.51, GOOGL: 1.0, SPY: 0.81 },
  SPY: { AAPL: 0.85, MSFT: 0.88, NVDA: 0.72, GOOGL: 0.81, SPY: 1.0 }
};

export const CorrelationMatrix = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Asset Correlation Heatmap Matrix</h4>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg p-4">
        <div className="min-w-[400px]">
          <div className="grid grid-cols-6 gap-1 text-[10px] text-center font-bold text-mutedCustom uppercase pb-2">
            <div></div>
            {tickers.map((t) => <div key={t}>{t}</div>)}
          </div>

          <div className="space-y-1">
            {tickers.map((row) => (
              <div key={row} className="grid grid-cols-6 gap-1 items-center text-xs font-semibold text-center">
                <div className="text-left font-bold text-white uppercase">{row}</div>
                {tickers.map((col) => {
                  const val = matrix[row][col];
                  return (
                    <div
                      key={col}
                      className="py-2.5 rounded font-mono text-[10px]"
                      style={{
                        backgroundColor: `rgba(0, 212, 255, ${val})`,
                        color: val > 0.6 ? "#070B14" : "#FFFFFF"
                      }}
                    >
                      {val.toFixed(2)}
                    </div>
                  );
                })}
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
export default CorrelationMatrix;
