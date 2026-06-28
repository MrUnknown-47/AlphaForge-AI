import asyncio
from abc import ABC, abstractmethod
from typing import Callable, Coroutine, Any

# Abstract Event definition
class Event(ABC):
    @property
    @abstractmethod
    def event_name(self) -> str:
        pass

class EventBus(ABC):
    @abstractmethod
    async def publish(self, topic: str, event: Event) -> None:
        pass

    @abstractmethod
    async def subscribe(self, topic: str, handler: Callable[[Event], Coroutine[Any, Any, None]]) -> None:
        pass

class InMemoryEventBus(EventBus):
    def __init__(self) -> None:
        self._subscribers: dict[str, list[Callable[[Event], Coroutine[Any, Any, None]]]] = {}

    async def publish(self, topic: str, event: Event) -> None:
        if topic in self._subscribers:
            # Dispatch asynchronously to avoid blocking publishers
            for handler in self._subscribers[topic]:
                asyncio.create_task(handler(event))

    async def subscribe(self, topic: str, handler: Callable[[Event], Coroutine[Any, Any, None]]) -> None:
        if topic not in self._subscribers:
            self._subscribers[topic] = []
        self._subscribers[topic].append(handler)

# Global local application event bus instance
event_bus = InMemoryEventBus()

async def get_event_bus() -> EventBus:
    """FastAPI Dependency for accessing the system event bus."""
    return event_bus