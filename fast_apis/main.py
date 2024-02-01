from fastapi import FastAPI
from apis_app.dependencies.database import (
    engine,
    Base
)
from apis_app.apis.v1_endpoints import employee

app = FastAPI()

app.include_router(employee.router)
Base.metadata.create_all(bind=engine)
