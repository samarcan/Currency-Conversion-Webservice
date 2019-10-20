from decimal import Decimal
from unittest import mock

import pytest
from app.entities.currencyExchangeEntity import CurrencyExchange
from app.shared.customExceptions import RedisDataProviderException
from app.use_cases.conversion import Conversion


@mock.patch(
    "app.data_providers.redis.currencyExchangeRedis.CurrencyStorageRedis.getCurrency"
)
def test_correctConversion(mockRedisGetCurrency):
    mockRedisGetCurrency.side_effect = [
        CurrencyExchange(currency="USD", value=Decimal("1")),
        CurrencyExchange(currency="EUR", value=Decimal("0.895656")),
        CurrencyExchange(currency="CZK", value=Decimal("22.9534")),
    ]
    result = Conversion().convertCurrency("EUR", "CZK", Decimal(1))
    assert result == {
        "base_currency": "USD",
        "initial_currency": "EUR",
        "initial_currency_exchange_rate": 0.9,
        "final_currency": "CZK",
        "final_currency_exchange_rate": 22.95,
        "initial_amount": 1,
        "conversion_result": 25.63,
    }


@mock.patch(
    "app.data_providers.redis.currencyExchangeRedis.CurrencyStorageRedis.getCurrency"
)
def test_failConversion(mockRedisGetCurrency):
    mockRedisGetCurrency.side_effect = [
        CurrencyExchange(currency="USD", value=Decimal("1")),
        CurrencyExchange(currency="EUR", value=Decimal("0.895656")),
        RedisDataProviderException("Currency does not exist."),
    ]
    with pytest.raises(RedisDataProviderException) as excinfo:
        result = Conversion().convertCurrency("EUR", "OOO", Decimal(1))
    assert "Currency does not exist." == str(excinfo.value)
