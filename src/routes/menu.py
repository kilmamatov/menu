from typing import List, Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from src.crud.menu import MenuCrud
from src.depend import get_menu_crud
from src.schemas.menu import MenuBase, ResponseMenu


router = APIRouter()


@router.get("/", response_model=List[ResponseMenu], status_code=status.HTTP_200_OK)
async def get_all_menu(crud: MenuCrud = Depends(get_menu_crud)):
    return await crud.get_all_menu()


@router.post("/", response_model=ResponseMenu, status_code=status.HTTP_201_CREATED)
async def create_menu_menu(new_menu: MenuBase, crud: MenuCrud = Depends(get_menu_crud)):
    return await crud.create_menu(new_menu)


@router.get("/{menu_id}", response_model=ResponseMenu)
async def get_menu(menu_id: UUID, crud: MenuCrud = Depends(get_menu_crud)):
    menu = await crud.get_menu(menu_id=menu_id)
    if menu is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='menu not found',
        )
    return menu


@router.patch("/{menu_id}", response_model=ResponseMenu)
async def update_menu(menu_id: UUID, updated_menu: MenuBase, crud: MenuCrud = Depends(get_menu_crud)):
    return await crud.update_menu(menu_id=menu_id, updated_menu=updated_menu)


@router.delete("/{menu_id}", status_code=status.HTTP_200_OK)
async def delete_menu(menu_id: UUID, crud: MenuCrud = Depends(get_menu_crud)):
    return await crud.delete_menu(menu_id=menu_id)


