import unittest
from unittest.mock import MagicMock, patch, call
from Web_server_task.src.sync.main import handle_request
from .constant import HTTPTestRequests, HTTPTestResponses, HTTPStatus


class TestSyncServer(unittest.TestCase):

    def setUp(self):
        self.conn = MagicMock()

    def test_hello(self):
        self.conn.recv.return_value = HTTPTestRequests.HELLO.value.encode('utf-8')
        handle_request(self.conn)
        self.conn.sendall.assert_called_with(HTTPTestResponses.HELLO.value)

    def test_io_task(self):
        with patch('Web_server_task.src.sync.main.time.sleep') as mock_sleep:
            self.conn.recv.return_value = HTTPTestRequests.IO_TASK.value.encode('utf-8')
            handle_request(self.conn)
            mock_sleep.assert_called_once_with(1)
            self.conn.sendall.assert_called_with(HTTPTestResponses.IO_TASK.value)

    def test_cpu_task(self):
        self.conn.recv.return_value = HTTPTestRequests.CPU_TASK.value.encode('utf-8')
        handle_request(self.conn)
        expected_result = sum(i for i in range(10 ** 6))
        expected_response = HTTPTestResponses.CPU_TASK.value.format(result=expected_result)
        self.conn.sendall.assert_called_with(expected_response.encode('utf-8'))

    def test_random_sleep(self):
        with patch('Web_server_task.src.sync.main.random.uniform', return_value=0.5) as mock_random:
            with patch('Web_server_task.src.sync.main.time.sleep') as mock_sleep:
                self.conn.recv.return_value = HTTPTestRequests.RANDOM_SLEEP.value.encode('utf-8')
                handle_request(self.conn)
                mock_random.assert_called_with(0.1, 1.0)
                mock_sleep.assert_called_with(0.5)
                expected_response = HTTPTestResponses.RANDOM_SLEEP.value.format(sleep_time=0.5).encode('utf-8')
                self.conn.sendall.assert_called_with(expected_response)

    def test_random_status(self):
        with patch('Web_server_task.src.sync.main.random.choice', return_value=404) as mock_random:
            self.conn.recv.return_value = HTTPTestRequests.RANDOM_STATUS.value.encode('utf-8')
            handle_request(self.conn)
            mock_random.assert_called_with([200, 404, 500])
            expected_response = HTTPTestResponses.RANDOM_STATUS.value.format(status_code=404, reason='Not Found').encode('utf-8')
            self.conn.sendall.assert_called_with(expected_response)

    def test_chain(self):
        self.conn.recv.return_value = HTTPTestRequests.CHAIN.value.encode('utf-8')
        handle_request(self.conn)
        self.conn.sendall.assert_has_calls([
            call(HTTPTestResponses.CHAIN_STEP_1.value.encode('utf-8')),
            call(HTTPTestResponses.CHAIN_STEP_2.value.encode('utf-8'))
        ])

    def test_error_test(self):
        self.conn.recv.return_value = HTTPTestRequests.ERROR_TEST.value.encode('utf-8')
        handle_request(self.conn)
        self.conn.sendall.assert_called_with(HTTPTestResponses.ERROR_TEST.value)

    def test_not_found(self):
        self.conn.recv.return_value = 'GET /nonexistentpath HTTP/1.1\r\nHost: localhost\r\n\r\n'.encode('utf-8')
        handle_request(self.conn)
        expected_response = HTTPStatus.NOT_FOUND.value.encode('utf-8')
        self.conn.sendall.assert_called_with(expected_response)


if __name__ == "__main__":
    unittest.main()
