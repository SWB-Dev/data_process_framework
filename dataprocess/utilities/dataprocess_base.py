from abc import ABC, abstractmethod
from . import ExecutionFlags

class DataProcessBase:

    def __new__(cls, *args, **kwargs):
        instance = super(DataProcessBase, cls).__new__(cls)
        instance.flags = 0
        instance.set_execution_flags()
        return instance

    @abstractmethod
    def get_data(self):
        """Method for reteiving data."""
    
    @abstractmethod
    def process_data(self):
        """Method to process the raw data."""
    
    @abstractmethod
    def prepare_data(self):
        """Method to prepare and normalize raw data."""
    
    @abstractmethod
    def send_prepared_data(self):
        """Method to send the prepared data."""

    def set_execution_flags(self, get_data = True, process_data = True, prepare_data = True, send_data = True):
        """WARNING: THIS METHOD SHOULD NOT BE OVERIDDEN!\n
        Sets the execution flags."""
        self.flags = get_data | (process_data << 1) | (prepare_data << 2) | (send_data << 3)
    
    def _should_execute(self, stage:ExecutionFlags) -> bool:
        """WARNING: INTERNAL METHOD - DO NOT OVERRIDE\n
        This method checks the execution flags to verify if a Data Process stage should execute."""
        return self.flags & stage.value

_DEFAULT_DATAPROCESSBASE = """import dataprocess as dp
class DefaultDataProcess(dp.DataProcessBase):
    def __init__(self):
        pass
    
    def get_data(self):
        \"\"\"Method for reteiving data.\"\"\"

    def process_data(self):
        \"\"\"Method to process the raw data.\"\"\"

    def prepare_data(self):
        \"\"\"Method to prepare and normalize raw data.\"\"\"

    def send_prepared_data(self):
        \"\"\"Method to send the prepared data.\"\"\"
"""

def generate_dataprocess(folder:str = None) -> str:
    """Generates a new .py file with an empty data process inherited from DataProcessBase"""
    import os

    fname = "new_dataprocess.py"
    fpath = os.path.join(folder,fname) if folder else fname
    i = 0

    while os.path.exists(fpath):
        i += 1
        fname = f"new_dataprocess({i}).py"
        fpath = os.path.join(folder,fname) if folder else fname
    
    with open(fpath, "w+") as f:
        f.write(_DEFAULT_DATAPROCESSBASE)
    
    return fpath