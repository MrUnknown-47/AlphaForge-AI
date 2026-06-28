from typing import Dict, Any, List
from app.modules.operations.uptime_tracker import UptimeTracker
from app.modules.operations.health_monitor import HealthMonitor
from app.modules.operations.model_monitor import ModelMonitor
from app.modules.operations.portfolio_monitor import PortfolioMonitor
from app.modules.operations.scheduler_monitor import SchedulerMonitor
from app.modules.operations.incident_manager import IncidentManager
from app.modules.operations.audit_logger import AuditLogger
from app.modules.operations.alert_manager import AlertManager
from app.modules.operations.scorecard_generator import ScorecardGenerator

# Caching instances singleton
_uptime_tracker = UptimeTracker()
_health_monitor = HealthMonitor(_uptime_tracker)
_model_monitor = ModelMonitor()
_portfolio_monitor = PortfolioMonitor()
_scheduler_monitor = SchedulerMonitor()
_incident_manager = IncidentManager()
_audit_logger = AuditLogger()
_alert_manager = AlertManager()
_scorecard_generator = ScorecardGenerator()

def get_health_monitor() -> HealthMonitor:
    return _health_monitor

def get_model_monitor() -> ModelMonitor:
    return _model_monitor

def get_portfolio_monitor() -> PortfolioMonitor:
    return _portfolio_monitor

def get_scheduler_monitor() -> SchedulerMonitor:
    return _scheduler_monitor

def get_incident_manager() -> IncidentManager:
    return _incident_manager

def get_audit_logger() -> AuditLogger:
    return _audit_logger

def get_alert_manager() -> AlertManager:
    return _alert_manager

def get_scorecard_generator() -> ScorecardGenerator:
    return _scorecard_generator

class OperationsService:
    def __init__(self) -> None:
        self.health = get_health_monitor()
        self.model = get_model_monitor()
        self.portfolio = get_portfolio_monitor()
        self.scheduler = get_scheduler_monitor()
        self.incident = get_incident_manager()
        self.audit = get_audit_logger()
        self.alert = get_alert_manager()
        self.scorecard = get_scorecard_generator()

    def get_health_status(self) -> Dict[str, Any]:
        return self.health.check_health()

    def get_model_metrics(self) -> Dict[str, Any]:
        return self.model.track_model_status(1.58, 0.612, 0.85, 0.08)

    def get_portfolio_state(self) -> Dict[str, Any]:
        return self.portfolio.evaluate_portfolio(0.45, 1.0, -0.015, -0.022, -0.114)

    def get_incidents(self) -> List[Dict[str, Any]]:
        return self.incident.incidents

    def get_alerts(self) -> List[Dict[str, Any]]:
        return self.alert.alerts_history

    def get_audit_trail(self) -> List[str]:
        # Return list of files in audit directory
        import glob
        return glob.glob(f"{self.audit.log_dir}/*.json")

    def get_scorecard(self) -> Dict[str, Any]:
        h = self.health.check_health()
        m = self.model.track_model_status(1.58, 0.612, 0.85, 0.08)
        p = self.portfolio.evaluate_portfolio(0.45, 1.0, -0.015, -0.022, -0.114)
        
        return self.scorecard.generate_scorecard(
            uptime=h["api_uptime"],
            sharpe=m["sharpe"],
            hit_ratio=m["hit_ratio"],
            drawdown=p["drawdown"],
            reconc_acc=100.0
        )
