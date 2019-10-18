import json
from decimal import Decimal
from typing import Dict
from urllib import request

import settings
from app.shared.customExceptions import APIDataProviderException


class ExchangeRateDataProvider:
    def __init__(self):
        self.allowedCurrencies = settings.ALLOWED_CURRENCIES
        self.urlBase = settings.OER_URL
        self.appId = settings.OER_APP_ID

    def obtainData(self) -> Dict[str, Decimal]:
        resp = self.__requestAPI(path="/latest.json")
        return self.__filterByCurrencies(resp)

    def __filterByCurrencies(self, resp: Dict) -> Dict:
        try:
            return {
                currency: Decimal(resp["rates"][currency])
                for currency in self.allowedCurrencies
            }
        except KeyError as e:
            raise APIDataProviderException(
                "Not found currency: %s in API response." % e.args[0]
            )

    def __requestAPI(self, path: str) -> Dict:
        url = "{urlBase}{path}?app_id={appId}".format(
            urlBase=self.urlBase, path=path, appId=self.appId
        )
        response = request.urlopen(url)
        if response.getcode() == 200:
            return json.loads(response.read())
        else:
            raise APIDataProviderException("Http status error.")
