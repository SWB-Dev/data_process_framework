from typing import Protocol, TypeVar

T = TypeVar("T")

class IDataRetreiveStrategy(Protocol):
    def get_data(self) -> T:
        """Strategy to get data from a datasource."""