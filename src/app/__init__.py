from aiohttp import web
from app.currency import routes as currency_routes

app = web.Application()
app.add_routes(currency_routes.getRoutes())
