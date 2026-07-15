from typing import Optional

from pydantic import BaseModel, Field


class Student(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    cgpa: float = Field(ge=0, le=10)


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    cgpa: Optional[float] = None


class StudentResponse(BaseModel):
    id: int
    name: str
    cgpa: float

    class Config:
        from_attributes = True