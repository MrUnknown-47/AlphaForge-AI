import api from "./api";

export const securityService = {
  getStatus: async () => {
    const res = await api.get("/security/status");
    return res.data;
  },
  getSecrets: async () => {
    const res = await api.get("/security/secrets");
    return res.data;
  },
  triggerKillSwitch: async () => {
    const res = await api.post("/security/kill-switch/trigger");
    return res.data;
  }
};
