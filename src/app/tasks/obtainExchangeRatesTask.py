from app.use_cases.updateCurrencyExchanges import UpdateCurrencyExchanges


def obtainExchangeRatesTask():
    uce = UpdateCurrencyExchanges()
    uce.update()
