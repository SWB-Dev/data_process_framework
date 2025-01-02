from typing import Protocol, TypeVar

T = TypeVar("T")

class IDataProcessor(Protocol):
    def process_data(self) -> T:
        """Method to process raw data."""