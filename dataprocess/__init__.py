from .abstractions.IDataProcess import ExecutionFlags, IDataProcess
from .abstractions.IDataProcessor import IDataProcessor
from .abstractions.IDataProcessorStrategy import IDataProcessorStrategy
from .abstractions.IDataRetreiver import IDataRetriever
from .abstractions.IDataRetreiveStrategy import IDataRetreiveStrategy
from .abstractions.IDataUpdater import IDataUpdater
from .abstractions.IDataUpdateStrategy import IDataUpdateStrategy

# from .helpers.dataframe_helpers import DataframeColumnConversion

from .utilities.strategy_data_processor import StrategyDataProcessor
from .utilities.strategy_data_retreiver import StrategyDataRetreiver
from .utilities.strategy_data_updater import StrategyDataUpdater
from .utilities.dataprocess_base import DataProcessBase

class g:
    ANNOUNCE:bool = True
    """Set announcing of framework activities."""

    USE_EXECUTION_FLAGS:bool = True
    """Determine if the framework should consider the execution flags when running
    the current process.  Default is True and so each ExecutionFlag will be
    checked before executing each process step of the current process."""

    CURRENT_PROCESS:IDataProcess = None
    """The DataProcess currently being executed."""

    FAILED_PROCESSES:list[str] = []
    """List of failed process steps.  Only populates if CONTINUE_ON_FAIL is set."""

    CONTINUE_ON_FAIL:bool = False
    """Determines if framework should continue with the next process if the
    current process fails.  Defaults to false which will raise the error and
    stop the framework from processing any further registered processes."""

from .dataprocess_setup import register_process, run, clear, remove, use_execution_flags, continue_on_fail, toggle_announce