import api from "./api";

export const validationService = {
  getScorecard: async () => {
    const res = await api.get("/validation/scorecard");
    return res.data;
  },
  getLiveMetrics: async () => {
    const res = await api.get("/validation/live");
    return res.data;
  }
};
