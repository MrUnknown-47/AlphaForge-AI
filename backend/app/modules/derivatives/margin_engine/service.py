from typing import Dict, Any, List

class MarginService:
    @staticmethod
    def calculate_reg_t(positions: List[Dict[str, Any]]) -> Dict[str, float]:
        initial_margin = 0.0
        maintenance_margin = 0.0
        portfolio_value = 0.0

        for pos in positions:
            val = pos.get("quantity", 0) * pos.get("market_price", 0.0)
            portfolio_value += val
            if pos.get("type") == "STOCK":
                initial_margin += abs(val) * 0.50 # Reg-T stock requirement is 50%
                maintenance_margin += abs(val) * 0.25 # Reg-T maintenance is 25%
            elif pos.get("type") == "OPTION":
                initial_margin += abs(val) * 1.00 # Standard Option premium upfront
                maintenance_margin += abs(val) * 0.20 # Standard option risk

        return {
            "initial_margin": initial_margin,
            "maintenance_margin": maintenance_margin,
            "portfolio_value": portfolio_value,
            "excess_liquidity": portfolio_value - maintenance_margin
        }

    @staticmethod
    def calculate_portfolio_margin(positions: List[Dict[str, Any]]) -> Dict[str, float]:
        # Portfolio margin stress test: test +15% / -15% moves on underlying stock
        stress_scenarios = [-0.15, -0.10, -0.05, 0.0, 0.05, 0.10, 0.15]
        max_loss = 0.0
        portfolio_value = 0.0

        for pos in positions:
            qty = pos.get("quantity", 0)
            S = pos.get("underlying_price", 0.0)
            market_price = pos.get("market_price", 0.0)
            portfolio_value += qty * market_price
            
            # Simple stock position
            if pos.get("type") == "STOCK":
                for shock in stress_scenarios:
                    loss = -qty * S * shock
                    if loss > max_loss:
                        max_loss = loss
            elif pos.get("type") == "OPTION":
                # Option stress test approximation: calculate loss based on delta/gamma
                delta = pos.get("delta", 0.0)
                gamma = pos.get("gamma", 0.0)
                for shock in stress_scenarios:
                    dS = S * shock
                    loss = -qty * (delta * dS + 0.5 * gamma * dS**2)
                    if loss > max_loss:
                        max_loss = loss

        # Initial margin is max_loss plus a buffer
        initial_margin = max(max_loss, portfolio_value * 0.15)
        maintenance_margin = max_loss
        return {
            "initial_margin": initial_margin,
            "maintenance_margin": maintenance_margin,
            "portfolio_value": portfolio_value,
            "excess_liquidity": portfolio_value - maintenance_margin
        }

    @staticmethod
    def calculate_span_approximation(futures_positions: List[Dict[str, Any]]) -> Dict[str, float]:
        # SPAN style scanning risk scenarios
        total_scanning_risk = 0.0
        portfolio_value = 0.0

        for pos in futures_positions:
            qty = pos.get("quantity", 0)
            settlement = pos.get("settlement", 0.0)
            contract_size = pos.get("contract_size", 100)
            val = qty * settlement * contract_size
            portfolio_value += val
            
            # Use base margin requirements from models
            margin_req = pos.get("margin_requirement", 5000.0)
            total_scanning_risk += abs(qty) * margin_req

        initial_margin = total_scanning_risk
        maintenance_margin = total_scanning_risk * 0.75 # Typically 75% of initial
        return {
            "initial_margin": initial_margin,
            "maintenance_margin": maintenance_margin,
            "portfolio_value": portfolio_value,
            "excess_liquidity": portfolio_value - maintenance_margin
        }
class MarginEngine:
    pass
