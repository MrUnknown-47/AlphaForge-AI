"use client";

import React from "react";
import { Badge } from "../ui/Badge";

interface PortfolioBook {
  book: string;
  capital: string;
  returns: string;
  sharpe: number;
  capacity: string;
}

const books: PortfolioBook[] = [
  { book: "Long Short Equities", capital: "$5.0M", returns: "+18.42%", sharpe: 1.85, capacity: "$50M" },
  { book: "Statistical Arbitrage", capital: "$3.0M", returns: "+12.14%", sharpe: 2.14, capacity: "$20M" },
  { book: "Macro & Currencies", capital: "$2.0M", returns: "+6.85%", sharpe: 1.42, capacity: "$100M" }
];

export const PortfolioManager = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Multi-Portfolio Sub-Book Allocations</h4>

      <div className="overflow-x-auto border border-borderCustom rounded bg-cardBg">
        <table className="w-full text-left text-xs border-collapse">
          <thead className="bg-secondaryBg border-b border-borderCustom text-[10px] text-mutedCustom uppercase tracking-wider">
            <tr>
              <th className="px-3 py-2.5">Sub-Book Portfolio</th>
              <th className="px-3 py-2.5">Allocated Capital</th>
              <th className="px-3 py-2.5">YTD Return</th>
              <th className="px-3 py-2.5">Sharpe</th>
              <th className="px-3 py-2.5">Capacity Limit</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-borderCustom font-medium">
            {books.map((row) => (
              <tr key={row.book} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                <td className="px-3 py-2.5 text-white font-bold">{row.book}</td>
                <td className="px-3 py-2.5 font-mono text-white">{row.capital}</td>
                <td className="px-3 py-2.5 font-mono text-successCustom">{row.returns}</td>
                <td className="px-3 py-2.5 font-mono text-accentCustom">{row.sharpe.toFixed(2)}</td>
                <td className="px-3 py-2.5 font-mono text-white">{row.capacity}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
export default PortfolioManager;
