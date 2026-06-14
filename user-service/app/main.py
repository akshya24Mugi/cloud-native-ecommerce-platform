from fastapi import FastAPI
from app.routes.user_routes import router
from app.database.database import Base, engine
from app.models import user_model

from prometheus_fastapi_instrumentator import Instrumentator


Base.metadata.create_all(bind=engine)

app = FastAPI()


Instrumentator().instrument(app).expose(app)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "User service V2"}