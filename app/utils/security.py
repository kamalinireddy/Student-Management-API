#Passlib is a library used to securely hash and verify passwords.
#CryptContext is an object that knows how to hash and verify passwords.
from passlib.context import CryptContext

#This creates an object called pwd_context which knowns which hashing algorithm to use (bcrypt) and how to verify passwords. 
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

#Function to hash a password.
def hash_password(password: str):
    return pwd_context.hash(password)


#Function to verify a password.
#plain_password → The password the user just entered during login (current password).
#hashed_password → The password stored in the database (the original password that was hashed and stored during signup).
def verify_password(
    plain_password: str,
    hashed_password: str
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )