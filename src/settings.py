import os

ALLOWED_CURRENCIES = ["EUR", "USD", "PLN", "CZK"]

# Redis
REDIS_HOST = "localhost"
REDIS_PORT = 6379

# OpenExchangeRate
OER_URL = "https://openexchangerates.org/api"
OER_APP_ID = os.environ["OER_APP_ID"]
