import { create } from "zustand";

interface Message {
  role: "user" | "assistant";
  content: string;
  timestamp: string;
}

interface CopilotState {
  chatHistory: Message[];
  addMessage: (message: Message) => void;
  clearChat: () => void;
}

export const useCopilotStore = create<CopilotState>((set) => ({
  chatHistory: [],
  addMessage: (msg) => set((state) => ({ chatHistory: [...state.chatHistory, msg] })),
  clearChat: () => set({ chatHistory: [] }),
}));
