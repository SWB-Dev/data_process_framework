from typing import Protocol, TypeVar

T = TypeVar("T")

class IDataUpdater(Protocol):
    def prepare_updates(self) -> T:
        """Method to prepare data for updating."""
    
    def send_updates(self) -> T:
        """Method for sending data updates."""