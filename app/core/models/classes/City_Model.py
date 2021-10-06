from tortoise.contrib.pydantic import pydantic_model_creator
from app.core.models.db.City_Entity import City_Entity

City_ReadModel = pydantic_model_creator(
    City_Entity,
    name="City_ReadModel"
)

City_WriteModel = pydantic_model_creator(
    City_Entity,
    name="City_WriteModel",
    exclude_readonly=True
)
