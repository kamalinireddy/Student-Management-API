from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.user_schema import (
    UserCreate,
    UserResponse,
)

from app.services.user_service import signup_user

router = APIRouter()


# Signup
@router.post("/signup", response_model=UserResponse, status_code=201)
def signup(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return signup_user(db, user)