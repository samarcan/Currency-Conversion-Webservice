from os import path

import settings
from aiohttp import web
from aiohttp_swagger import setup_swagger
from app import app

if __name__ == "__main__":
    setup_swagger(
        app, swagger_from_file=path.join(settings.PROJECT_DIR, "swagger.yaml")
    )
    web.run_app(app, port=settings.SERVER_PORT)
