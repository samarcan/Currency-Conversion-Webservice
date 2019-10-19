from decimal import Decimal
from typing import Dict


class CurrencyExchange:
    def __init__(self, currency: str = None, value: Decimal = None):
        self._currency = currency
        self._value = value

    @property
    def currency(self):
        return self._currency

    @property
    def value(self):
        return self._value

    def toDict(self) -> Dict:
        return {"currency": self.currency, "value": self.value}

    def fromDict(self, dictEntity):
        self._currency = dictEntity["currency"]
        self._value = dictEntity["value"]
        return self
