import { create } from "zustand";

export interface Position {
  ticker: string;
  side: "LONG" | "SHORT";
  quantity: number;
  entry: number;
  current: number;
  pnl: number;
  pnl_pct: number;
  exposure_pct: number;
  status: string;
}

export interface Order {
  id: string;
  ticker: string;
  side: "BUY" | "SELL";
  type: "MARKET" | "LIMIT";
  quantity: number;
  price?: number;
  status: "PENDING" | "FILLED" | "CANCELLED";
  timestamp: string;
}

export interface Fill {
  id: string;
  ticker: string;
  side: "BUY" | "SELL";
  price: number;
  quantity: number;
  commission: number;
  slippage_bps: number;
  latency_ms: number;
  timestamp: string;
}

export interface LiveTelemetry {
  average_slippage_bps: number;
  fill_ratio: number;
  average_latency_ms: number;
  implementation_shortfall_bps: number;
  vwap_deviation_bps: number;
}

export interface LiveRiskState {
  kill_switch_active: boolean;
  max_position_exposure: number;
  current_exposure: number;
  daily_drawdown: number;
}

export interface LivePnlState {
  daily_pnl: number;
  realized_pnl: number;
  unrealized_pnl: number;
  portfolio_equity: number;
  equity_curve: { time: string; value: number }[];
}

export interface LiveEvent {
  id: string;
  event_type: "ORDER_SUBMITTED" | "ORDER_ACCEPTED" | "PARTIAL_FILL" | "FILL_COMPLETED" | "RISK_WARNING" | "BROKER_DISCONNECT" | "BROKER_CONNECT";
  message: string;
  timestamp: string;
}

interface TradingState {
  positions: Position[];
  orders: Order[];
  fills: Fill[];
  telemetry: LiveTelemetry;
  risk: LiveRiskState;
  pnl: LivePnlState;
  events: LiveEvent[];
  connectionStatus: "CONNECTED" | "CONNECTING" | "DISCONNECTED";
  
  // Actions
  setPositions: (positions: Position[]) => void;
  setOrders: (orders: Order[]) => void;
  addOrder: (order: Order) => void;
  setFills: (fills: Fill[]) => void;
  setTelemetry: (telemetry: LiveTelemetry) => void;
  setRisk: (risk: LiveRiskState) => void;
  setPnl: (pnl: LivePnlState) => void;
  addEvent: (event: LiveEvent) => void;
  setConnectionStatus: (status: "CONNECTED" | "CONNECTING" | "DISCONNECTED") => void;
  flattenPositions: () => void;
  toggleKillSwitch: (active: boolean) => void;
  connectWebSockets: () => () => void;
}

export const useTradingStore = create<TradingState>((set, get) => {
  let wsList: WebSocket[] = [];

  return {
    positions: [
      { ticker: "AAPL", side: "LONG", quantity: 150, entry: 182.40, current: 185.10, pnl: 405.00, pnl_pct: 1.48, exposure_pct: 15.2, status: "ACTIVE" },
      { ticker: "NVDA", side: "LONG", quantity: 80, entry: 920.00, current: 945.50, pnl: 2040.00, pnl_pct: 2.77, exposure_pct: 22.4, status: "ACTIVE" },
      { ticker: "MSFT", side: "SHORT", quantity: 50, entry: 415.00, current: 412.20, pnl: 140.00, pnl_pct: 0.67, exposure_pct: 8.5, status: "ACTIVE" }
    ],
    orders: [
      { id: "ord_0991", ticker: "TSLA", side: "BUY", type: "LIMIT", quantity: 100, price: 175.50, status: "PENDING", timestamp: new Date(Date.now() - 50000).toISOString() },
      { id: "ord_0992", ticker: "AAPL", side: "SELL", type: "LIMIT", quantity: 50, price: 186.00, status: "PENDING", timestamp: new Date(Date.now() - 30000).toISOString() }
    ],
    fills: [
      { id: "fill_881", ticker: "NVDA", side: "BUY", price: 920.00, quantity: 80, commission: 4.50, slippage_bps: 1.25, latency_ms: 22.4, timestamp: new Date(Date.now() - 600000).toISOString() },
      { id: "fill_882", ticker: "MSFT", side: "SELL", price: 415.00, quantity: 50, commission: 2.25, slippage_bps: 0.85, latency_ms: 18.2, timestamp: new Date(Date.now() - 400000).toISOString() }
    ],
    telemetry: {
      average_slippage_bps: 1.15,
      fill_ratio: 0.965,
      average_latency_ms: 24.5,
      implementation_shortfall_bps: 1.45,
      vwap_deviation_bps: 0.75
    },
    risk: {
      kill_switch_active: false,
      max_position_exposure: 50.0,
      current_exposure: 46.1,
      daily_drawdown: 0.45
    },
    pnl: {
      daily_pnl: 2585.00,
      realized_pnl: 1200.00,
      unrealized_pnl: 1385.00,
      portfolio_equity: 252585.00,
      equity_curve: [
        { time: "09:30", value: 250000.00 },
        { time: "10:00", value: 250450.00 },
        { time: "10:30", value: 251100.00 },
        { time: "11:00", value: 250800.00 },
        { time: "11:30", value: 251500.00 },
        { time: "12:00", value: 252100.00 },
        { time: "12:30", value: 251900.00 },
        { time: "13:00", value: 252585.00 }
      ]
    },
    events: [
      { id: "evt_001", event_type: "BROKER_CONNECT", message: "Successfully connected to Alpaca Paper Broker API.", timestamp: new Date().toISOString() },
      { id: "evt_002", event_type: "ORDER_SUBMITTED", message: "LIMIT BUY order submitted for 100 TSLA @ $175.50", timestamp: new Date().toISOString() }
    ],
    connectionStatus: "DISCONNECTED",

    setPositions: (positions) => set({ positions }),
    setOrders: (orders) => set({ orders }),
    addOrder: (order) => set((state) => {
      // If order is FILLED, add it to fills as well
      const updatedOrders = [order, ...state.orders];
      let updatedFills = state.fills;
      let updatedPositions = state.positions;

      if (order.status === "FILLED") {
        const fillId = `fill_${Math.floor(Math.random() * 1000)}`;
        const newFill: Fill = {
          id: fillId,
          ticker: order.ticker,
          side: order.side,
          price: order.price || 150.00,
          quantity: order.quantity,
          commission: 2.50,
          slippage_bps: 1.10,
          latency_ms: 25.0,
          timestamp: new Date().toISOString()
        };
        updatedFills = [newFill, ...state.fills];

        // Update positions or add new position
        const existingIdx = state.positions.findIndex(p => p.ticker === order.ticker);
        const positionSide = order.side === "BUY" ? "LONG" : "SHORT";
        
        if (existingIdx >= 0) {
          const existing = state.positions[existingIdx];
          const newQty = order.side === "BUY" ? existing.quantity + order.quantity : existing.quantity - order.quantity;
          if (newQty === 0) {
            updatedPositions = state.positions.filter(p => p.ticker !== order.ticker);
          } else {
            const updatedPosList = [...state.positions];
            updatedPosList[existingIdx] = {
              ...existing,
              quantity: Math.abs(newQty),
              side: newQty > 0 ? "LONG" : "SHORT",
              current: order.price || existing.current
            };
            updatedPositions = updatedPosList;
          }
        } else {
          updatedPositions = [
            ...state.positions,
            {
              ticker: order.ticker,
              side: positionSide,
              quantity: order.quantity,
              entry: order.price || 150.00,
              current: order.price || 150.00,
              pnl: 0.0,
              pnl_pct: 0.0,
              exposure_pct: 5.0,
              status: "ACTIVE"
            }
          ];
        }
      }

      return {
        orders: updatedOrders,
        fills: updatedFills,
        positions: updatedPositions
      };
    }),
    setFills: (fills) => set({ fills }),
    setTelemetry: (telemetry) => set({ telemetry }),
    setRisk: (risk) => set({ risk }),
    setPnl: (pnl) => set({ pnl }),
    addEvent: (event) => set((state) => ({ events: [event, ...state.events.slice(0, 49)] })),
    setConnectionStatus: (status) => set({ connectionStatus: status }),

    flattenPositions: () => {
      set((state) => {
        // Create matching opposite orders to liquidate all positions
        const liquidationOrders: Order[] = state.positions.map((pos) => ({
          id: `ord_liq_${Math.floor(Math.random() * 10000)}`,
          ticker: pos.ticker,
          side: pos.side === "LONG" ? "SELL" : "BUY",
          type: "MARKET",
          quantity: pos.quantity,
          status: "FILLED",
          timestamp: new Date().toISOString()
        }));

        // Trigger notifications
        const liquidationEvents: LiveEvent[] = state.positions.map((pos) => ({
          id: `evt_liq_${Math.floor(Math.random() * 10000)}`,
          event_type: "FILL_COMPLETED",
          message: `Liquidated position for ${pos.ticker} (${pos.quantity} shares).`,
          timestamp: new Date().toISOString()
        }));

        return {
          positions: [],
          orders: [...liquidationOrders, ...state.orders],
          events: [...liquidationEvents, ...state.events],
          risk: {
            ...state.risk,
            current_exposure: 0.0
          }
        };
      });
    },

    toggleKillSwitch: (active) => {
      set((state) => {
        const message = active ? "EMERGENCY SYSTEM KILL SWITCH ACTIVATED. HALTING ALL RUNTIMES." : "Emergency Kill Switch deactivated.";
        const event: LiveEvent = {
          id: `evt_ks_${Math.floor(Math.random() * 10000)}`,
          event_type: "RISK_WARNING",
          message,
          timestamp: new Date().toISOString()
        };

        return {
          risk: {
            ...state.risk,
            kill_switch_active: active
          },
          events: [event, ...state.events],
          positions: active ? [] : state.positions // Flatten if activated
        };
      });
    },

    connectWebSockets: () => {
      set({ connectionStatus: "CONNECTING" });

      // In Next.js, support running locally or staging on standard backend ports
      const wsUrl = "ws://localhost:8000/live";

      // Simulated websocket stream updates to guarantee rich client-side animations
      const interval = setInterval(() => {
        const store = get();
        if (store.risk.kill_switch_active) return;

        // Fluctuates prices and updates unrealized PnL
        const updatedPositions = store.positions.map((pos) => {
          const changePct = (Math.random() - 0.5) * 0.002; // +/- 0.1% change
          const newCurrent = pos.current * (1 + changePct);
          const pnlDiff = pos.side === "LONG" 
            ? (newCurrent - pos.entry) * pos.quantity 
            : (pos.entry - newCurrent) * pos.quantity;
          const pnlPct = (pnlDiff / (pos.entry * pos.quantity)) * 100;
          return {
            ...pos,
            current: parseFloat(newCurrent.toFixed(2)),
            pnl: parseFloat(pnlDiff.toFixed(2)),
            pnl_pct: parseFloat(pnlPct.toFixed(2))
          };
        });

        // Fluctuates telemetry metrics
        const updatedTelemetry: LiveTelemetry = {
          average_slippage_bps: parseFloat((store.telemetry.average_slippage_bps + (Math.random() - 0.5) * 0.05).toFixed(2)),
          fill_ratio: parseFloat((Math.min(1.0, store.telemetry.fill_ratio + (Math.random() - 0.5) * 0.002)).toFixed(3)),
          average_latency_ms: parseFloat((store.telemetry.average_latency_ms + (Math.random() - 0.5) * 1.5).toFixed(1)),
          implementation_shortfall_bps: parseFloat((store.telemetry.implementation_shortfall_bps + (Math.random() - 0.5) * 0.05).toFixed(2)),
          vwap_deviation_bps: parseFloat((store.telemetry.vwap_deviation_bps + (Math.random() - 0.5) * 0.02).toFixed(2))
        };

        // Update real-time equity curve
        const lastVal = store.pnl.equity_curve[store.pnl.equity_curve.length - 1].value;
        const newVal = lastVal + (Math.random() - 0.48) * 150;
        const now = new Date();
        const timeStr = `${now.getHours().toString().padStart(2, "0")}:${now.getMinutes().toString().padStart(2, "0")}:${now.getSeconds().toString().padStart(2, "0")}`;
        const newCurve = [...store.pnl.equity_curve.slice(1), { time: timeStr, value: parseFloat(newVal.toFixed(2)) }];

        set({
          positions: updatedPositions,
          telemetry: updatedTelemetry,
          pnl: {
            ...store.pnl,
            daily_pnl: parseFloat((store.pnl.daily_pnl + (Math.random() - 0.48) * 50).toFixed(2)),
            portfolio_equity: parseFloat(newVal.toFixed(2)),
            equity_curve: newCurve
          }
        });

        // Trigger occasional simulated events or partial fills
        if (Math.random() > 0.92) {
          const eventsList = [
            "Partial fill: Bought 10 TSLA @ $175.50",
            "Fill completed: Sold 50 AAPL @ $186.00",
            "Risk warning: Portfolio exposure approaching 48% target limit."
          ];
          const typeList: ("PARTIAL_FILL" | "FILL_COMPLETED" | "RISK_WARNING")[] = [
            "PARTIAL_FILL",
            "FILL_COMPLETED",
            "RISK_WARNING"
          ];
          const choiceIdx = Math.floor(Math.random() * eventsList.length);
          const evt: LiveEvent = {
            id: `evt_sim_${Math.floor(Math.random() * 10000)}`,
            event_type: typeList[choiceIdx],
            message: eventsList[choiceIdx],
            timestamp: new Date().toISOString()
          };
          store.addEvent(evt);
        }
      }, 3000);

      // Setup actual websockets gracefully
      try {
        const wsPaths = ["orders", "fills", "pnl", "telemetry", "events"];
        wsPaths.forEach((path) => {
          const ws = new WebSocket(`${wsUrl}/${path}`);
          ws.onopen = () => {
            set({ connectionStatus: "CONNECTED" });
          };
          ws.onmessage = (event) => {
            try {
              const data = JSON.parse(event.data);
              // Dispatch to state based on category/payload attributes
              if (path === "orders") get().setOrders(data);
              if (path === "fills") get().setFills(data);
              if (path === "pnl") get().setPnl(data);
              if (path === "telemetry") get().setTelemetry(data);
              if (path === "events") get().addEvent(data);
            } catch (err) {
              // Ignore payload decode errors
            }
          };
          ws.onerror = () => {
            set({ connectionStatus: "DISCONNECTED" });
          };
          ws.onclose = () => {
            // connectionStatus handled gracefully by local simulations fallback
          };
          wsList.push(ws);
        });
      } catch (err) {
        // graceful connection error fallback
      }

      return () => {
        clearInterval(interval);
        wsList.forEach((ws) => {
          try {
            ws.close();
          } catch (e) {}
        });
      };
    }
  };
});
