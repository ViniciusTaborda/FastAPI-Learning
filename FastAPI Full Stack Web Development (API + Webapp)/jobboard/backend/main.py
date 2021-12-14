from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base
from apis.version1.route_user import router


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    app.include_router(router)
    return app


app = start_application()


@app.get("/")
def hello_world():
    return {"detail": "Hello World!"}
