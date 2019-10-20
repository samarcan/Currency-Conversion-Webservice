from aiohttp import web
from app.serializers.conversionSerializer import ConversionSerializer
from app.use_cases.conversion import Conversion
from schematics.exceptions import DataError


class ConversionController(web.View):
    async def get(self):
        urlParams = dict(self.request.rel_url.query)
        try:
            validatedData = self.__validateUrlParams(urlParams)
            return web.json_response(
                Conversion().convertCurrency(
                    initCurrencyName=validatedData["initial_currency"],
                    finalCurrencyName=validatedData["final_currency"],
                    amount=validatedData["amount"],
                )
            )
        except DataError as e:
            return web.json_response(
                {"errors": self.__obtainValidationErrors(e)}, status=400
            )
        except Exception:
            return web.json_response({"errors": ["Internal server error"]}, status=500)

    def __validateUrlParams(self, urlParams):
        conversionSerializer = ConversionSerializer(urlParams)
        conversionSerializer.validate()
        return conversionSerializer.to_native()

    def __obtainValidationErrors(self, e):
        return {
            key: [error.summary for error in e.messages[key].errors]
            for key in e.messages.keys()
        }
