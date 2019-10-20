import json

import settings
from aiohttp import web
from app.serializers.conversionSerializer import ConversionSerializer
from app.shared.logger import getAppLogger
from app.use_cases.conversion import Conversion
from schematics.exceptions import DataError


class ConversionController(web.View):
    def __init__(self, *args, **kwargs):
        self._logger = getAppLogger(settings.WEBSERVICE_NAME)
        super().__init__(*args, **kwargs)

    async def get(self):
        urlParams = dict(self.request.rel_url.query)
        self._logger.info("Receive input: %s" % json.dumps(urlParams))
        try:
            validatedData = self.__validateUrlParams(urlParams)
            self._logger.debug("Data validated: %s" % json.dumps(urlParams))
            response = Conversion(self._logger).convertCurrency(
                initCurrencyName=validatedData["initial_currency"],
                finalCurrencyName=validatedData["final_currency"],
                amount=validatedData["amount"],
            )
            self._logger.debug("Reponse: %s" % json.dumps(response))
            return web.json_response(response)
        except DataError as e:
            errorResponse = {"errors": self.__obtainValidationErrors(e)}
            self._logger.error("Input error: %s" % json.dumps(errorResponse))
            return web.json_response(errorResponse, status=400)
        except Exception as e:
            self._logger.critical("Server error: %s" % str(e))
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
