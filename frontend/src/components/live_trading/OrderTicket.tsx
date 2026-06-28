"use client";

import React, { useState } from "react";
import { Button } from "../ui/Button";

export const OrderTicket = ({
  ticker,
  onPlaceOrder
}: {
  ticker: string;
  onPlaceOrder: (side: "BUY" | "SELL", qty: number, price: number) => void;
}) => {
  const [qty, setQty] = useState(10);
  const [price, setPrice] = useState(182.50);
  const [type, setType] = useState("LIMIT");
  const [stopLoss, setStopLoss] = useState(174.60);
  const [takeProfit, setTakeProfit] = useState(198.00);

  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Execution Ticket</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs">
        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-[10px] text-mutedCustom font-bold uppercase mb-1">Ticker</label>
            <input
              type="text"
              className="w-full bg-cardBg border border-borderCustom rounded px-3 py-1.5 font-bold focus:outline-none"
              value={ticker}
              readOnly
            />
          </div>
          <div>
            <label className="block text-[10px] text-mutedCustom font-bold uppercase mb-1">Order Type</label>
            <select
              className="w-full bg-cardBg border border-borderCustom rounded px-3 py-1.5 focus:outline-none text-white font-bold"
              value={type}
              onChange={(e) => setType(e.target.value)}
            >
              <option value="MARKET">MARKET</option>
              <option value="LIMIT">LIMIT</option>
              <option value="STOP">STOP</option>
              <option value="BRACKET">BRACKET</option>
            </select>
          </div>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-[10px] text-mutedCustom font-bold uppercase mb-1">Quantity</label>
            <input
              type="number"
              className="w-full bg-cardBg border border-borderCustom rounded px-3 py-1.5 focus:outline-none text-white font-mono"
              value={qty}
              onChange={(e) => setQty(Number(e.target.value))}
            />
          </div>
          <div>
            <label className="block text-[10px] text-mutedCustom font-bold uppercase mb-1">Limit Price</label>
            <input
              type="number"
              step={0.01}
              className="w-full bg-cardBg border border-borderCustom rounded px-3 py-1.5 focus:outline-none text-white font-mono"
              value={price}
              onChange={(e) => setPrice(Number(e.target.value))}
            />
          </div>
        </div>

        {type === "BRACKET" && (
          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-[10px] text-mutedCustom font-bold uppercase mb-1">Stop Loss</label>
              <input
                type="number"
                step={0.01}
                className="w-full bg-cardBg border border-borderCustom rounded px-3 py-1.5 focus:outline-none text-white font-mono"
                value={stopLoss}
                onChange={(e) => setStopLoss(Number(e.target.value))}
              />
            </div>
            <div>
              <label className="block text-[10px] text-mutedCustom font-bold uppercase mb-1">Take Profit</label>
              <input
                type="number"
                step={0.01}
                className="w-full bg-cardBg border border-borderCustom rounded px-3 py-1.5 focus:outline-none text-white font-mono"
                value={takeProfit}
                onChange={(e) => setTakeProfit(Number(e.target.value))}
              />
            </div>
          </div>
        )}

        <div className="border-t border-borderCustom pt-3 space-y-2 text-[10px] text-mutedCustom font-semibold uppercase">
          <div className="flex justify-between">
            <span>Estimated Fees:</span>
            <span className="text-white">$0.00 (Zero Fee Paper)</span>
          </div>
          <div className="flex justify-between">
            <span>Exposure Allocation:</span>
            <span className="text-accentCustom font-mono">${(qty * price).toLocaleString()}</span>
          </div>
        </div>

        <div className="grid grid-cols-2 gap-3">
          <Button
            variant="primary"
            className="w-full bg-successCustom hover:bg-opacity-90 text-white font-bold"
            onClick={() => onPlaceOrder("BUY", qty, price)}
          >
            BUY / LONG
          </Button>
          <Button
            variant="danger"
            className="w-full bg-dangerCustom hover:bg-opacity-90 text-white font-bold"
            onClick={() => onPlaceOrder("SELL", qty, price)}
          >
            SELL / SHORT
          </Button>
        </div>
      </div>
    </div>
  );
};
export default OrderTicket;
