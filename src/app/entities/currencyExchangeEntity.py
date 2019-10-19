from decimal import Decimal
from typing import Dict, Optional


class CurrencyExchange:
    def __init__(self, currency: str = None, value: Decimal = None):
        self._currency = currency
        self._value = value

    @property
    def currency(self) -> Optional[str]:
        return self._currency

    @property
    def value(self) -> Optional[Decimal]:
        return self._value

    def toDict(self) -> Dict:
        return {"currency": self.currency, "value": self.value}

    def fromDict(self, dictEntity) -> CurrencyExchange:
        self._currency = dictEntity["currency"]
        self._value = dictEntity["value"]
        return self

    def __eq__(self, entity) -> bool:
        return self.value == entity.value and self.currency == entity.currency
