from fastapi import FastAPI

from app.database import Base, engine

from app.models.student_model import Student
from app.routers.student_router import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)