import settings
from app.shared.logger import getAppLogger
from app.use_cases.updateCurrencyExchanges import UpdateCurrencyExchanges


def obtainExchangeRatesTask():
    logger = getAppLogger(settings.CELERY_WORKER_NAME)
    logger.info("Starting celery task to obtain latest exchange rates")
    UpdateCurrencyExchanges(logger).update()
    logger.info("Finished celery task to obtain latest exchange rates")
