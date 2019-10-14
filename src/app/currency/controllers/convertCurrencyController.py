from aiohttp import web
from aiohttp_swagger import swagger_path


class ConvertCurrencyController(web.View):
    @swagger_path("swagger/convert_currency.yaml")
    async def get(self):
        return web.Response(text="Not implemented")
