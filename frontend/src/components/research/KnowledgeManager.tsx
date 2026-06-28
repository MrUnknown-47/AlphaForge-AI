"use client";

import React from "react";
import { Badge } from "../ui/Badge";
import { Button } from "../ui/Button";

export const KnowledgeManager = () => {
  return (
    <div className="space-y-4">
      <h4 className="text-xs font-bold uppercase tracking-wider text-white">Knowledge Base Index Manager</h4>

      <div className="bg-secondaryBg bg-opacity-20 border border-borderCustom rounded p-4 space-y-4 text-xs font-semibold text-mutedCustom">
        <div className="flex justify-between border-b border-borderCustom pb-2">
          <span>Vector Embeddings:</span>
          <span className="text-white font-mono">1,424 Document Vectors</span>
        </div>
        <div className="flex justify-between border-b border-borderCustom pb-2">
          <span>Knowledge Graph Nodes:</span>
          <span className="text-white font-mono">250 Nodes</span>
        </div>
        <div className="flex justify-between pb-2">
          <span>Vector Database Host:</span>
          <span className="text-successCustom">● CONNECTED (Local sqlite)</span>
        </div>

        <div className="flex justify-end gap-2 pt-2">
          <Button variant="secondary" size="sm">RE-INDEX VECTOR BASE</Button>
        </div>
      </div>
    </div>
  );
};
export default KnowledgeManager;
