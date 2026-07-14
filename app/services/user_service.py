from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user_model import User
from app.schemas.user_schema import UserCreate

from app.repositories.user_repository import (
    get_user_by_username,
    get_user_by_email,
    create_user,
)

from app.utils.security import hash_password


# Signup User
def signup_user(db: Session, user: UserCreate):

    existing_user = get_user_by_username(db, user.username)

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    existing_email = get_user_by_email(db, user.email)

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    hashed_password = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )

    return create_user(db, new_user)