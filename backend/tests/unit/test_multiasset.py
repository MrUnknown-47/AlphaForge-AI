import pytest
from app.modules.assets.security_master import SecurityMaster
from app.modules.assets.asset_classifier import AssetClassifier
from app.modules.assets.contract_specs import ContractSpecifications
from app.modules.assets.corporate_actions import CorporateActionsManager
from app.modules.derivatives.strategies.service import OptionsStrategyService
from app.modules.futures.contracts import FuturesContractsManager
from app.modules.futures.margin import FuturesMarginEngine
from app.modules.futures.rollover import FuturesRolloverEngine
from app.modules.fx.carry import ForexCarryCalculator
from app.modules.fx.hedging import ForexHedgingEngine
from app.modules.crypto.funding import CryptoFundingRateManager
from app.modules.crypto.risk import CryptoRiskEngine

def test_security_master():
    master = SecurityMaster()
    details = master.get_security_details("ES_U26")
    assert details["type"] == "FUTURE"
    assert details["multiplier"] == 50

def test_asset_classifier():
    classifier = AssetClassifier()
    assert classifier.classify("EQUITY") == "Risk Asset - Stocks"
    assert classifier.classify("BOND") == "Fixed Income Asset - Treasuries"

def test_contract_specs():
    specs = ContractSpecifications()
    notional = specs.get_notional_value("ES_U26", price=4500.0, quantity=2, multiplier=50)
    assert notional == 4500.0 * 2 * 50
    margin = specs.get_initial_margin(notional, margin_requirement=0.08)
    assert margin == notional * 0.08

def test_corporate_actions():
    manager = CorporateActionsManager()
    split = manager.apply_stock_split("AAPL", price=150.0, quantity=10, ratio=2.0)
    assert split["adjusted_price"] == 75.0
    assert split["adjusted_quantity"] == 20
    
    div = manager.process_dividend("AAPL", cash_balance=1000.0, dividend_per_share=0.50, shares_held=100)
    assert div == 1050.0

def test_options_strategies():
    # Long call
    lc = OptionsStrategyService.long_call(S=150.0, strike=150.0, premium=5.0)
    assert lc["strategy"] == "Long Call"
    assert lc["max_loss"] == 5.0
    
    # Iron condor
    ic = OptionsStrategyService.iron_condor(S=150.0, short_put=140.0, long_put=135.0, short_call=160.0, long_call=165.0, net_premium=2.50)
    assert ic["strategy"] == "Iron Condor"
    assert ic["max_profit"] == 2.50
    
    # Collar
    collar = OptionsStrategyService.collar(S=150.0, put_strike=142.50, call_strike=157.50, net_premium=0.0)
    assert collar["strategy"] == "Collar"
    assert collar["max_loss"] == 150.0 - 142.50

def test_futures_engine():
    contracts = FuturesContractsManager()
    margin_eng = FuturesMarginEngine()
    roll_eng = FuturesRolloverEngine()
    
    spec = contracts.get_futures_spec("CL")
    assert spec["name"] == "Crude Oil"
    
    margin = margin_eng.calculate_margin("NQ", quantity=2)
    assert margin["maintenance_margin"] == 18000.0 * 2
    
    roll = roll_eng.perform_rollover("ES_U26", "ES_Z26", position_qty=5)
    assert roll["status"] == "SUCCESSFUL_ROLLOVER"

def test_forex_engine():
    carry_calc = ForexCarryCalculator()
    hedge_eng = ForexHedgingEngine()
    
    carry = carry_calc.calculate_carry_rate("EURUSD", is_long=True)
    # EUR (0.0425) - USD (0.0525) = -0.01
    assert abs(carry - (-0.01)) < 1e-4
    
    hedge = hedge_eng.calculate_hedging_shares(foreign_currency_exposure=1000000.0, spot_price=1.08)
    assert hedge["required_fx_units"] == -1000000.0

def test_crypto_engine():
    funding_eng = CryptoFundingRateManager()
    risk_eng = CryptoRiskEngine()
    
    rate = funding_eng.get_funding_rate("BTC-PERP")
    assert rate == 0.00012
    
    liq = risk_eng.calculate_liquidation_price(entry_price=60000.0, leverage=10.0, is_long=True)
    # 60000 * (1 - 0.1) = 54000
    assert liq == 54000.0
