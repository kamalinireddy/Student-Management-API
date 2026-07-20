# This is a model class for the User table in the database. It defines the structure of the table and its columns using SQLAlchemy ORM.
from sqlalchemy import Column, Integer, String

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
#the above information becomes a part of Base.metadata.