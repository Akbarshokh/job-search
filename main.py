from fastapi import FastAPI
from core.config import settings
from api.general_pages.routes import general_pages_router


def include_router(app):
    app.include_router(general_pages_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    return app


app = start_application()