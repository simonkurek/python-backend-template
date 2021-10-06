import os
from dotenv import load_dotenv

load_dotenv()


class OpenAPISettings:
    name: str
    version: str
    description: str

    def __init__(self):
        self.name = os.getenv("OPENAPI_API_NAME")
        self.version = os.getenv("OPENAPI_API_VERSION")
        self.description = os.getenv("OPENAPI_API_DESCRIPTION")
