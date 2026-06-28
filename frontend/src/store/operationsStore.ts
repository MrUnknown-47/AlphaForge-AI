import { create } from "zustand";

interface OperationsState {
  uptimePct: number;
  brokerLatencyMs: number;
  dbConnected: boolean;
  brokerConnected: boolean;
  activeAlerts: string[];
  setOpsMetrics: (data: Partial<OperationsState>) => void;
}

export const useOperationsStore = create<OperationsState>((set) => ({
  uptimePct: 100.0,
  brokerLatencyMs: 15.0,
  dbConnected: true,
  brokerConnected: true,
  activeAlerts: [],
  setOpsMetrics: (data) => set((state) => ({ ...state, ...data })),
}));
