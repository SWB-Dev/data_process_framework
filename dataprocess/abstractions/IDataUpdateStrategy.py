from typing import Protocol, TypeVar

T = TypeVar("T")

class IDataUpdateStrategy(Protocol):
    def prepare_updates(self) -> T:
        """Strategy to prepare data for updating."""
    
    def send_updates(self) -> T:
        """Strategy for sending data updates."""