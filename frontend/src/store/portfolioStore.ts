import { create } from "zustand";

interface Position {
  ticker: string;
  quantity: number;
  entry_price: number;
  market_value: number;
  unrealized_pnl: number;
}

interface PortfolioState {
  cash: number;
  portfolioValue: number;
  buyingPower: number;
  exposurePct: number;
  dailyReturn: number;
  positions: Position[];
  setPortfolioData: (data: Partial<PortfolioState>) => void;
}

export const usePortfolioStore = create<PortfolioState>((set) => ({
  cash: 100000.0,
  portfolioValue: 100000.0,
  buyingPower: 100000.0,
  exposurePct: 0.0,
  dailyReturn: 0.0,
  positions: [],
  setPortfolioData: (data) => set((state) => ({ ...state, ...data })),
}));
