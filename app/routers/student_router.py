from fastapi import APIRouter, Header, Response
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
def get_all_students_route():
    return get_students()

# Get one student
@router.get("/students/{id}", response_model=StudentResponse)
def get_student_route(id: int):
    return get_student(id)

# Create student
@router.post("/students", status_code=201, response_model=StudentResponse)
def create_student_route(student: Student):
    return create_student(student)

# Replace entire student
@router.put("/students/{id}", response_model=StudentResponse)
def update_student_route(id: int, student: Student):
    return update_student(id, student)

# Update selected fields
@router.patch("/students/{id}", response_model=StudentResponse)
def patch_student_route(id: int, student: StudentUpdate):
    return patch_student(id, student)

# Delete student
@router.delete("/students/{id}")
def remove_student_route(id: int):
    return remove_student(id)

# Search students
@router.get("/students/search")
def search_students_route(cgpa: float):
    return search_students(cgpa)