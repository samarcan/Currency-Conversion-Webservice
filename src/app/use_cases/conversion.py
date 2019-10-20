from decimal import ROUND_HALF_UP, Decimal
from typing import Dict

import settings
from app.data_providers.redis.currencyExchangeRedis import CurrencyStorageRedis
from app.entities.currencyExchangeEntity import CurrencyExchange
from app.shared.customExceptions import RedisDataProviderException


class Conversion:
    def __init__(self, logger):
        self._logger = logger
        self._currencyStorage = CurrencyStorageRedis(self._logger)
        self._baseCurrency = self.__getExchangeRate(settings.BASE_CURRENCY)

    def convertCurrency(
        self, initCurrencyName: str, finalCurrencyName: str, amount: Decimal
    ) -> Dict:
        initCurrency = self.__getExchangeRate(initCurrencyName)
        finalCurrency = self.__getExchangeRate(finalCurrencyName)
        conversionResult = self.__makeConversion(initCurrency, finalCurrency, amount)
        return self.__prepareResponse(
            initCurrency, finalCurrency, amount, conversionResult
        )

    def __makeConversion(
        self,
        initCurrency: CurrencyExchange,
        finalCurrency: CurrencyExchange,
        amount: Decimal,
    ) -> Decimal:
        return (
            amount * self._baseCurrency.value / initCurrency.value * finalCurrency.value
        )

    def __getExchangeRate(self, currencyName: str) -> CurrencyExchange:
        return self._currencyStorage.getCurrency(currencyName)

    def __roundDecimal(self, decimalNumber: Decimal) -> float:
        return float(decimalNumber.quantize(Decimal(".01"), ROUND_HALF_UP))

    def __prepareResponse(
        self,
        initCurrency: CurrencyExchange,
        finalCurrency: CurrencyExchange,
        amount: Decimal,
        conversionResult: Decimal,
    ) -> Dict:
        return {
            "base_currency": self._baseCurrency.currency,
            "initial_currency": initCurrency.currency,
            "initial_currency_exchange_rate": self.__roundDecimal(initCurrency.value),
            "final_currency": finalCurrency.currency,
            "final_currency_exchange_rate": self.__roundDecimal(finalCurrency.value),
            "initial_amount": self.__roundDecimal(amount),
            "conversion_result": self.__roundDecimal(conversionResult),
        }
