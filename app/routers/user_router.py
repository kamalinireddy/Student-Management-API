from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.user_schema import (
    UserCreate,
    UserResponse,
)

from app.services.user_service import (
    signup_user,
    login_user,
)

router = APIRouter(
    tags=["Authentication"]
)


# Signup
@router.post("/signup", response_model=UserResponse, status_code=201)
def signup(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return signup_user(db, user)


# Login
@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return login_user(
        db,
        form_data.username,
        form_data.password
    )