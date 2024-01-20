from unittest.mock import MagicMock, call, patch

import pytest

from src.app.sync.main import handle_request
from .constant import HTTPStatus, HTTPTestRequests, HTTPTestResponses


@pytest.fixture
def mock_conn() -> MagicMock:
    conn = MagicMock()
    return conn


def test_hello(mock_conn: MagicMock) -> None:
    mock_conn.recv.return_value = HTTPTestRequests.HELLO.value.encode("utf-8")
    handle_request(mock_conn)
    assert mock_conn.sendall.call_args == call(HTTPTestResponses.HELLO.value)


def test_io_task(mock_conn: MagicMock) -> None:
    with patch("src.app.sync.main.time.sleep") as mock_sleep:
        mock_conn.recv.return_value = HTTPTestRequests.IO_TASK.value.encode("utf-8")
        handle_request(mock_conn)
        mock_sleep.assert_called_once_with(1)
        assert mock_conn.sendall.call_args == call(HTTPTestResponses.IO_TASK.value)


def test_cpu_task(mock_conn: MagicMock) -> None:
    mock_conn.recv.return_value = HTTPTestRequests.CPU_TASK.value.encode("utf-8")
    handle_request(mock_conn)
    expected_result = sum(i for i in range(10**6))
    expected_response = HTTPTestResponses.CPU_TASK.value.format(result=expected_result)
    assert mock_conn.sendall.call_args == call(expected_response.encode("utf-8"))


def test_random_sleep(mock_conn: MagicMock) -> None:
    with patch("src.app.sync.main.random.uniform", return_value=0.5) as mock_random:
        with patch("src.app.sync.main.time.sleep") as mock_sleep:
            mock_conn.recv.return_value = HTTPTestRequests.RANDOM_SLEEP.value.encode("utf-8")
            handle_request(mock_conn)
            assert mock_random.call_args == call(0.1, 1.0)
            assert mock_sleep.call_args == call(0.5)
            expected_response = HTTPTestResponses.RANDOM_SLEEP.value.format(sleep_time=0.5).encode("utf-8")
            assert mock_conn.sendall.call_args == call(expected_response)


def test_random_status(mock_conn: MagicMock) -> None:
    with patch("src.app.sync.main.random.choice", return_value=404) as mock_random:
        mock_conn.recv.return_value = HTTPTestRequests.RANDOM_STATUS.value.encode("utf-8")
        handle_request(mock_conn)
        assert mock_random.call_args == call([200, 404, 500])
        expected_response = HTTPTestResponses.RANDOM_STATUS.value.format(status_code=404, reason="Not Found").encode(
            "utf-8"
        )
        assert mock_conn.sendall.call_args == call(expected_response)


def test_chain(mock_conn: MagicMock) -> None:
    mock_conn.recv.return_value = HTTPTestRequests.CHAIN.value.encode("utf-8")
    handle_request(mock_conn)
    expected_calls = [
        call(HTTPTestResponses.CHAIN_STEP_1.value.encode("utf-8")),
        call(HTTPTestResponses.CHAIN_STEP_2.value.encode("utf-8")),
    ]
    mock_conn.sendall.assert_has_calls(expected_calls, any_order=False)


def test_error_test(mock_conn: MagicMock) -> None:
    mock_conn.recv.return_value = HTTPTestRequests.ERROR_TEST.value.encode("utf-8")
    handle_request(mock_conn)
    assert mock_conn.sendall.call_args == call(HTTPTestResponses.ERROR_TEST.value)


def test_not_found(mock_conn: MagicMock) -> None:
    mock_conn.recv.return_value = "GET /nonexistentpath HTTP/1.1\r\nHost: localhost\r\n\r\n".encode("utf-8")
    handle_request(mock_conn)
    expected_response = HTTPStatus.NOT_FOUND.value.encode("utf-8")
    assert mock_conn.sendall.call_args == call(expected_response)
