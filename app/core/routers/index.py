from fastapi.routing import APIRouter
from starlette.responses import HTMLResponse

router = APIRouter(
    tags=["Index"],
)


@router.get("/")
async def index():
    return {
        "welcome": "Hello in Python Backend Template",
        "info": [
            "If you want to test api or see api documentation go to '/docs'",
            "If you want to see project documenation, is in main project folder in README.md file"
        ]
    }
