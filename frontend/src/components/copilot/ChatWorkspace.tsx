"use client";

import React, { useState } from "react";
import { Button } from "../ui/Button";

interface Message {
  sender: string;
  text: string;
  time: string;
}

export const ChatWorkspace = () => {
  const [messages, setMessages] = useState<Message[]>([
    { sender: "CIO Agent", text: "Portfolio beta currently matches target 0.88. Allocating to tech momentum remains high conviction.", time: "10 mins ago" },
    { sender: "Risk Manager Agent", text: "Confirming exposure limits. Drawdown stands at 1.05%, well under the 20% guardrails.", time: "8 mins ago" }
  ]);
  const [input, setInput] = useState("");

  const handleSend = (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;
    setMessages([
      ...messages,
      { sender: "User (Quant)", text: input, time: "Just now" }
    ]);
    setInput("");
  };

  return (
    <div className="space-y-4 flex flex-col h-96 bg-cardBg border border-borderCustom rounded overflow-hidden p-4">
      <div className="flex justify-between items-center border-b border-borderCustom pb-3">
        <h4 className="text-xs font-bold uppercase tracking-wider text-white">Interactive Research Workspace Chat</h4>
        <Badge variant="info">Analyst Mode: ACTIVE</Badge>
      </div>

      <div className="flex-1 overflow-y-auto space-y-3 text-xs pr-2">
        {messages.map((msg, idx) => (
          <div key={idx} className="bg-secondaryBg bg-opacity-20 border border-borderCustom p-3 rounded space-y-1">
            <div className="flex justify-between font-bold">
              <span className="text-accentCustom uppercase">{msg.sender}</span>
              <span className="text-[10px] text-mutedCustom">{msg.time}</span>
            </div>
            <p className="text-white leading-relaxed">{msg.text}</p>
          </div>
        ))}
      </div>

      <form onSubmit={handleSend} className="flex gap-2 border-t border-borderCustom pt-3">
        <input
          type="text"
          placeholder="Ask copilot team (e.g. 'explain AAPL model SHAP scores')..."
          className="flex-1 bg-secondaryBg border border-borderCustom text-white placeholder-mutedCustom px-3 py-1.5 text-xs rounded focus:outline-none focus:border-accentCustom"
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <Button type="submit" variant="primary" size="sm">SEND</Button>
      </form>
    </div>
  );
};
import { Badge } from "../ui/Badge";
export default ChatWorkspace;
