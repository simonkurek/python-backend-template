import pkgutil

from fastapi import FastAPI
from tortoise.contrib.starlette import register_tortoise

from app.main import logger

from app.config.db import TortoiseSettings

from app.core import routers


def init(app: FastAPI):
    """
    Init routers and etc.
    :return:
    """
    init_routers(app)
    init_db(app)


def init_db(app: FastAPI):
    """
    Init database models.
    :param app:
    :return:
    """
    logger.info("Initializing database connection...")

    tortoise_settings = TortoiseSettings()

    register_tortoise(
        app,
        db_url=tortoise_settings.db_url,
        generate_schemas=tortoise_settings.generate_schemas,
        modules=tortoise_settings.modules,
    )

    logger.success("Database successfully initialized!")


def init_routers(app: FastAPI):
    """
    Initialize routers defined in `app.api`
    :param app:
    :return:
    """
    logger.info("Initializing routers...")
    counter = 0
    for loader, module_name, _ in pkgutil.walk_packages(routers.__path__):
        _module = loader.find_module(module_name).load_module(module_name)
        app.include_router(_module.router)
        counter += 1
    logger.success(f"{counter} routers successfully initialized!")
