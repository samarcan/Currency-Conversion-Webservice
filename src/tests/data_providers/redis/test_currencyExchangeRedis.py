from decimal import Decimal
from unittest import mock

import fakeredis
import pytest
from app.data_providers.redis.currencyExchangeRedis import CurrencyStorageRedis
from app.entities.currencyExchangeEntity import CurrencyExchange
from app.shared.customExceptions import RedisDataProviderException
from app.shared.logger import getAppLogger


@pytest.fixture
def logger():
    return getAppLogger("test_currencyExchangeRedis")


@pytest.fixture
def fakeRedisClient():
    fakeRedisClient = fakeredis.FakeStrictRedis()
    fakeRedisClient.set("EUR", "2.22")
    return fakeRedisClient


@mock.patch(
    "app.data_providers.redis.currencyExchangeRedis.CurrencyStorageRedis.connect"
)
def test_getCurrencyExchangeRedis(mockRedisConnection, fakeRedisClient, logger):
    mockRedisConnection.return_value = fakeRedisClient
    currencyStorageRedis = CurrencyStorageRedis(logger)
    currency = currencyStorageRedis.getCurrency("EUR")
    assert currency == CurrencyExchange("EUR", Decimal("2.22"))
    with pytest.raises(RedisDataProviderException) as excinfo:
        currency = currencyStorageRedis.getCurrency("OPL")
    assert "Currency does not exist." == str(excinfo.value)


@mock.patch(
    "app.data_providers.redis.currencyExchangeRedis.CurrencyStorageRedis.connect"
)
def test_setCurrencyExchangeRedis(mockRedisConnection, fakeRedisClient, logger):
    mockRedisConnection.return_value = fakeRedisClient
    currency = CurrencyExchange("USD", Decimal("1.22"))
    currencyStorageRedis = CurrencyStorageRedis(logger)
    currencyStorageRedis.setCurrency(currency)
