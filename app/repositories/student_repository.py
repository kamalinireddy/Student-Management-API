from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.student_model import Student


# Get all students
def get_all_students(db: Session):
    return db.query(Student).all()


# Get one student
def find_student(db: Session, id: int):
    student = db.query(Student).filter(Student.id == id).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# Create student
def add_student(db: Session, student: Student):
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


# Delete student
def delete_student(db: Session, student: Student):
    db.delete(student)
    db.commit()