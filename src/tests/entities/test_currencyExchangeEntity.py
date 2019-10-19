from decimal import Decimal

import pytest
from app.entities.currencyExchangeEntity import CurrencyExchange


def test_setCurrencyExchangeEntity():
    eurExchange = CurrencyExchange(currency="EUR", value=Decimal(1.2))
    assert type(eurExchange) == CurrencyExchange
    assert eurExchange.value == Decimal(1.2)
    assert eurExchange.currency == "EUR"


def test_toDict_CurrencyExchangeEntity():
    eurExchange = CurrencyExchange(currency="EUR", value=Decimal(1.2))
    assert eurExchange.toDict() == {"currency": "EUR", "value": Decimal(1.2)}


def test_fromDict_CurrencyExchangeEntity():
    dictEntity = {"currency": "EUR", "value": Decimal(1.2)}
    eurExchange = CurrencyExchange().fromDict(dictEntity)
    assert type(eurExchange) == CurrencyExchange
    assert eurExchange.value == Decimal(1.2)
    assert eurExchange.currency == "EUR"
