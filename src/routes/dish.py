from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from src.crud.dish import DishMenuCrud
from src.depend import get_dish_crud
from src.schemas.dish import ResponseDishMenu, DishMenuBase


router = APIRouter()


@router.get("/{submenu_id}/dishes", response_model=List[ResponseDishMenu], status_code=status.HTTP_200_OK)
async def get_all_dishes(submenu_id: UUID, crud: DishMenuCrud = Depends(get_dish_crud)):
    return await crud.get_all_dishes(submenu_id=submenu_id)


@router.post("/{submenu_id}/dishes", response_model=ResponseDishMenu, status_code=status.HTTP_201_CREATED)
async def create_dish(submenu_id: UUID, new_dish: DishMenuBase, crud: DishMenuCrud = Depends(get_dish_crud)):
    return await crud.create_dish(submenu_id=submenu_id, new_dish=new_dish)


@router.get("/{submenu_id}/dishes/{dish_id}", response_model=ResponseDishMenu, status_code=status.HTTP_200_OK)
async def get_dish(submenu_id: UUID, dish_id: UUID, crud: DishMenuCrud = Depends(get_dish_crud)):
    dish = await crud.get_dish(submenu_id=submenu_id, dish_id=dish_id)
    if dish is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='dish not found',
        )
    return dish


@router.patch("/{submenu_id}/dishes/{dish_id}", response_model=ResponseDishMenu, status_code=status.HTTP_200_OK)
async def update_dish(
        submenu_id: UUID,
        dish_id: UUID,
        new_dish: DishMenuBase,
        crud: DishMenuCrud = Depends(get_dish_crud)
):
    return await crud.update_dish(submenu_id=submenu_id, dish_id=dish_id, new_dish=new_dish)


@router.delete("/{submenu_id}/dishes/{dish_id}", status_code=status.HTTP_200_OK)
async def delete_dish(
        submenu_id: UUID,
        dish_id: UUID,
        crud: DishMenuCrud = Depends(get_dish_crud)
):
    return await crud.delete_dish(submenu_id=submenu_id, dish_id=dish_id)



