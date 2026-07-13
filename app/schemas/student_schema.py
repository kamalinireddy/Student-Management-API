from pydantic import BaseModel, Field
from typing import Optional

# Schema for creating a student
class Student(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    cgpa: float = Field(ge=0, le=10)

# Schema for updating a student
class StudentUpdate(BaseModel):
    name: Optional[str] = None
    cgpa: Optional[float] = None

# Response Schema
class StudentResponse(BaseModel):
    id: int
    name: str
    cgpa: float