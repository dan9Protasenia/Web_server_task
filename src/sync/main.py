import socket
import time
import random
from constant import LOCAL_HOST_SYNC, port_sync


def add_custom_header_middleware(response):
    response += "\r\nX-Custom-Header: MyCustomHeader"
    return response


def handle_request(conn):
    request_data = conn.recv(1024).decode('utf-8')

    request = request_data.split('\n')
    path = request[0].split()[1]

    if path == "/hello":
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, World!"
    elif path == "/io_task":
        time.sleep(1)
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nI/O Task"
    elif path == "/cpu_task":
        result = sum(i for i in range(10 ** 6))
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nCPU Task: {result}"
    elif path == "/random_sleep":
        sleep_time = random.uniform(0.1, 1.0)
        time.sleep(sleep_time)
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nRandom Sleep: {sleep_time} seconds"
    elif path == "/random_status":
        status_code = random.choice([200, 404, 500])
        response = (f"HTTP/1.1 {status_code} {status_code_map[status_code]}"
                    f"\r\nContent-Type: text/plain\r\n\r\nRandom Status: {status_code}")
    elif path == "/chain":
        response1 = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nChain Step 1"
        conn.sendall(response1.encode('utf-8'))
        time.sleep(0.5)
        response2 = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nChain Step 2"
        conn.sendall(response2.encode('utf-8'))
        return
    elif path == "/error_test":
        response = "HTTP/1.1 500 Internal Server Error\r\nContent-Type: text/plain\r\n\r\nError Test"
    else:
        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n\r\n404 Not Found"

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
    sock.bind((LOCAL_HOST_SYNC, port_sync))
    sock.listen(1)
    print(f'Server listening on port {port_sync}')

    while True:
        conn, addr = sock.accept()
        print(f"Address: {addr}, Port: {port_sync}")
        handle_request(conn)


if __name__ == "__main__":
    start()
