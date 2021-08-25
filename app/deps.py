from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError

from .settings import settings
from . import security, schemas, crud

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/get-token")


def get_current_user(token : str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=security.ALGORITHM)
        token_data = schemas.TokenPayload(**payload)

    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials"
        )
    
    user = crud.get_user_by_username(token_data.sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return schemas.User(**user.dict())