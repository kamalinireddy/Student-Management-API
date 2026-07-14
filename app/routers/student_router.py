from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.student_schema import (
    Student,
    StudentUpdate,
    StudentResponse,
)

from app.services.student_service import (
    get_students,
    get_student,
    create_student,
    update_student,
    patch_student,
    remove_student,
    search_students,
)

router = APIRouter()


# Home API
@router.get("/")
def home():
    return {"message": "Welcome to Student Management API"}


# Get all students
@router.get("/students", response_model=list[StudentResponse])
def get_all_students_route(db: Session = Depends(get_db)):
    return get_students(db)


# Get one student
@router.get("/students/{id}", response_model=StudentResponse)
def get_student_route(id: int, db: Session = Depends(get_db)):
    return get_student(db, id)


# Create student
@router.post("/students", status_code=201, response_model=StudentResponse)
def create_student_route(student: Student, db: Session = Depends(get_db)):
    return create_student(db, student)


# Replace entire student
@router.put("/students/{id}", response_model=StudentResponse)
def update_student_route(
    id: int,
    student: Student,
    db: Session = Depends(get_db)
):
    return update_student(db, id, student)


# Update selected fields
@router.patch("/students/{id}", response_model=StudentResponse)
def patch_student_route(
    id: int,
    student: StudentUpdate,
    db: Session = Depends(get_db)
):
    return patch_student(db, id, student)


# Delete student
@router.delete("/students/{id}")
def remove_student_route(
    id: int,
    db: Session = Depends(get_db)
):
    return remove_student(db, id)


# Search students
@router.get("/students/search", response_model=list[StudentResponse])
def search_students_route(
    cgpa: float,
    db: Session = Depends(get_db)
):
    return search_students(db, cgpa)