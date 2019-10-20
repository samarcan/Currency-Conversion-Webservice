from typing import List

from app.data_providers.APIs.exchangeRate import ExchangeRateDataProvider
from app.data_providers.redis.currencyExchangeRedis import CurrencyStorageRedis
from app.entities.currencyExchangeEntity import CurrencyExchange
from app.shared.customExceptions import APIDataProviderException


class UpdateCurrencyExchanges:
    def __init__(self, logger):
        self._logger = logger
        self._currencyStorage = CurrencyStorageRedis(self._logger)
        self._erDataprovider = ExchangeRateDataProvider(self._logger)

    def update(self):
        exchangerates = self.__obtainExchangesRates()
        self.__storeExchangesRates(exchangerates)

    def __obtainExchangesRates(self) -> List[CurrencyExchange]:
        exchangeRates: List[CurrencyExchange] = []
        try:
            exchangerates = self._erDataprovider.obtainData()
        except APIDataProviderException as e:
            self._logger.error(e)
        return exchangerates

    def __storeExchangesRates(self, exchangerates: List[CurrencyExchange]):
        for er in exchangerates:
            self._currencyStorage.setCurrency(er)
        self._currencyStorage.backup()
