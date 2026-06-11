from fastapi import FastAPI

from app.database.database import Base
from app.database.database import engine

from app.models.order_model import Order

from app.routes.order_routes import router

Base.metadata.create_all(bind=engine)

from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()

Instrumentator().instrument(app).expose(app)

app.include_router(router)


@app.get("/")

def root():
    return {
        "message": "Order service is running"
    }