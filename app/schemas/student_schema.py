#a blueprint is describing a what valid data should look like for a student.

from typing import Optional

#Pydantic is a library that FastAPI uses to
#1. Validate incoming data
#2. Convert JSON into Python objects
#3. Convert Python objects back into JSON
from pydantic import BaseModel, Field


class Student(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    #ge = means greater thn or equal to
    #le = means less thn or equal to 
    cgpa: float = Field(ge=0, le=10)

#for patch where we want to update only some fields, we can make the fields optional. If a field is not provided, it will be set to None.
class StudentUpdate(BaseModel):
    name: Optional[str] = None
    cgpa: Optional[float] = None


class StudentResponse(BaseModel):
    id: int
    name: str
    cgpa: float

    class Config:
        from_attributes = True