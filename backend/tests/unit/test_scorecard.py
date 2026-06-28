import pytest
from app.modules.validation.scorecard_generator import ScorecardGenerator

def test_scorecard_fail_gates():
    generator = ScorecardGenerator()
    
    # Passes validation (Sharpe 1.58, DD -11.4%, hit ratio 61.2%, PSI 0.08, daily loss 0.5%)
    sc_pass = generator.generate_scorecard(
        paper_days=30, sharpe=1.58, sortino=2.05, max_drawdown=-0.114,
        hit_ratio=0.612, profit_factor=1.65, psi=0.08, latency_ms=12.5, daily_loss=0.005
    )
    assert sc_pass["validation_passed"] is True

    # Fails validation (PSI 0.28 > 0.25 limit)
    sc_fail_psi = generator.generate_scorecard(
        paper_days=30, sharpe=1.58, sortino=2.05, max_drawdown=-0.114,
        hit_ratio=0.612, profit_factor=1.65, psi=0.28, latency_ms=12.5, daily_loss=0.005
    )
    assert sc_fail_psi["validation_passed"] is False

    # Fails validation (Sharpe 0.8 < 1.0 limit)
    sc_fail_sharpe = generator.generate_scorecard(
        paper_days=30, sharpe=0.8, sortino=1.05, max_drawdown=-0.114,
        hit_ratio=0.612, profit_factor=1.65, psi=0.08, latency_ms=12.5, daily_loss=0.005
    )
    assert sc_fail_sharpe["validation_passed"] is False

def test_institutional_scorecard_gates():
    from app.modules.shadow_validation.scorecard_generator import ScorecardGenerator as InstScorecard
    gen = InstScorecard()

    # Passes (Sharpe 1.58 > 1.25, Hit Ratio 61.2% > 60%, Drawdown 11.4% < 15%, PSI 0.08 < 0.15)
    sc = gen.generate_scorecard(sharpe=1.58, hit_ratio=0.612, max_drawdown=-0.114, psi=0.08, ruin_prob=0.001, uptime=99.9, latency=45.0)
    assert sc["passed"] is True

    # Fails Sharpe (1.18 <= 1.25 limit)
    sc_fail_sharpe = gen.generate_scorecard(sharpe=1.18, hit_ratio=0.612, max_drawdown=-0.114, psi=0.08, ruin_prob=0.001, uptime=99.9, latency=45.0)
    assert sc_fail_sharpe["passed"] is False

