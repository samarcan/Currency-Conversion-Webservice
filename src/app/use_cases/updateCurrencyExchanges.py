from typing import List

from app.data_providers.APIs.exchangeRate import ExchangeRateDataProvider
from app.data_providers.redis.currencyExchangeRedis import CurrencyStorageRedis
from app.entities.currencyExchangeEntity import CurrencyExchange


class UpdateCurrencyExchanges:
    def __init__(self):
        self._currencyStorage = CurrencyStorageRedis()
        self._erDataprovider = ExchangeRateDataProvider()

    def update(self):
        exchangerates = self.__obtainExchangesRates()
        self.__storeExchangesRates(exchangerates)

    def __obtainExchangesRates(self) -> List[CurrencyExchange]:
        return self._erDataprovider.obtainData()

    def __storeExchangesRates(self, exchangerates: List[CurrencyExchange]):
        for er in exchangerates:
            self._currencyStorage.setCurrency(er)
        self._currencyStorage.backup()
