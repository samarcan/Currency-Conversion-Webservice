from aiohttp import web
from aiohttp_swagger import swagger_path


class ConversionController(web.View):
    @swagger_path("swagger/convert_currency.yaml")
    async def get(self):
        urlParams = dict(self.request.rel_url.query)
        return web.Response(text="Not implemented")
