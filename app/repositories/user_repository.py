#The functions in user_repository.py are responsible for interacting with the database (fetching, creating, updating, deleting users) and returning the results to the router or service layer.
from sqlalchemy.orm import Session

from app.models.user_model import User

#db is a session which was used basically to isolate api requests.
#A Session is a temporary workspace for one API request—it executes database operations, tracks changes, manages transactions, and keeps requests isolated from one another.

#Search the users table by email and return the matching User object (or None).
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user