import dataprocess as dp

_process:dp.IDataProcess = None

class MockDataProcess(dp.DataProcessBase):
    def __init__(self, *args, **kwargs):
        for k,v in kwargs.items():
            self.__setattr__(k, v)
    
    def get_data(self):
        """Method for reteiving data."""
        test_g_current_process_equals_process()
        test_g_failed_processes_is_empty()
    
    def process_data(self):
        """Method to process the raw data."""
        dp.continue_on_fail()
        raise Exception("process_data exception.")
    
    def prepare_data(self):
        """Method to prepare and normalize raw data."""
        return True
    
    def send_prepared_data(self):
        """Method to send the prepared data."""
        return True

def setup():
    global _process
    _process = MockDataProcess()
    dp.register_process(_process)

def test_g_use_execution_flags():
    dp.use_execution_flags(False)

    if dp.g.USE_EXECUTION_FLAGS:
        raise AssertionError("g.USE_EXECUTION_FLAGS failed to update (False).")
    
    dp.use_execution_flags(True)

    if not dp.g.USE_EXECUTION_FLAGS:
        raise AssertionError("g.USE_EXECUTION_FLAGS failed to update (True).")
    
    print(f"Passed: test_g_use_execution_flags")
    
    

def test_g_current_process_equals_process():
    if dp.g.CURRENT_PROCESS != _process:
        raise AssertionError("Current process mismatch.")
    
    print(f"Passed: test_g_current_process_equals_process")

def test_g_failed_processes_is_empty():
    if len(dp.g.FAILED_PROCESSES):
        raise AssertionError("FAILED:test_g_failed_processes_is_empty::g.FAILED_PROCESSES was not empty.")
    
    print(f"Passed: test_g_failed_processes_is_empty")

def test_g_failed_processes_is_not_empty():
    if not len(dp.g.FAILED_PROCESSES):
        raise AssertionError("FAILED:test_g_failed_processes_is_empty::g.FAILED_PROCESSES was empty.")

    print(f"Passed: test_g_failed_processes_is_not_empty")
    
def main():
    setup()
    test_g_use_execution_flags()
    dp.run()
    test_g_failed_processes_is_not_empty()

if __name__ == "__main__":
    main()