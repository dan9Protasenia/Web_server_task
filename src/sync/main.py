import socket
import time
import random
from constant import SyncHost, SyncPort, Path, HTTPStatus, HTTPResponses


def add_custom_header_middleware(response):
    headers_end = response.find("\r\n\r\n") + 2

    response = (
            response[:headers_end] +
            HTTPResponses.CUSTOM_HEADER.value +
            response[headers_end:]
    )
    return response


def handle_request(conn):
    request_data = conn.recv(1024).decode('utf-8')
    request = request_data.split('\n')
    path = request[0].split()[1]

    if path == Path.HELLO.value:
        response = HTTPResponses.HELLO.value

    elif path == Path.IO_TASK.value:
        time.sleep(1)
        response = HTTPResponses.IO_TASK.value

    elif path == Path.CPU_TASK.value:
        result = sum(i for i in range(10 ** 6))
        response = HTTPResponses.CPU_TASK.value.format(status=HTTPStatus.OK.value, result=result)

    elif path == Path.RANDOM_SLEEP.value:
        sleep_time = random.uniform(0.1, 1.0)
        time.sleep(sleep_time)
        response = HTTPResponses.RANDOM_SLEEP.value.format(status=HTTPStatus.OK.value, sleep_time=sleep_time)

    elif path == Path.RANDOM_STATUS.value:
        status_code = random.choice([200, 404, 500])
        reason = status_code_map[status_code]
        response = HTTPResponses.RANDOM_STATUS.value.format(status_code=status_code, reason=reason)

    elif path == Path.CHAIN.value:
        response = HTTPResponses.CHAIN_STEP_1.value
        conn.sendall(response.encode('utf-8'))
        time.sleep(0.5)
        response = HTTPResponses.CHAIN_STEP_2.value
        conn.sendall(response.encode('utf-8'))
        return

    elif path == Path.ERROR_TEST.value:
        response = HTTPResponses.ERROR_TEST.value

    else:
        response = HTTPResponses.NOT_FOUND_RESPONSE.value

    response = add_custom_header_middleware(response)
    conn.sendall(response.encode('utf-8'))
    conn.close()


status_code_map = {
    200: "OK",
    404: "Not Found",
    500: "Internal Server Error"
}


def start():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((SyncHost.LOCALHOST.value, SyncPort.PORT.value))
    sock.listen(1)
    print(f'Server listening on port {SyncPort.PORT.value}')

    while True:
        conn, addr = sock.accept()
        print(f"Address: {addr}, Port: {SyncPort.PORT.value}")
        handle_request(conn)


if __name__ == "__main__":
    start()
