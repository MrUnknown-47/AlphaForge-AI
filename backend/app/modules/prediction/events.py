from app.shared.events import Event

class ModelRegisteredEvent(Event):
    """Fired when a trained model is logged in the database registry."""
    def __init__(self, model_name: str, version: str) -> None:
        self.model_name = model_name
        self.version = version

    @property
    def event_name(self) -> str:
        return "prediction.model_registered"