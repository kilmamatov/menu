from typing import Annotated
from uuid import UUID
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, func, insert, select, update
from src.db.database import get_db
from src.db.models import Dishes
from src.schemas.dish import DishMenuBase


class DishMenuCrud:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_db)]):
        self.session = session

    async def get_all_dishes(self, submenu_id: UUID):
        query = select(Dishes).where(Dishes.submenu_id == submenu_id)
        result = await self.session.execute(query)
        return result.scalars().fetchall()

    async def create_dish(self, submenu_id: UUID, new_dish: DishMenuBase) -> Dishes:
        stmt = insert(Dishes).values(submenu_id=submenu_id, **new_dish.model_dump()).returning(Dishes)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def get_dish(self, submenu_id: UUID, dish_id: UUID) -> Dishes:
        stmt = select(Dishes).where(Dishes.submenu_id == submenu_id, Dishes.id == dish_id)
        result = await self.session.execute(stmt)
        return result.scalar()

    async def update_dish(self, submenu_id: UUID, dish_id: UUID, new_dish: DishMenuBase) -> Dishes:
        stmt = update(Dishes).where(
            Dishes.submenu_id == submenu_id,
            Dishes.id == dish_id).values(**new_dish.model_dump()).returning(Dishes)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def delete_dish(self, submenu_id: UUID, dish_id: UUID):
        query = delete(Dishes).where(Dishes.submenu_id == submenu_id, Dishes.id == dish_id)
        await self.session.execute(query)
        await self.session.commit()

