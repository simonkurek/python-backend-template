from fastapi import FastAPI
from loguru import logger

from app.config.openapi import OpenAPISettings
from app.initializer import init

open_api_settings = OpenAPISettings()

app = FastAPI(
    title=open_api_settings.name,
    version=open_api_settings.version,
    description=open_api_settings.description,
)
logger.info("Starting application initialization...")
init(app)
logger.success("Successfully initialized!")
