"""

https://github.com/amitsaha/python-prometheus-demo

https://blog.codeship.com/monitoring-your-asynchronous-python-web-applications-using-prometheus/
"""

from aiohttp import web
from monitoring import setup_monitoring

@web.middleware
async def error_middleware(request, handler):
    try:
        resp = await handler(request)
    except web.HTTPException as ex:
        resp = web.Response(body=str(ex), status=ex.status)
    except Exception as ex:
        resp = web.Response(body=str(ex), status=500)
    
    return resp


async def test(request: web.Request) -> web.Response:
    return web.Response(text=r'test')

async def test1(request):
    1/0

import sys

if __name__ == '__main__':
    app_name = sys.argv[1]
    
    app = web.Application(middlewares=[error_middleware])
    app.router.add_get('/test', test)
    app.router.add_get('/test1', test1)

    setup_monitoring(app, app_name)
    web.run_app(app, port=8080)
