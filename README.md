# Data Process Framework (v0.2.2)

## Usage

`import dataprocess`

`dataprocess.register_process(your_process)`

`dataprocess.run()`

## Rundown

The dataprocess works by creating classes that implement the `IDataProcess` protocol.  These include the methods:

- `get_data()`
- `process_data()`
- `prepare_data()`
- `send_prepared_data()`

It is recommended to inherit from the provided base class `DataProcessbase`.

You may exclude a Data Process Stage from executing with the provided method `set_execution_flags()`.  This should assist with development and debugging.

eg. `MyDataProcess.set_execution_flags(get_data=False)`

How and what your implemntations do in the methods is totally up to you.  Some pre-defined utility classes are created to use the Strategy pattern.

- `StrategyDataRetreiver`
- `StrategyDataUpdater`
- `StrategyDataProcessor`

Each of these utility classes has a method `with_strategy(strategy)` which takes in a strategy implemntation for the respective utility:

- `IDataRetreiveStrategy`
- `IDataUpdateStrategy`
- `IDataProcessorStrategy`

### Execution Flags

Execution flags are on by default.  

- Turn off: `dataprocess.use_execution_flags(False)`
- Turn On: `dataprocess.use_execution_flags(True)` or `dataprocess.use_execution_flags()`

Excution flag values are:

- 0b0001 = GET_DATA
- 0b0010 = PROCESS_DATA
- 0b0100 = PREPARE_DATA
- 0b1000 = SEND_DATA

`DataProcessBase` automatically sets all flags on instantiation.  `set_execution_flags()` updates the flags using bitwise OR.

### IDataRetreiveStrategy Methods

- `get_data()`

### IDataUpdateStrategy Methods

- `prepare_updates()`
- `send_updates()`

### IDataProcessorStrategy Methods

- `process_data()`

## Example

    import dataprocess

    class MyDataProcess(dataprocess.DataProcessBase):

        def __init__(self):
            self.retreiver = dataprocess.StrategyDataRetreiver()
            self.processor = dataprocess.StrategyDataProcessor()
            self.updater = dataprocess.StrategyDataUpdater()

        def get_data(self):
            strategy = MyDataRetreiveStrategy(data_credentials)
            self.raw_data = self.retreiver.with_strategy(strategy).get_data()

        def process_data(self):
            strategy = MyDataProcessorStrategy(self.raw_data)
            self.processed_data = self.processor.with_strategy(strategy).process_data()

        def prepare_data(self):
            strategy = MyDataUpdatePrepareStrategy(self.processed_data)
            self.prepared_data = self.updater.with_strategy(strategy).prepare_data()

        def send_prepared_data(self):
            strategy = MyDataUpdateSendStrategy(self.prepared_data, data_credentials)
            self.updater.with_strategy(strategy).send_updates()


    class MyDataRetreiveStrategy:

        def __init__(self, data_credentials):
            self.data_credentials = data_credentials

        def get_data(self):
            conn = datastre.connect(self.data_credentials)
            raw_data = conn.get_raw_data()
            return raw_data

    class MyDataProcessorStrategy:

        def __init__(self, raw_data):
            self.raw_data = raw_data

        def process_data(self):
            data = pd.DataFrame.from_records(self.raw_data)
            return self._normalize_data(data)

        def _normalize_data(self, data):
            """Some actions to normalize the data."

    class MyDataUpdatePrepareStrategy:

        def __init__(self, processed_data):
            self.processed_data = processed_data

        def prepare_updates(self):
            """Some actions to prepare the data for sending."

    class MyDataUpdateSendStrategy:
        def __init__(self, send_data):
            self.send_data = send_data

        def send_updates(self):
            """Some actions to send the prepared data."""

    def main():
        dataprocess.register_process(MyDataProcess())
        dataprocess.run()

    if __name__ == "__main__":
        main()

## Create and Use Package

After cloning this repo onto your machine, create the package from the command line with:

```shell
python setup.py bdist_wheel clean
```

You may need to install `wheel` first: `pip install wheel`

The resulting `.whl` file in the `dist` folder can then be moved into your project and installed like any other Python package using the `pip install` command.

## Attributions

Steven Barnes
Magdiel Delgadillo