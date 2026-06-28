import api from "./api";

export const operationsService = {
  getHealth: async () => {
    const res = await api.get("/ops/health");
    return res.data;
  },
  getIncidents: async () => {
    const res = await api.get("/ops/incidents");
    return res.data;
  },
  getAlerts: async () => {
    const res = await api.get("/ops/alerts");
    return res.data;
  }
};
