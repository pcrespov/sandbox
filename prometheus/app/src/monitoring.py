import prometheus_client
from aiohttp import web
from prometheus_client import Counter, Gauge, Histogram, CONTENT_TYPE_LATEST
import time


def middleware_factory(app_name):
    @web.middleware
    async def middlewave_handler(request, handler):
        request['start_time'] = time.time()
        request.app['REQUEST_IN_PROGRESS'].labels(
            app_name, request.path, request.method).inc()

        resp = await handler(request)

        resp_time = time.time() - request['start_time']
        request.app['REQUEST_LATENCY'].labels(
            app_name, request.path).observe(resp_time)
        request.app['REQUEST_IN_PROGRESS'].labels(
            app_name, request.path, request.method).dec()
        request.app['REQUEST_COUNT'].labels(
            app_name, request.method, request.path, resp.status).inc()

        return resp
    return middlewave_handler

async def metrics(request):
    resp = web.Response(body=prometheus_client.generate_latest())
    resp.content_type = CONTENT_TYPE_LATEST
    return resp


def setup_monitoring(app, app_name):

    # Total number of requests processed
    app['REQUEST_COUNT'] = Counter(
        'requests_total', 'Total Request Count',
        ['app_name', 'method', 'endpoint', 'http_status']
    )

    # Latency of a request in seconds
    app['REQUEST_LATENCY'] = Histogram(
        'request_latency_seconds', 'Request latency',
        ['app_name', 'endpoint']
    )

    # Number of requests in progress
    app['REQUEST_IN_PROGRESS']=Gauge(
        'requests_in_progress_total', 'Requests in progress',
        ['app_name', 'endpoint', 'method']
    )

    app.middlewares.insert(0, middleware_factory(app_name))
    app.router.add_get("/metrics", metrics)
