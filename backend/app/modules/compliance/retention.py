from typing import Dict, Any

class ComplianceRetentionManager:
    def __init__(self) -> None:
        self.retention_rules = {
            "audit_records": 7, # 7 years
            "trade_executions": 7,
            "ai_agent_decisions": 5, # 5 years
            "model_outputs": 3,
            "ops_logs": 1
        }

    def get_retention_period(self, record_type: str) -> int:
        return self.retention_rules.get(record_type, 7)
