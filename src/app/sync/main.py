import random
import signal
import socket
import sys
import time
import json

from urllib.parse import urlparse, parse_qs
from app.sync.constant import HTTPResponses, HTTPStatus, Path, SyncHost, SyncPort
from app.core.weather_api.weather_client import WeatherClient


def add_custom_header_middleware(response: str) -> str:
    headers_end = response.find("\r\n\r\n") + 2
    response = response[:headers_end] + HTTPResponses.CUSTOM_HEADER.value + response[headers_end:]
    return response


def handle_request(conn: socket.socket) -> None:
    request_data = conn.recv(1024).decode("utf-8")
    request = request_data.split("\n")
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
        conn.sendall(response.encode("utf-8"))
        time.sleep(0.5)
        response = HTTPResponses.CHAIN_STEP_2.value
        conn.sendall(response.encode("utf-8"))

    elif path == Path.ERROR_TEST.value:
        response = HTTPResponses.ERROR_TEST.value

    elif path.startswith(Path.WEATHER.value):
        query_params = parse_qs(urlparse(request[0]).query)
        latitude = query_params.get('latitude')
        longitude = query_params.get('longitude')

        if not latitude or not longitude:
            conn.sendall(HTTPResponses.BAD_REQUEST.value.encode("utf-8"))
            conn.close()

            return

        try:
            weather_client = WeatherClient()
            current_weather = weather_client.fetch_current_weather_sync(latitude=float(latitude[0]),
                                                                        longitude=float(longitude[0]))

            response_body = json.dumps(current_weather.dict())
            response = HTTPResponses.WEATHER_RESPONSE.value.format(status=HTTPStatus.OK.value, response_body=response_body)

        except Exception as e:
            print(f"Error fetching weather data: {e}")
            response = HTTPResponses.WEATHER_ERROR.value

    else:
        response = HTTPResponses.NOT_FOUND_RESPONSE.value

    response = add_custom_header_middleware(response)
    conn.sendall(response.encode("utf-8"))
    conn.close()


def close_server(sock: socket.socket) -> None:
    sock.close()
    print("Server closed")
    sys.exit(0)


def signal_handler(signum: int, frame) -> None:
    print(f"Received signal: {signum}")
    close_server(sock)


status_code_map = {200: "OK", 404: "Not Found", 500: "Internal Server Error"}


def start() -> None:
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((SyncHost.LOCALHOST.value, SyncPort.PORT.value))
    sock.listen(1)
    sock.settimeout(1)
    print(f"Server listening on port {SyncPort.PORT.value}")

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    try:
        while True:
            try:
                conn, addr = sock.accept()
            except socket.timeout:
                continue
            except KeyboardInterrupt:
                break
            else:
                handle_request(conn)
    finally:
        close_server(sock)


if __name__ == "__main__":
    start()
