import api from "./api";

export const brokerService = {
  getAccount: async () => {
    const res = await api.get("/broker/account");
    return res.data;
  },
  placeOrder: async (ticker: string, side: string, qty: number, type: string = "MARKET", price?: number) => {
    const res = await api.post("/broker/order", { ticker, side, qty, type, price });
    return res.data;
  },
  getPositions: async () => {
    const res = await api.get("/broker/positions");
    return res.data;
  }
};
