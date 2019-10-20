from decimal import Decimal
from unittest import mock

import pytest
from app.entities.currencyExchangeEntity import CurrencyExchange
from app.use_cases.updateCurrencyExchanges import UpdateCurrencyExchanges


@mock.patch("app.data_providers.APIs.exchangeRate.ExchangeRateDataProvider.obtainData")
@mock.patch(
    "app.data_providers.redis.currencyExchangeRedis.CurrencyStorageRedis.backup"
)
@mock.patch(
    "app.data_providers.redis.currencyExchangeRedis.CurrencyStorageRedis.setCurrency"
)
def test_successUpdateCurrencyExchanges(
    mockSetCurrency, mockRedisBackup, mockObtainData
):
    mockObtainData.return_value = [
        CurrencyExchange(currency="EUR", value=Decimal("1.2")),
        CurrencyExchange(currency="USD", value=Decimal("1")),
        CurrencyExchange(currency="CZK", value=Decimal("22.0")),
    ]
    uce = UpdateCurrencyExchanges()
    uce.update()
