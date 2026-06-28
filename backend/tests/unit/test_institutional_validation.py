import pytest
from app.modules.trading.institutional_validation import InstitutionalValidator

def test_paper_evaluator_keys():
    validator = InstitutionalValidator()
    results = validator.run_paper_evaluator()
    assert "30_day" in results
    assert "60_day" in results
    assert "90_day" in results
    assert isinstance(results["30_day"]["Expected_CAGR"], float)

def test_transaction_cost_stress():
    validator = InstitutionalValidator()
    results = validator.stress_test_transaction_costs()
    # Cost of 5 bps should yield higher Sharpe than 100 bps
    assert results[5] > results[100]

def test_monte_carlo_metrics():
    validator = InstitutionalValidator()
    results = validator.run_monte_carlo(num_simulations=10, days=50) # small run
    assert "Expected_CAGR" in results
    assert "Expected_Sharpe" in results
    assert "Probability_of_Ruin" in results
    assert results["Probability_of_Ruin"] == 0.0
