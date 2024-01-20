import asyncio
import json
import random

from aiohttp import web
from aiohttp.web import (
    Application,
    HTTPBadRequest,
    HTTPException,
    HTTPInternalServerError,
    Request,
    Response,
    json_response,
)

from ..core.enums.consant_async import HTTPResponse, Path, SyncHost, SyncPort
from ..core.modules.weather_client import WeatherClient


async def custom_header_middleware(app: Application, handler) -> Response:
    async def middleware_handler(request: Request) -> Response:
        response = await handler(request)
        response.headers["Custom-Header"] = HTTPResponse.CUSTOM_HEADER.value
        return response

    return middleware_handler


async def hello(request: Request) -> Response:
    return Response(text=HTTPResponse.HELLO.value)


async def echo(request: Request) -> Response:
    try:
        data = await request.json()
    except json.JSONDecodeError:
        raise HTTPBadRequest(text="Invalid JSON")

    return json_response(data)


async def io_task(request: Request) -> Response:
    await asyncio.sleep(1)

    return Response(text=HTTPResponse.IO_TASK.value)


async def cpu_task(request: Request) -> Response:
    result = sum(i for i in range(1000000))

    return Response(text=HTTPResponse.CPU_TASK.value.format(result=result))


async def random_sleep(request: Request) -> Response:
    sleep_time = random.uniform(0.1, 1.0)
    await asyncio.sleep(sleep_time)

    return Response(text=HTTPResponse.RANDOM_SLEEP.value.format(sleep_time=sleep_time))


async def random_status(request: Request) -> Response:
    statuses = [200, 404, 500]
    status = random.choice(statuses)

    return Response(status=status, text=HTTPResponse.RANDOM_STATUS.value.format(status=status))


async def chain(request: Request) -> Response:
    await asyncio.sleep(0.5)
    response_text = HTTPResponse.CHAIN_STEP_1.value
    await asyncio.sleep(0.5)
    response_text += HTTPResponse.CHAIN_STEP_2.value

    return Response(text=response_text)


async def handle_404(request: Request) -> Response:
    return Response(text=HTTPResponse.NOT_FOUND.value, status=404)


async def handle_500(request: Request) -> Response:
    return Response(text=HTTPResponse.ERROR_500.value, status=500)


async def error_test(request: Request) -> Response:
    raise HTTPInternalServerError(text=HTTPResponse.ERROR_TEST.value)


async def error_middleware(app: Application, handler) -> Response:
    async def middleware_handler(request: Request) -> Response:
        try:
            response = await handler(request)

        except HTTPException as ex:
            if ex.status == 404:
                response = await handle_404(request)
            elif ex.status == 500:
                response = await handle_500(request)
            else:
                raise

        except Exception as ex:
            print(f"Unexpected exception: {ex}")
            response = await handle_500(request)

        return response

    return middleware_handler


async def weather(request: Request) -> Request:
    latitude = request.query.get("latitude")
    longitude = request.query.get("longitude")

    if not latitude or not longitude:
        raise HTTPBadRequest(reason="Missing latitude or longitude parameter")

    try:
        weather_client = WeatherClient()
        current_weather = await weather_client.fetch_current_weather_async(
            latitude=float(latitude), longitude=float(longitude)
        )
        return json_response(current_weather.dict())
    except Exception as e:
        print(f"Error fetching weather data: {e}")

        raise HTTPInternalServerError()


async def create_app() -> Application:
    app = Application(middlewares=[error_middleware, custom_header_middleware])
    app.router.add_get(Path.HELLO.value, hello)
    app.router.add_post(Path.ECHO.value, echo)
    app.router.add_get(Path.IO_TASK.value, io_task)
    app.router.add_get(Path.CPU_TASK.value, cpu_task)
    app.router.add_get(Path.RANDOM_SLEEP.value, random_sleep)
    app.router.add_get(Path.RANDOM_STATUS.value, random_status)
    app.router.add_get(Path.CHAIN.value, chain)
    app.router.add_get(Path.ERROR_TEST.value, error_test)
    app.router.add_get(Path.WEATHER.value, weather)

    return app


if __name__ == "__main__":
    app = web.run_app(create_app(), host=SyncHost.LOCALHOST.value, port=SyncPort.PORT.value)
