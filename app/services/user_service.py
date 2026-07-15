from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.utils.jwt import create_access_token
from app.models.user_model import User
from app.schemas.user_schema import UserCreate

from app.repositories.user_repository import (
    get_user_by_username,
    get_user_by_email,
    create_user,
)

from app.utils.security import (
    hash_password,
    verify_password,
)


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


# Login User
def login_user(db: Session, username: str, password: str):
    
    user = get_user_by_email(db, username)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        {
            "sub": user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }