import api from "./api";

export const portfolioService = {
  getSummary: async () => {
    const res = await api.get("/portfolio/summary");
    return res.data;
  },
  getHoldings: async () => {
    const res = await api.get("/portfolio/holdings");
    return res.data;
  }
};
