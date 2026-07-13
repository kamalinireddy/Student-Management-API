from app.repositories.student_repository import (
    get_all_students,
    find_student,
    add_student,
    delete_student,
    students,
)

def get_students():
    return get_all_students()


def get_student(id: int):
    return find_student(id)


def create_student(student):

    new_student = {
        "id": len(students) + 1,
        "name": student.name,
        "cgpa": student.cgpa
    }

    add_student(new_student)

    return new_student


def update_student(id: int, student):

    existing_student = find_student(id)

    existing_student["name"] = student.name
    existing_student["cgpa"] = student.cgpa

    return existing_student


def patch_student(id: int, student):

    existing_student = find_student(id)

    if student.name is not None:
        existing_student["name"] = student.name

    if student.cgpa is not None:
        existing_student["cgpa"] = student.cgpa

    return existing_student


def remove_student(id: int):

    student = find_student(id)

    delete_student(student)

    return {
        "message": "Student deleted successfully"
    }


def search_students(cgpa: float):

    result = []

    for student in students:
        if student["cgpa"] == cgpa:
            result.append(student)

    return result