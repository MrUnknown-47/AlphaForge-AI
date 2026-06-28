import api from "./api";

export const predictionService = {
  getLatestSignal: async (symbol: string) => {
    const res = await api.get(`/prediction/signal/${symbol}`);
    return res.data;
  },
  getPredictionHistory: async (symbol: string) => {
    const res = await api.get(`/prediction/history/${symbol}`);
    return res.data;
  }
};
