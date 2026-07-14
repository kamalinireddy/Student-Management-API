from fastapi import FastAPI

from app.database import Base, engine

from app.models.student_model import Student
from app.models.user_model import User

from app.routers.student_router import router as student_router
from app.routers.user_router import router as user_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(student_router)
app.include_router(user_router)