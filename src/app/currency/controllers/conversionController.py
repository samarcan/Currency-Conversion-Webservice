from aiohttp import web
from aiohttp_swagger import swagger_path
from app.currency.serializers.conversionSerializer import ConversionSerializer
from schematics.exceptions import DataError


class ConversionController(web.View):
    @swagger_path("swagger/convert_currency.yaml")
    async def get(self):
        try:
            urlParams = dict(self.request.rel_url.query)
            conversionSerializer = ConversionSerializer(urlParams)
            conversionSerializer.validate()
            return web.Response(text="Not implemented")
        except DataError as e:
            validationErrors = {
                key: [error.summary for error in e.messages[key].errors]
                for key in e.messages.keys()
            }
            return web.json_response({"errors": validationErrors}, status=400)
