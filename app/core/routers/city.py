from fastapi.routing import APIRouter
from app.core.models.db.City_Entity import City_Entity
from app.core.models.classes.City_Model import City_WriteModel, City_ReadModel

router = APIRouter(
    prefix="/city",
    tags=["City"],
)


@router.get("/all")
async def get_all():
    return await City_ReadModel.from_queryset(City_Entity.all())


@router.get("/{city_id}")
async def get_by_id(city_id):
    return await City_ReadModel.from_queryset_single(City_Entity.get(id=city_id))


@router.post("/")
async def create(city_data: City_WriteModel):
    city_obj = await City_Entity.create(**city_data.dict(exclude_unset=True))
    return await City_ReadModel.from_tortoise_orm(city_obj)


@router.delete("/{city_id}")
async def delete(city_id):
    await City_Entity.filter(id=city_id).delete()
    return {}
