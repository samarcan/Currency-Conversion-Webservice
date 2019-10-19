from app import celeryApp
from app.tasks.obtainExchangeRatesTask import obtainExchangeRatesTask


@celeryApp.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(5.0, celeryApp.task(obtainExchangeRatesTask).s(), name="")
