from typing import List

from aiohttp import web
from aiohttp.web import RouteDef

from .controllers.convertCurrencyController import ConvertCurrencyController


def getRoutes() -> List[RouteDef]:
    return [web.view("/convert-currency", ConvertCurrencyController)]
