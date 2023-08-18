from pydantic import BaseModel, ConfigDict, RootModel
from uuid import UUID


class ConfigModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class MenuBase(ConfigModel):
    title: str
    description: str


class ResponseMenu(MenuBase):
    id: UUID


# ResponseAllMenu = RootModel[list[ResponseMenu]]






