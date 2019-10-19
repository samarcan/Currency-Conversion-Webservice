import settings
from redis import Redis


class RedisInterface:
    def __init__(self):
        self._conn = self.connect()

    def setKey(self, key, value):
        self._conn.set(key, value)

    def getKey(self, key):
        return self._conn.get(key)

    def backup(self):
        self._conn.bgsave()

    def connect(self):
        return Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
