import settings
from app.shared.logger import getAppLogger
from app.use_cases.updateCurrencyExchanges import UpdateCurrencyExchanges


def obtainExchangeRatesTask():
    if settings.OER_APP_ID:
        logger = getAppLogger(settings.CELERY_WORKER_NAME)
        logger.info("Starting celery task to obtain latest exchange rates")
        UpdateCurrencyExchanges(logger).update()
        logger.info("Finished celery task to obtain latest exchange rates")
    else:
        logger.critical("OpenExchangeRates app id must be provided.")
