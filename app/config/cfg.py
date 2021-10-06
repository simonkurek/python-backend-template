import os
from dotenv import load_dotenv

load_dotenv()

IS_TEST = bool(os.getenv("API_TEST"))
