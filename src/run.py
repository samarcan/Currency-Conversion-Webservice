import settings
from aiohttp import web
from aiohttp_swagger import setup_swagger
from app import app

if __name__ == "__main__":
    setup_swagger(app, swagger_from_file="src/swagger.yaml")
    web.run_app(app, port=settings.SERVER_PORT)
