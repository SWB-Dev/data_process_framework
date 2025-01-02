from typing import TypeVar
from .. import IDataProcessor, IDataProcessorStrategy

T = TypeVar("T")

class StrategyDataProcessor:
    
    strategy:IDataProcessorStrategy

    def process_data(self) -> T:
        return self.strategy.process_data()
    
    def with_strategy(self, strategy:IDataProcessorStrategy) -> IDataProcessor:
        self.strategy = strategy
        return self