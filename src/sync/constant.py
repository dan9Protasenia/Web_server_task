from enum import Enum


class SyncHost(Enum):
    LOCALHOST = 'localhost'


class SyncPort(Enum):
    PORT = 8001


class HTTPStatus(Enum):
    OK = "200 OK"
    NOT_FOUND = "404 Not Found"
    INTERNAL_SERVER_ERROR = "500 Internal Server Error"


class HTTPResponses(Enum):
    HELLO = f"HTTP/1.1 {HTTPStatus.OK.value}\r\nContent-Type: text/plain\r\n\r\nHello, World!"
    IO_TASK = f"HTTP/1.1 {HTTPStatus.OK.value}\r\nContent-Type: text/plain\r\n\r\nI/O Task"
    CPU_TASK = "HTTP/1.1 {status}\r\nContent-Type: text/plain\r\n\r\nCPU Task: {result}"
    RANDOM_SLEEP = "HTTP/1.1 {status}\r\nContent-Type: text/plain\r\n\r\nRandom Sleep: {sleep_time} seconds"
    RANDOM_STATUS = "HTTP/1.1 {status_code} {reason}\r\nContent-Type: text/plain\r\n\r\nRandom Status: {status_code}"
    CHAIN_STEP_1 = f"HTTP/1.1 {HTTPStatus.OK.value}\r\nContent-Type: text/plain\r\n\r\nChain Step 1"
    CHAIN_STEP_2 = f"HTTP/1.1 {HTTPStatus.OK.value}\r\nContent-Type: text/plain\r\n\r\nChain Step 2"
    ERROR_TEST = f"HTTP/1.1 {HTTPStatus.INTERNAL_SERVER_ERROR.value}\r\nContent-Type: text/plain\r\n\r\nError Test"
    NOT_FOUND_RESPONSE = f"HTTP/1.1 {HTTPStatus.NOT_FOUND.value}\r\nContent-Type: text/plain\r\n\r\n404 Not Found"
    CUSTOM_HEADER = "X-Custom-Header: MyCustomHeader\r\n"


class Path(Enum):
    HELLO = "/hello"
    IO_TASK = "/io_task"
    CPU_TASK = "/cpu_task"
    RANDOM_SLEEP = "/random_sleep"
    RANDOM_STATUS = "/random_status"
    CHAIN = "/chain"
    ERROR_TEST = "/error_test"
