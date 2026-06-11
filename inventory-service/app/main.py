from fastapi import FastAPI

from app.database.database import Base
from app.database.database import engine

from app.models.inventory_model import Inventory

from app.routes.inventory_routes import router

from prometheus_fastapi_instrumentator import Instrumentator

Base.metadata.create_all(bind=engine)

app = FastAPI()

Instrumentator().instrument(app).expose(app)
app.include_router(router)


@app.get("/")
def root():
    
    return {
        "message": "Inventory Service is running."
    }