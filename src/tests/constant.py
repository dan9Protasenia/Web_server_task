from enum import Enum


class HTTPStatus(Enum):
    OK = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nX-Custom-Header: MyCustomHeader\r\n\r\n200 OK"
    NOT_FOUND = (
        "HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\nX-Custom-Header: MyCustomHeader\r\n\r\n404 Not Found"
    )
    INTERNAL_SERVER_ERROR = "HTTP/1.1 500 Internal Server Error\r\nContent-Type: text/plain\r\nX-Custom-Header: MyCustomHeader\r\n\r\n500 Internal Server Error"


class HTTPTestRequests(Enum):
    HELLO = "GET /hello HTTP/1.1\r\nHost: localhost\r\n\r\n"
    IO_TASK = "GET /io_task HTTP/1.1\r\nHost: localhost\r\n\r\n"
    CPU_TASK = "GET /cpu_task HTTP/1.1\r\nHost: localhost\r\n\r\n"
    RANDOM_SLEEP = "GET /random_sleep HTTP/1.1\r\nHost: localhost\r\n\r\n"
    RANDOM_STATUS = "GET /random_status HTTP/1.1\r\nHost: localhost\r\n\r\n"
    CHAIN = "GET /chain HTTP/1.1\r\nHost: localhost\r\n\r\n"
    ERROR_TEST = "GET /error_test HTTP/1.1\r\nHost: localhost\r\n\r\n"


class HTTPTestResponses(Enum):
    HELLO = b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nX-Custom-Header: MyCustomHeader\r\n\r\nHello, World!"
    IO_TASK = b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nX-Custom-Header: MyCustomHeader\r\n\r\nI/O Task"
    CPU_TASK = (
        "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nX-Custom-Header: MyCustomHeader\r\n\r\nCPU Task: {result}"
    )
    RANDOM_SLEEP = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nX-Custom-Header: MyCustomHeader\r\n\r\nRandom Sleep: {sleep_time} seconds"
    RANDOM_STATUS = "HTTP/1.1 {status_code} {reason}\r\nContent-Type: text/plain\r\nX-Custom-Header: MyCustomHeader\r\n\r\nRandom Status: {status_code}"
    CHAIN_STEP_1 = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nChain Step 1"
    CHAIN_STEP_2 = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nChain Step 2"
    ERROR_TEST = b"HTTP/1.1 500 Internal Server Error\r\nContent-Type: text/plain\r\nX-Custom-Header: MyCustomHeader\r\n\r\nError Test"
