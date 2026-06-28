import api from "./api";

export const authService = {
  login: async (email: string, password: string) => {
    const res = await api.post("/auth/login", { email, password });
    return res.data;
  },
  register: async (email: string, username: string, password: string) => {
    const res = await api.post("/auth/register", { email, username, password });
    return res.data;
  },
  logout: async () => {
    const res = await api.post("/auth/logout");
    return res.data;
  },
  refresh: async () => {
    const res = await api.post("/auth/refresh");
    return res.data;
  },
  verifyMfa: async (code: string) => {
    const res = await api.post("/auth/mfa", { code });
    return res.data;
  },
  resetPassword: async (email: string) => {
    const res = await api.post("/auth/reset-password", { email });
    return res.data;
  },
  confirmReset: async (token: string, new_pass: string) => {
    const res = await api.post("/auth/reset-password/confirm", { token, new_password: new_pass });
    return res.data;
  }
};
export default authService;
