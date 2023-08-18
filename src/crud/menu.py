from typing import Annotated
from uuid import UUID

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, func, insert, select, update
from src.db.database import get_db
from src.db.models import Menu
from src.schemas.menu import MenuBase


class MenuCrud:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_db)]):
        self.session = session

    async def get_all_menu(self):
        return (
            await self.session.execute(select(Menu))
        ).scalars().fetchall()

    async def create_menu(self, new_menu: MenuBase) -> Menu:
        stmt = insert(Menu).values(**new_menu.model_dump()).returning(Menu)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def get_menu(self, menu_id: UUID) -> Menu:
        stmt = select(Menu).where(Menu.id == menu_id)
        result = await self.session.execute(stmt)
        return result.scalar()

    async def update_menu(self, menu_id: UUID, updated_menu: MenuBase) -> Menu:
        stmt = update(Menu).where(Menu.id == menu_id).values(**updated_menu.model_dump()).returning(Menu)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def delete_menu(self, menu_id: UUID):
        query = delete(Menu).where(Menu.id == menu_id)
        await self.session.execute(query)
        await self.session.commit()






