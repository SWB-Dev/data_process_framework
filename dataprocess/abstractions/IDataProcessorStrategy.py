from typing import Protocol, TypeVar

T = TypeVar("T")

class IDataProcessorStrategy(Protocol):
    def process_data(self) -> T:
        """Strategy for processing raw data."""