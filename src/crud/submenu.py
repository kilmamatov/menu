from typing import Annotated
from uuid import UUID

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, func, insert, select, update
from src.db.database import get_db
from src.db.models import SubMenu
from src.schemas.submenu import SubMenuBase


class SubMenuCrud:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_db)]):
        self.session = session

    async def get_all_submenu(self, menu_id: UUID):
        return (
            await self.session.execute(select(SubMenu).where(SubMenu.menu_id == menu_id))
        ).scalars().fetchall()

    async def create_submenu(self, menu_id: UUID, new_submenu: SubMenuBase) -> SubMenu:
        stmt = insert(SubMenu).values(menu_id=menu_id, **new_submenu.model_dump()).returning(SubMenu)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def get_submenu(self, menu_id: UUID, submenu_id: UUID):
        stmt = select(SubMenu).where(SubMenu.menu_id == menu_id, SubMenu.id == submenu_id)
        result = await self.session.execute(stmt)
        return result.scalar()

    async def update_submenu(self, menu_id: UUID, submenu_id: UUID, new_submenu: SubMenuBase) -> SubMenu:
        stmt = update(SubMenu).where(
            SubMenu.menu_id == menu_id,
            SubMenu.id == submenu_id).values(**new_submenu.model_dump()).returning(SubMenu)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def delete_submenu(self, menu_id: UUID, submenu_id: UUID):
        query = delete(SubMenu).where(SubMenu.menu_id == menu_id, SubMenu.id == submenu_id)
        await self.session.execute(query)
        await self.session.commit()

