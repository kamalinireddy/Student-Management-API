from sqlalchemy.orm import Session

from app.models.student_model import Student as StudentDB
from app.schemas.student_schema import Student, StudentUpdate

from app.repositories.student_repository import (
    get_all_students,
    find_student,
    add_student,
    delete_student,
)


# Get all students
def get_students(db: Session):
    return get_all_students(db)


# Get one student
def get_student(db: Session, id: int):
    return find_student(db, id)


# Create student
def create_student(db: Session, student: Student):

    new_student = StudentDB(
        name=student.name,
        cgpa=student.cgpa
    )

    return add_student(db, new_student)


# Replace entire student
def update_student(db: Session, id: int, student: Student):

    existing_student = find_student(db, id)

    existing_student.name = student.name
    existing_student.cgpa = student.cgpa

    db.commit()
    db.refresh(existing_student)

    return existing_student


# Update selected fields
def patch_student(db: Session, id: int, student: StudentUpdate):

    existing_student = find_student(db, id)

    if student.name is not None:
        existing_student.name = student.name

    if student.cgpa is not None:
        existing_student.cgpa = student.cgpa

    db.commit()
    db.refresh(existing_student)

    return existing_student


# Delete student
def remove_student(db: Session, id: int):

    student = find_student(db, id)

    delete_student(db, student)

    return {
        "message": "Student deleted successfully"
    }


# Search students
def search_students(db: Session, cgpa: float):

    return db.query(StudentDB).filter(
        StudentDB.cgpa == cgpa
    ).all()