from typing import Protocol, TypeVar

T = TypeVar("T")

class IDataRetriever(Protocol):
    def get_data(self) -> T:
        """Get data from the datasource."""