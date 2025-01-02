import dataprocess as dp

_process:dp.IDataProcess = None

class MockDataProcess(dp.DataProcessBase):
    def __init__(self, *args, **kwargs):
        for k,v in kwargs.items():
            self.__setattr__(k, v)
    
    def get_data(self):
        """Method for reteiving data."""
        return True
    
    def process_data(self):
        """Method to process the raw data."""
        return True
    
    def prepare_data(self):
        """Method to prepare and normalize raw data."""
        return True
    
    def send_prepared_data(self):
        """Method to send the prepared data."""
        return True

def setup():
    global _process
    _process = MockDataProcess()

def test_dataprocess_has_execution_flags():
    if _process.flags is None:
        raise AssertionError("Data Process flags do not exist.")
    print("Passed: test_dataprocess_has_execution_flags", _process.flags)

def test_data_process_execution_flag_get_data_true():
    if not _process._should_execute(dp.ExecutionFlags.GET_DATA):
        raise AssertionError("Data Process flag GET DATA not set.")
    print("Passed: test_data_process_execution_flag_get_data_true", dp.ExecutionFlags.GET_DATA)

def test_data_process_execution_flag_get_data_false():
    _process.set_execution_flags(get_data=False)
    if _process._should_execute(dp.ExecutionFlags.GET_DATA):
        raise AssertionError("Data Process flag GET DATA should not be set.")
    print("Passed: test_data_process_execution_flag_get_data_false", dp.ExecutionFlags.GET_DATA)

def test_multiple_data_process_unique_flags():
    p1 = MockDataProcess()
    p2 = MockDataProcess()

    p1.set_execution_flags(get_data=False)

    if p1.flags == p2.flags:
        raise AssertionError("Multiple DataProcess instances do not have unique flags.")
    print(f"Passed: test_multiple_data_process_unique_flags", f"p1: {p1.flags} p2: {p2.flags}")

def main():
    setup()
    test_dataprocess_has_execution_flags()
    test_data_process_execution_flag_get_data_true()
    test_data_process_execution_flag_get_data_false()
    test_multiple_data_process_unique_flags()

if __name__ == "__main__":
    main()
