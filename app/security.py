from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt

from .settings import settings

ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"])

def verify_password(plain_password : str, hashed_password : str):
    return pwd_context.verify(plain_password,hashed_password)

def create_access_token(subject : str):
    expire = datetime.utcnow() + timedelta(days=1)
    to_encode = {"exp" : expire, "sub" : str(subject)}
    jwt_encoded = jwt.encode(to_encode, settings.secret_key, algorithm=ALGORITHM)
    return jwt_encoded