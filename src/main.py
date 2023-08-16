from fastapi import FastAPI
from src.routes.menu import router as menu_router

app = FastAPI(docs_url="/")

app.include_router(
    menu_router,
    prefix="/api/v1/menus",
    tags=["menus"],
)
