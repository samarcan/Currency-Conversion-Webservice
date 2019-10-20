import os

SERVER_PORT = os.environ.get("SERVER_PORT", 8080)
ALLOWED_CURRENCIES = ["EUR", "USD", "PLN", "CZK"]
BASE_CURRENCY = "USD"

# Redis
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)

# OpenExchangeRate
OER_URL = "https://openexchangerates.org/api"
OER_APP_ID = os.environ.get("OER_APP_ID", None)
