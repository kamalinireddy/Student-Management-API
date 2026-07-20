#dependencies.py extracts the JWT from the request, verifies it, retrieves the corresponding user from the database, and returns the authenticated user to protected routes.

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.database import get_db
from app.repositories.user_repository import get_user_by_email
from app.utils.jwt import SECRET_KEY, ALGORITHM

#Gets the Bearer token from the Authorization header using oauth2_scheme.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

"""get_current_user() authenticates the user by validating the JWT access token, 
extracting the user's email from it, 
looking up that user in the database, and 
returning the user object. 
If any step fails, it returns a 401 Unauthorized error.
"""
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials"
    )

    try:
        #decodes and verifies the jwt token using the SECRET_KEY and ALGORITHM.
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        #extracts the email (subject) from the payload of the decoded JWT.
        email = payload.get("sub")

        if email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    #Looks up the user in the database using that email.
    user = get_user_by_email(db, email)

    if user is None:
        raise credentials_exception

    return user