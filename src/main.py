from fastapi import FastAPI
from src.routes.menu import router as menu_router
from src.routes.submenu import router as submenu_router
from src.routes.dish import router as dish_router

app = FastAPI(docs_url="/")

app.include_router(
    menu_router,
    prefix="/api/v1/menus",
    tags=["menus"],
)

app.include_router(
    submenu_router,
    prefix="/api/v1/menus",
    tags=["submenus"],
)

app.include_router(
    dish_router,
    prefix="/api/v1/menus/{menu_id}/submenus",
    tags=["dishes"],
)
