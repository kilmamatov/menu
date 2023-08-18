from typing import List, Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from src.crud.submenu import SubMenuCrud
from src.depend import get_submenu_crud
from src.schemas.submenu import ResponseSubMenu, SubMenuBase

router = APIRouter()


@router.get("/{menu_id}/submenus", response_model=List[ResponseSubMenu], status_code=status.HTTP_200_OK)
async def get_all_submenu(menu_id: UUID, crud: SubMenuCrud = Depends(get_submenu_crud)):
    return await crud.get_all_submenu(menu_id=menu_id)


@router.post("/{menu_id}/submenus", response_model=ResponseSubMenu, status_code=status.HTTP_201_CREATED)
async def create_submenu(menu_id: UUID, new_submenu: SubMenuBase, crud: SubMenuCrud = Depends(get_submenu_crud)):
    return await crud.create_submenu(menu_id=menu_id, new_submenu=new_submenu)


@router.get("/{menu_id}/submenus/{submenu_id}", response_model=ResponseSubMenu, status_code=status.HTTP_200_OK)
async def get_submenu(menu_id: UUID, submenu_id: UUID, crud: SubMenuCrud = Depends(get_submenu_crud)):
    submenu = await crud.get_submenu(menu_id=menu_id, submenu_id=submenu_id)
    if submenu is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='submenu not found',
        )
    return submenu


@router.patch("/{menu_id}/submenus/{submenu_id}", response_model=ResponseSubMenu, status_code=status.HTTP_200_OK)
async def update_submenu(
        menu_id: UUID,
        submenu_id: UUID,
        new_submenu: SubMenuBase,
        crud: SubMenuCrud = Depends(get_submenu_crud)
):
    return await crud.update_submenu(menu_id=menu_id, submenu_id=submenu_id, new_submenu=new_submenu)


@router.delete("/{menu_id}/submenus/{submenu_id}", status_code=status.HTTP_200_OK)
async def delete_submenu(menu_id: UUID, submenu_id: UUID, crud: SubMenuCrud = Depends(get_submenu_crud)):
    return await crud.delete_submenu(menu_id=menu_id, submenu_id=submenu_id)
