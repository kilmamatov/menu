from pydantic import BaseModel, ConfigDict
from uuid import UUID


class ConfigModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class SubMenuBase(ConfigModel):
    title: str
    description: str


class ResponseSubMenu(SubMenuBase):
    menu_id: UUID
    id: UUID



