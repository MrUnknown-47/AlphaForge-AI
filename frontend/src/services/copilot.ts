import api from "./api";

export const copilotService = {
  askCopilot: async (prompt: string) => {
    const res = await api.post("/copilot/query", { prompt });
    return res.data;
  },
  getMarketAnalysis: async () => {
    const res = await api.get("/copilot/market");
    return res.data;
  },
  getPortfolioAnalysis: async () => {
    const res = await api.get("/copilot/portfolio");
    return res.data;
  }
};
