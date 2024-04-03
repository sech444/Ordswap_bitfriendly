from datetime import datetime, timedelta
from typing import Any, Union
from app.core.config import settings
from jose import jwt
from passlib.context import CryptContext
import re
from passlib.hash import bcrypt



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


ALGORITHM = "HS256"


def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
   
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt




from passlib.context import CryptContext

# Create a passlib CryptContext object
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """
    Hashes a password using passlib's CryptContext.

    Parameters:
    - password (str): The plaintext password to be hashed.

    Returns:
    - str: The hashed password.
    """
    # Hash the password using passlib's CryptContext
    hashed_password = pwd_context.hash(password)
    return hashed_password

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a password against a hashed password using passlib's CryptContext.

    Parameters:
    - plain_password (str): The plaintext password to be verified.
    - hashed_password (str): The hashed password stored in the database.

    Returns:
    - bool: True if the passwords match, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)


def check_password_strength(password):
    """
    Checks the strength of a password

    Parameters:
    password (str): The password to check

    Returns:
    str: A string indicating the strength of the password
    """

    # The password is considered weak if it's less than 8 characters long
    if len(password) < 8:
        return 'Password is too short, it should be at least 8 characters long.'

    # The password is considered strong if it contains at least one digit, one lowercase letter,
    # one uppercase letter, and one special character
    if (re.search(r'\d', password) and
        re.search(r'[a-z]', password) and
        re.search(r'[A-Z]', password) and
        re.search(r'[!@#$%^&*()]', password)):
        return 'Strong'

    # If the password is neither weak nor strong, it's considered medium
    return 'Medium'



