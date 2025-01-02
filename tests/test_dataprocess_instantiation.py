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

class MockDataProcessComplex(dp.DataProcessBase):
    def __init__(self, prop1, prop2):
        self.prop1 = prop1
        self.prop2 = prop2
    
    def get_data(self):
        """Method for reteiving data."""
        return self.prop1
    
    def process_data(self):
        """Method to process the raw data."""
        return self.prop2
    
    def prepare_data(self):
        """Method to prepare and normalize raw data."""
        return self.prop1
    
    def send_prepared_data(self):
        """Method to send the prepared data."""
        return self.prop2

def setup():
    global _process
    _process = MockDataProcess()

def test_multiple_data_process_unique_kwargs():
    p1 = MockDataProcess(p1=True)
    p2 = MockDataProcess(p2=True)

    if not p1.__getattribute__("p1"):
        raise AssertionError("Multiple DataProcess instances do not have unique kwargs.")

    if not p2.__getattribute__("p2"):
        raise AssertionError("Multiple DataProcess instances do not have unique kwargs.")
    
    try:
        p1.__getattribute__("p2")
        raise AssertionError("Multiple DataProcess instances do not have unique kwargs.")
    except AttributeError:
        ...
    
    try:
        p2.__getattribute__("p1")
        raise AssertionError("Multiple DataProcess instances do not have unique kwargs.")
    except AttributeError:
        ...

    print(f"Passed: test_multiple_data_process_unique_kwargs", f"p1.p1: {p1.p1} p2.p2: {p2.p2}")

def test_complex_constructor():
    p = MockDataProcessComplex("Complex String", 42)
    p2 = MockDataProcessComplex(92, "Another String")

    print(p.prop1, p.prop2, p2.prop1, p2.prop2)

def test_dataprocess_adds_another():
    """"""
    dp.toggle_announce()
    class MockDataProcessAddsNewDataProcess(dp.DataProcessBase):
        def __init__(self, name:str, number:int):
            self.name = name
            self.number = number
            self.duplicate = False

        def get_data(self):
            """Method for reteiving data."""
            if self.number < 1:
                self.duplicate = True
            return True
        
        def process_data(self):
            """Method to process the raw data."""
            if self.duplicate:
                dp.register_process(MockDataProcessAddsNewDataProcess(self.name, self.number + 1))
            return True
        
        def prepare_data(self):
            """Method to prepare and normalize raw data."""
            if self.number == 1:
                print(f"Passed: test_dataprocess_adds_another")
            return True
        
        def send_prepared_data(self):
            """Method to send the prepared data."""
            return True
        
    dp.register_process(MockDataProcessAddsNewDataProcess("duplicate", 0))
    dp.run()
    dp.toggle_announce()


def main():
    setup()
    test_multiple_data_process_unique_kwargs()
    test_complex_constructor()
    test_dataprocess_adds_another()

if __name__ == "__main__":
    main()