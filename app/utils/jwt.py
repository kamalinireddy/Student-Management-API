#This jwt.py file contains the function that creates (generates) a JWT access token after a user successfully logs in.

from datetime import datetime, timedelta

#The jwt imported from python-jose is the library that creates and verifies JWT tokens.
from jose import jwt

from app.config import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)

#function used to create a JWT token. It takes a dictionary as input, which contains the data to be encoded in the token. The function adds an expiration time to the token, encodes it using the specified algorithm and secret key, and returns the encoded JWT token.
def create_access_token(data: dict):

    #we copy the input data to avoid modifying the original dictionary. This is important because we want to add the expiration time to the token without altering the original data.
    to_encode = data.copy()
    
    #the expiration time is calculated.
    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    #The "exp" claim is a standard JWT claim that tells when the token expires.
    to_encode.update({"exp": expire})

    #The jwt.encode function is used to create the JWT token. It takes three arguments: the data to encode (to_encode), the secret key (SECRET_KEY), and the algorithm to use for encoding (ALGORITHM). The function returns the encoded JWT token as a string.
    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt