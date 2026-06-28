import { create } from "zustand";

interface Order {
  id: string;
  ticker: string;
  side: "BUY" | "SELL";
  quantity: number;
  price?: number;
  type: "MARKET" | "LIMIT";
  status: "PENDING" | "FILLED" | "CANCELLED";
  timestamp: string;
}

interface TradingState {
  orders: Order[];
  setOrders: (orders: Order[]) => void;
  addOrder: (order: Order) => void;
}

export const useTradingStore = create<TradingState>((set) => ({
  orders: [],
  setOrders: (orders) => set({ orders }),
  addOrder: (order) => set((state) => ({ orders: [order, ...state.orders] })),
}));
