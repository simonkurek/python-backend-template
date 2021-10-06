from tortoise.models import Model
from tortoise import fields

import requests


class City_Entity(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(50, unique=True)
    timezone = fields.CharField(50)

    def current_time(self) -> str:
        r = requests.get(
            f'http://worldtimeapi.org/api/timezone/{self.timezone}')
        current_time = r.json()['datetime']
        return current_time

    class PydanticMeta:
        computed = ('current_time', )
