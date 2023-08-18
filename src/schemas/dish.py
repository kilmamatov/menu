from pydantic import BaseModel, ConfigDict
from uuid import UUID


class ConfigModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class DishMenuBase(ConfigModel):
    title: str
    description: str
    price: float


class ResponseDishMenu(DishMenuBase):
    submenu_id: UUID
    id: UUID
