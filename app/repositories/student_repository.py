from fastapi import HTTPException

# Temporary Database
students = [
    {"id": 1, "name": "Rahul", "cgpa": 8.2},
    {"id": 2, "name": "Sara", "cgpa": 9.1},
]

def find_student(id: int):
    for student in students:
        if student["id"] == id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
def get_all_students():
    return students


def add_student(student):
    students.append(student)
    return student


def delete_student(student):
    students.remove(student)