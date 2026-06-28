from app.config import settings
from app.modules.broker.interface import BrokerInterface
from app.modules.broker.paper_broker import PaperBroker
from app.modules.broker.alpaca_broker import AlpacaBroker

# Singleton caches
_broker_instance = None

def get_broker() -> BrokerInterface:
    """Factory method returning the active broker instance based on configuration."""
    global _broker_instance
    broker_type = settings.BROKER.upper()
    
    if _broker_instance is not None:
        if broker_type == "ALPACA" and isinstance(_broker_instance, AlpacaBroker):
            return _broker_instance
        elif broker_type == "PAPER" and isinstance(_broker_instance, PaperBroker):
            return _broker_instance
        
    if broker_type == "ALPACA":
        _broker_instance = AlpacaBroker()
    else:
        _broker_instance = PaperBroker()
        
    return _broker_instance
