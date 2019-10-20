from decimal import Decimal
from unittest import mock

import pytest
from app.entities.currencyExchangeEntity import CurrencyExchange
from app.shared.logger import getAppLogger
from app.use_cases.updateCurrencyExchanges import UpdateCurrencyExchanges


@pytest.fixture
def logger():
    return getAppLogger("test_updateCurrencyExchanges")


@mock.patch("app.data_providers.APIs.exchangeRate.ExchangeRateDataProvider.obtainData")
@mock.patch(
    "app.data_providers.redis.currencyExchangeRedis.CurrencyStorageRedis.backup"
)
@mock.patch(
    "app.data_providers.redis.currencyExchangeRedis.CurrencyStorageRedis.setCurrency"
)
def test_successUpdateCurrencyExchanges(
    mockSetCurrency, mockRedisBackup, mockObtainData, logger
):
    mockObtainData.return_value = [
        CurrencyExchange(currency="EUR", value=Decimal("1.2")),
        CurrencyExchange(currency="USD", value=Decimal("1")),
        CurrencyExchange(currency="CZK", value=Decimal("22.0")),
    ]
    uce = UpdateCurrencyExchanges(logger)
    uce.update()
