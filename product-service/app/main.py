from fastapi import FastAPI

from app.database.database import engine
from app.database.database import Base

from app.models.product_model import Product

from app.routes.product_routes import router

Base.metadata.create_all(bind=engine)


from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app)

app.include_router(router)



@app.get("/")
def root():
    return {
        "message": "Product Service is running."
    }