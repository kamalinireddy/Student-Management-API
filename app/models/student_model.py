# This is a model class for the Student table in the database. It defines the structure of the table and its columns using SQLAlchemy ORM.
from sqlalchemy import Column, Integer, String, Float

from app.database import Base

class Student(Base):
    #create a table named "students" in the database.
    __tablename__ = "students"
    # id should be int , unique, primary key, and indexed for faster search.
    id = Column(Integer, primary_key=True, index=True)
    #name should be string and cannot be null.
    name = Column(String, nullable=False)
    #cgpa should be int and cannot be null.
    cgpa = Column(Float, nullable=False)
    
#the above information becomes a part of Base.metadata.