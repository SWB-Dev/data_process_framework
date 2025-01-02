from typing import TypeVar
from .. import IDataUpdater, IDataUpdateStrategy

T = TypeVar("T")

class StrategyDataUpdater:

    strategy:IDataUpdateStrategy

    def prepare_updates(self) -> T:
        return self.strategy.prepare_updates()
    
    def send_updates(self) -> T:
        return self.strategy.send_updates()
    
    def with_strategy(self, strategy:IDataUpdateStrategy) -> IDataUpdater:
        self.strategy = strategy
        return self