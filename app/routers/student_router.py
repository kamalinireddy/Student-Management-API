from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.user_model import User
from app.dependencies import get_current_user
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

router = APIRouter(
    tags=["Students"]
)


@router.get(
    "/",
    summary="Home",
    description="Returns a welcome message."
)
def home():
    return {"message": "Welcome to Student Management API"}


@router.get(
    "/students",
    response_model=list[StudentResponse],
    summary="Get all students",
    description="Returns every student stored in the database."
)
def get_all_students_route(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_students(db)


@router.get(
    "/students/{id}",
    response_model=StudentResponse,
    summary="Get one student",
    description="Returns a student by ID."
)
def get_student_route(
    id: int,
    db: Session = Depends(get_db)
):
    return get_student(db, id)


@router.post(
    "/students",
    response_model=StudentResponse,
    status_code=201,
    summary="Create student",
    description="Creates a new student."
)
def create_student_route(
    student: Student,
    db: Session = Depends(get_db)
):
    return create_student(db, student)


@router.put(
    "/students/{id}",
    response_model=StudentResponse,
    summary="Replace student",
    description="Completely replaces an existing student."
)
def update_student_route(
    id: int,
    student: Student,
    db: Session = Depends(get_db)
):
    return update_student(db, id, student)


@router.patch(
    "/students/{id}",
    response_model=StudentResponse,
    summary="Update student",
    description="Updates selected student fields."
)
def patch_student_route(
    id: int,
    student: StudentUpdate,
    db: Session = Depends(get_db)
):
    return patch_student(db, id, student)


@router.delete(
    "/students/{id}",
    summary="Delete student",
    description="Deletes a student."
)
def remove_student_route(
    id: int,
    db: Session = Depends(get_db)
):
    return remove_student(db, id)


@router.get(
    "/students/search",
    response_model=list[StudentResponse],
    summary="Search students",
    description="Search students by CGPA."
)
def search_students_route(
    cgpa: float,
    db: Session = Depends(get_db)
):
    return search_students(db, cgpa)