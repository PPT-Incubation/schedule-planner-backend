from typing import Optional
from datetime import date
from pydantic import BaseModel

class User(BaseModel):
    username : str

class UserIn(User):
    password : str

class UserOutDB(User):
    hashed_pwd : str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenPayload(BaseModel):
    sub : str