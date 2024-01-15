import asyncio
import json
import random

from aiohttp import web

from .consant import HTTPResponse, Path, SyncHost, SyncPort


async def custom_header_middleware(app, handler):
    async def middleware_handler(request):
        response = await handler(request)
        response.headers["Custom-Header"] = HTTPResponse.CUSTOM_HEADER.value
        return response

    return middleware_handler


async def hello(request):
    return web.Response(text=HTTPResponse.HELLO.value)


async def echo(request):
    try:
        data = await request.json()
    except json.JSONDecodeError:
        raise web.HTTPBadRequest(text="Invalid JSON")

    return web.json_response(data)


async def io_task(request):
    await asyncio.sleep(1)

    return web.Response(text=HTTPResponse.IO_TASK.value)


async def cpu_task(request):
    result = sum(i for i in range(1000000))

    return web.Response(text=HTTPResponse.CPU_TASK.value.format(result=result))


async def random_sleep(request):
    sleep_time = random.uniform(0.1, 1.0)
    await asyncio.sleep(sleep_time)

    return web.Response(text=HTTPResponse.RANDOM_SLEEP.value.format(sleep_time=sleep_time))


async def random_status(request):
    statuses = [200, 404, 500]
    status = random.choice(statuses)

    return web.Response(status=status, text=HTTPResponse.RANDOM_STATUS.value.format(status=status))


async def chain(request):
    await asyncio.sleep(0.5)
    response_text = HTTPResponse.CHAIN_STEP_1.value
    await asyncio.sleep(0.5)
    response_text += HTTPResponse.CHAIN_STEP_2.value

    return web.Response(text=response_text)


async def handle_404(request):
    return web.Response(text=HTTPResponse.NOT_FOUND.value, status=404)


async def handle_500(request):
    return web.Response(text=HTTPResponse.ERROR_500.value, status=500)


async def error_test(request):
    raise web.HTTPInternalServerError(text=HTTPResponse.ERROR_TEST.value)


async def error_middleware(app, handler):
    async def middleware_handler(request):
        try:
            response = await handler(request)
            return response

        except web.HTTPException as ex:
            if ex.status == 404:
                return await handle_404(request)

            elif ex.status == 500:
                return await handle_500(request)
            raise

        except Exception as ex:
            print(f"Unexpected exception: {ex}")
            return await handle_500(request)

    return middleware_handler


async def create_app():
    app = web.Application(middlewares=[error_middleware, custom_header_middleware])
    app.router.add_get(Path.HELLO.value, hello)
    app.router.add_post(Path.ECHO.value, echo)
    app.router.add_get(Path.IO_TASK.value, io_task)
    app.router.add_get(Path.CPU_TASK.value, cpu_task)
    app.router.add_get(Path.RANDOM_SLEEP.value, random_sleep)
    app.router.add_get(Path.RANDOM_STATUS.value, random_status)
    app.router.add_get(Path.CHAIN.value, chain)
    app.router.add_get(Path.ERROR_TEST.value, error_test)

    return app


if __name__ == "__main__":
    app = web.run_app(create_app(), host=SyncHost.LOCALHOST.value, port=SyncPort.PORT.value)
