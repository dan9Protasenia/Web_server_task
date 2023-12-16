import asyncio
import json
import random

from aiohttp import web

from consant import LOCAL_HOST, port


async def custom_header_middleware(app, handler):
    async def middleware_handler(request):
        response = await handler(request)
        response.headers['Custom-Header'] = 'MyCustomHeaderValue'
        return response

    return middleware_handler


async def hello(request):
    return web.Response(text="Hello, World!")


async def echo(request):
    try:
        data = await request.json()
    except json.JSONDecodeError:
        raise web.HTTPBadRequest(text="Invalid JSON")

    return web.json_response(data)


async def io_task(request):
    await asyncio.sleep(1)
    return web.Response(text="I/O Task Completed")


async def cpu_task(request):
    result = sum(i for i in range(1000000))
    return web.Response(text=f"CPU Task Completed: {result}")


async def random_sleep(request):
    sleep_time = random.uniform(0.1, 1.0)
    await asyncio.sleep(sleep_time)
    return web.Response(text=f"Slept for {sleep_time:.2f} seconds")


async def random_status(request):
    statuses = [200, 404, 500]
    status = random.choice(statuses)
    return web.Response(status=status, text=f"Random Status: {status}")


async def chain(request):
    await asyncio.sleep(0.5)
    response_text = "Chain Step 1\n"
    await asyncio.sleep(0.5)
    response_text += "Chain Step 2"
    return web.Response(text=response_text)


async def handle_404(request):
    return web.Response(text="404: Page not found", status=404)


async def handle_500(request):
    return web.Response(text="500: Internal Server Error", status=500)


async def error_test(request):
    raise web.HTTPInternalServerError(text="Internal Server Error for Test")


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
    app.router.add_get('/hello', hello)
    app.router.add_post('/echo', echo)
    app.router.add_get('/io_task', io_task)
    app.router.add_get('/cpu_task', cpu_task)
    app.router.add_get('/random_sleep', random_sleep)
    app.router.add_get('/random_status', random_status)
    app.router.add_get('/chain', chain)
    app.router.add_get('/error_test', error_test)
    return app


if __name__ == '__main__':
    app = web.run_app(create_app(), host=LOCAL_HOST, port=port)
