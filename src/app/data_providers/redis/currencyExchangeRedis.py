from decimal import Decimal
from typing import Optional

from app.entities.currencyExchangeEntity import CurrencyExchange
from app.shared.redisInterface import RedisInterface


class CurrencyStorageRedis(RedisInterface):
    def getCurrency(self, currency: str) -> Optional[CurrencyExchange]:
        value = self.getKey(currency)
        if value:
            return CurrencyExchange(currency=currency, value=Decimal(value.decode()))
        else:
            return None

    def setCurrency(self, ce: CurrencyExchange):
        self.setKey(ce.currency, str(ce.value))