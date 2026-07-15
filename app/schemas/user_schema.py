from pydantic import BaseModel, EmailStr


# Used while creating a new account
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# Used while logging in
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Sent back to the client
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True