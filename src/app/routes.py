from typing import List

from aiohttp import web
from aiohttp.web import RouteDef
from app.controllers.conversionController import ConversionController


def getRoutes() -> List[RouteDef]:
    return [web.view("/convert-currency", ConversionController)]
