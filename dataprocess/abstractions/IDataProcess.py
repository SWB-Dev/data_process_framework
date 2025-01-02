from typing import Protocol
from enum import IntEnum

class ExecutionFlags(IntEnum):
    """
    :type           IntEnum:\n
    0b0001 GET_DATA\n
    0b0010 PROCESS_DATA\n
    0b0100 PREPARE_DATA\n
    0b1000 SEND_DATA
    """
    GET_DATA = 0b0001
    PROCESS_DATA = 0b0010
    PREPARE_DATA = 0b0100
    SEND_DATA = 0b1000

class IDataProcess(Protocol):
    flags:int = None

    def get_data(self):
        """Method for reteiving data."""
    
    def process_data(self):
        """Method to process the raw data."""
    
    def prepare_data(self):
        """Method to prepare and normalize raw data."""
    
    def send_prepared_data(self):
        """Method to send the prepared data."""

    def set_execution_flags(self, get_data = True, process_data = True, prepare_data = True, send_data = True):
        """WARNING: THIS METHOD SHOULD NOT BE OVERIDDEN!\n
        Sets the execution flags."""

    def _should_execute(self, stage:ExecutionFlags) -> bool:
        """WARNING: INTERNAL METHOD - DO NOT OVERRIDE\n
        This method checks the execution flags to verify if a Data Process stage should execute."""