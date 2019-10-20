import json
from unittest import mock

import pytest
from app.data_providers.APIs.exchangeRate import ExchangeRateDataProvider
from app.entities.currencyExchangeEntity import CurrencyExchange
from app.shared.customExceptions import APIDataProviderException


def mockUrlopen(responseData, responseCode=None):
    responseCode = responseCode if responseCode is not None else 200
    urlOpenMocked = mock.Mock()
    urlOpenMocked.read.return_value = json.dumps(responseData)
    urlOpenMocked.getcode.return_value = responseCode
    return urlOpenMocked


@mock.patch("urllib.request.urlopen")
def test_exchangeCorrectRate(urlopenMocked):
    urlopenMocked.return_value = mockUrlopen(
        responseData={"rates": {"EUR": 1, "USD": 1, "PLN": 1, "CZK": 1}}
    )
    dataProvider = ExchangeRateDataProvider()
    data = dataProvider.obtainData()
    assert data == [
        CurrencyExchange(currency="EUR", value=1),
        CurrencyExchange(currency="USD", value=1),
        CurrencyExchange(currency="PLN", value=1),
        CurrencyExchange(currency="CZK", value=1),
    ]


@mock.patch("urllib.request.urlopen")
def test_exchangeFailRate(urlopenMocked):
    urlopenMocked.return_value = mockUrlopen(
        responseData={"rates": {"EUR": 1, "PLN": 1, "CZK": 1}}
    )
    dataProvider = ExchangeRateDataProvider()
    with pytest.raises(APIDataProviderException) as excinfo:
        data = dataProvider.obtainData()
    assert "Not found currency: USD in API response." == str(excinfo.value)


@mock.patch("urllib.request.urlopen")
def test_exchangeFailStatusCode(urlopenMocked):
    urlopenMocked.return_value = mockUrlopen(
        responseData={"rates": {"EUR": 1, "USD": 1, "PLN": 1, "CZK": 1}},
        responseCode=500,
    )
    dataProvider = ExchangeRateDataProvider()
    with pytest.raises(APIDataProviderException) as excinfo:
        data = dataProvider.obtainData()
    assert "Http status error." == str(excinfo.value)
