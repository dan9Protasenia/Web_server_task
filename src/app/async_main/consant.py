from enum import Enum


class SyncHost(Enum):
    LOCALHOST = "localhost"


class SyncPort(Enum):
    PORT = 8002


class HTTPResponse(Enum):
    HELLO = "Hello, World!"
    IO_TASK = "I/O Task Completed"
    CPU_TASK = "CPU Task Completed: {result}"
    RANDOM_SLEEP = "Slept for {sleep_time:.2f} seconds"
    RANDOM_STATUS = "Random Status: {status}"
    CHAIN_STEP_1 = "Chain Step 1\n"
    CHAIN_STEP_2 = "Chain Step 2\n"
    ERROR_TEST = "Internal Server Error for Test"
    NOT_FOUND = "404: Page not found"
    ERROR_500 = "500: Internal Server Error"
    CUSTOM_HEADER = "MyCustomHeaderValue"


class Path(Enum):
    HELLO = "/hello"
    ECHO = "/echo"
    IO_TASK = "/io_task"
    CPU_TASK = "/cpu_task"
    RANDOM_SLEEP = "/random_sleep"
    RANDOM_STATUS = "/random_status"
    CHAIN = "/chain"
    ERROR_TEST = "/error_test"
    WEATHER = "/weather"
