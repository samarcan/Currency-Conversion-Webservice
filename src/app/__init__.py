from aiohttp import web
from app import routes as currency_routes

app = web.Application()
app.add_routes(currency_routes.getRoutes())
