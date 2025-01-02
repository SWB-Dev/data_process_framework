from typing import TypeVar
from .. import IDataRetreiveStrategy, IDataRetriever

T = TypeVar("T")

class StrategyDataRetreiver():
    
    strategy:IDataRetreiveStrategy

    def get_data(self) -> T:
        return self.strategy.get_data()
    
    def with_strategy(self, strategy:IDataRetreiveStrategy) -> IDataRetriever:
        """Method to assign a data retreiving strategy to the retreiver."""
        self.strategy = strategy
        return self