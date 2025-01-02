# Filename: dataprocess_setup.py
# Author: Steven Barnes
# Date: 2024-12-31
# Description: Houses all the global package functions needed to use and
# interact with Data Process Framework (DPF).

# System Imports
from typing import Callable, Generator

# Package Imports
from .abstractions import IDataProcess
from . import ExecutionFlags, g

# Global variables
processes:list[IDataProcess] = []
# USE_EXECUTION_FLAGS = True
# g.update(USE_EXECUTION_FLAGS = USE_EXECUTION_FLAGS)


# Global Public functions
def use_execution_flags(use_flags:bool = True):
    # global USE_EXECUTION_FLAGS
    # USE_EXECUTION_FLAGS = use_flags
    # g.update(USE_EXECUTION_FLAGS = use_flags)
    g.USE_EXECUTION_FLAGS = use_flags

def continue_on_fail(contine_on_fail:bool = True):
    g.CONTINUE_ON_FAIL = contine_on_fail

def toggle_announce(announce:bool = not g.ANNOUNCE):
    g.ANNOUNCE = announce

def register_process(process:IDataProcess):
    """Register a process that implements the IDataProcess protocol."""
    if g.ANNOUNCE:
        print(f"Registering process: {type(process).__name__}")
    processes.append(process)

def announce_process(process:IDataProcess):
    announce_text = f"Running {type(process).__name__}..."
    rail = '-' * len(announce_text)

    print(rail)
    print(f"Running {type(process).__name__}...")
    print(rail)

def clear():
    processes.clear()
    if g.ANNOUNCE:
        print("All processes have been removed!")

def remove(process:IDataProcess):
    processes.remove(process)
    if g.ANNOUNCE:
        print(f"{type(process).__name__} has been removed!")

def get_failed_processes() -> list[str]:
    return g.FAILED_PROCESSES

# Global Private functions
def __execute_with_flags(process:IDataProcess):
    """Executes a DataProcess based on the execution flag settings."""
    if process._should_execute(ExecutionFlags.GET_DATA):
        process.get_data()
    if process._should_execute(ExecutionFlags.PROCESS_DATA):
        process.process_data()
    if process._should_execute(ExecutionFlags.PREPARE_DATA):
        process.prepare_data()
    if process._should_execute(ExecutionFlags.SEND_DATA):
        process.send_prepared_data()

def __execute_without_flags(process:IDataProcess):
    """Executes all the steps of a DataProcess."""
    process.get_data()
    process.process_data()
    process.prepare_data()
    process.send_prepared_data()

def __get_by_execution_flags(process:IDataProcess):
    """Yield each process step based on the execution flagging to be used when calling __execute_process_step."""
    if process._should_execute(ExecutionFlags.GET_DATA):
        yield process.get_data
    if process._should_execute(ExecutionFlags.PROCESS_DATA):
        yield process.process_data
    if process._should_execute(ExecutionFlags.PREPARE_DATA):
        yield process.prepare_data
    if process._should_execute(ExecutionFlags.SEND_DATA):
        yield process.send_prepared_data

def __get_without_flags(process:IDataProcess):
    """Yield each process step to be used when calling __execute_process_step."""
    yield process.get_data
    yield process.process_data
    yield process.prepare_data
    yield process.send_prepared_data

def __execute_process_step(fn:Callable):
    """Run the passed in process step and keep track if it fails."""
    try:
        retval = fn()
        return retval
    except Exception as e:
        """"""
        g.FAILED_PROCESSES.append(fn.__qualname__)        
        return e

def __execute_dataprocess(process:IDataProcess):
    """Execute the DataProcess.  Checks the g.CONTINUE_ON_FAIL flag to determine whether to raise Exceptions or not."""
    steps = __get_by_execution_flags if g.USE_EXECUTION_FLAGS else __get_without_flags

    for step in steps(process):
        retval = __execute_process_step(step)
        if isinstance(retval, Exception):
            if g.CONTINUE_ON_FAIL:
                return
            else:
                raise retval

# Execution point
def run():
    """
    Run all registered data processes.

    process.get_data()\n
    process.process_data()\n
    process.prepare_data()\n
    process.send_prepared_data()\n
    """
    g.FAILED_PROCESSES.clear()
    # run_fn = __execute_without_flags
    # if g.USE_EXECUTION_FLAGS:
    #     run_fn = __execute_with_flags
    while len(processes):
        # g.update(CURRENT_PROCESS=process)
        process = processes.pop(0)
        g.CURRENT_PROCESS = process
        if g.ANNOUNCE:
            announce_process(process)
        # run_fn(process)
        __execute_dataprocess(process)
    if g.ANNOUNCE:
        print("Finished running all registered data processes.")