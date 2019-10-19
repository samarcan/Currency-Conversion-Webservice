import settings
from aiohttp import web
from app import routes as currency_routes
from celery import Celery

app = web.Application()
app.add_routes(currency_routes.getRoutes())

celeryApp = Celery(
    "tasks",
    broker="redis://{host}:{port}".format(
        host=settings.REDIS_HOST, port=settings.REDIS_PORT
    ),
)
