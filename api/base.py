from fastapi import APIRouter

from api.version1 import routes
from api.version1 import route_user


api_router = APIRouter()
api_router.include_router(
    routes.general_pages_router,
    prefix="",
    tags=["general_pages"]
)
api_router.include_router(
    route_user.router,
    prefix="/users",
    tags=["users"]
)