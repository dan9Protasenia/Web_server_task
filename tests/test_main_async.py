from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from aiohttp.web import Application

from ..src.app.async_main.main import create_app


class MyAppTestCase(AioHTTPTestCase):
    async def get_application(self) -> Application:
        return await create_app()

    @unittest_run_loop
    async def test_hello(self) -> None:
        request = await self.client.request("GET", "/hello")
        assert request.status == 200
        text = await request.text()
        assert text == "Hello, World!"

    @unittest_run_loop
    async def test_echo(self) -> None:
        data = {"test": "data"}
        request = await self.client.post("/echo", json=data)
        assert request.status == 200
        json_response = await request.json()
        assert json_response == data

    @unittest_run_loop
    async def test_io_task(self) -> None:
        request = await self.client.request("GET", "/io_task")
        assert request.status == 200
        text = await request.text()
        assert text == "I/O Task Completed"

    @unittest_run_loop
    async def test_cpu_task(self) -> None:
        request = await self.client.request("GET", "/cpu_task")
        assert request.status == 200
        text = await request.text()
        assert "CPU Task Completed" in text

    @unittest_run_loop
    async def test_random_sleep(self) -> None:
        request = await self.client.request("GET", "/random_sleep")
        assert request.status == 200
        text = await request.text()
        assert text.startswith("Slept for")

    @unittest_run_loop
    async def test_random_status(self) -> None:
        request = await self.client.request("GET", "/random_status")
        assert request.status in [200, 404, 500]

    @unittest_run_loop
    async def test_chain(self) -> None:
        request = await self.client.request("GET", "/chain")
        assert request.status == 200
        text = await request.text()
        assert text.strip().endswith("Chain Step 2")

    @unittest_run_loop
    async def test_error_test(self) -> None:
        request = await self.client.request("GET", "/error_test")
        assert request.status == 500
        text = await request.text()
        assert text == "500: Internal Server Error"
