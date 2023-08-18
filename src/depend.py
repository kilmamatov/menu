from typing import Annotated
from fastapi import Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.crud.menu import MenuCrud
from src.crud.submenu import SubMenuCrud
from src.crud.dish import DishMenuCrud
from src.db.database import get_db


###
# MENU
###
async def get_menu_crud(db: Annotated[AsyncSession, Depends(get_db)]):
    return MenuCrud(db)


###
# SubMenu
###
async def get_submenu_crud(db: Annotated[AsyncSession, Depends(get_db)]):
    return SubMenuCrud(db)


###
# Dishes
###
async def get_dish_crud(db: Annotated[AsyncSession, Depends(get_db)]):
    return DishMenuCrud(db)

