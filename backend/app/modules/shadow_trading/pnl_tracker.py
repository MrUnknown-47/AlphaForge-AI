import logging
from typing import Dict, Any, List

logger = logging.getLogger("PnLTracker")

class PnLTracker:
    def __init__(self, initial_value: float = 100000.0) -> None:
        self.initial_value = initial_value
        self.high_watermark = initial_value
        self.trading_halted = False

    def check_risk_limits(
        self, portfolio_value: float, active_positions: List[Dict[str, Any]], daily_loss: float
    ) -> bool:
        """
        Risk checks:
        - Max position size <= 10%
        - Max total exposure <= 50%
        - Daily loss <= 3%
        - Max drawdown <= 20%
        """
        if self.trading_halted:
            return True

        # Drawdown check
        if portfolio_value > self.high_watermark:
            self.high_watermark = portfolio_value
        drawdown = (portfolio_value - self.high_watermark) / self.high_watermark
        if abs(drawdown) > 0.20:
            logger.error(f"HALT: Max Drawdown limit breached! Drawdown: {drawdown*100:.2f}%")
            self.trading_halted = True

        # Daily loss check
        loss_pct = daily_loss / self.initial_value if self.initial_value > 0 else 0.0
        if loss_pct > 0.03:
            logger.error(f"HALT: Daily Loss limit breached! Loss: {loss_pct*100:.2f}%")
            self.trading_halted = True

        # Position/Exposure checks
        total_exposure = 0.0
        for pos in active_positions:
            pos_val = abs(pos["quantity"]) * pos["entry_price"]
            total_exposure += pos_val
            # Single position check (10%)
            if pos_val > portfolio_value * 0.10:
                logger.error(f"HALT: Single Position size limit breached on {pos['ticker']}!")
                self.trading_halted = True

        # Total exposure check (50%)
        exposure_pct = total_exposure / portfolio_value if portfolio_value > 0 else 0.0
        if exposure_pct > 0.50:
            logger.error(f"HALT: Total Exposure limit breached! Exposure: {exposure_pct*100:.2f}%")
            self.trading_halted = True

        return self.trading_halted
