export class RealtimeWSClient {
  private url: string;
  private listeners: Map<string, Array<(data: any) => void>>;
  private ws: any;

  constructor(url: string) {
    this.url = url;
    this.listeners = new Map();
  }

  public connect() {
    console.log(`Connecting to AlphaForge live market stream: ${this.url}`);
    // Simulate real-time streaming heartbeats
    setInterval(() => {
      this.trigger("predictions", {
        ticker: "AAPL",
        price: 182.50 + (Math.random() - 0.5) * 0.5,
        change: 1.39 + (Math.random() - 0.5) * 0.1,
        timestamp: new Date().toISOString()
      });
    }, 3000);
  }

  public subscribe(event: string, callback: (data: any) => void) {
    if (!this.listeners.has(event)) {
      this.listeners.set(event, []);
    }
    this.listeners.get(event)?.push(callback);
  }

  private trigger(event: string, data: any) {
    const list = this.listeners.get(event);
    if (list) {
      list.forEach((cb) => cb(data));
    }
  }
}

export const wsClient = new RealtimeWSClient(
  process.env.NEXT_PUBLIC_WS_URL || "ws://localhost:8000/live_trading/stream"
);
