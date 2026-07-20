from fastapi import FastAPI

#engine = consists the connection information to the database(database URL, username, password, host, port, etc.)
#base = Is a special SQLAlchemy class that keeps track of all the classes that represent database tables.
from app.database import Base, engine

#for python to execute the code in the models folder, we need to import the models, thus base gets to know about the class which are inhertied from it and thus sqlalchemy can create the tables in the database.
from app.models.student_model import Student
from app.models.user_model import User

#each router contains group of endpoints
#student_router = get/ students, post/ students, put/students.
#user_router =  post/ signup, post/login.
from app.routers.student_router import router as student_router
from app.routers.user_router import router as user_router

#title, description, version written for swagger.
app = FastAPI(
    title="Student Management API",
    description="""
A FastAPI backend project demonstrating:

- CRUD Operations
- SQLAlchemy ORM
- PostgreSQL Database
- JWT Authentication
- Password Hashing
- Layered Architecture (Router → Service → Repository)
""",
    version="1.0.0"
)

#Take every model registered in Base and create those tables inside the connected PostgreSQL database if they don't already exist.
Base.metadata.create_all(bind=engine)

# Takes that router object. Registers all its routes with the FastAPI application.
app.include_router(student_router)
app.include_router(user_router)