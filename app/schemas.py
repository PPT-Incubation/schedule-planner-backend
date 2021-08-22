from typing import Optional
from datetime import date
from pydantic import BaseModel

class MatkulBase(BaseModel):
    nama : str
    kelas : str
    sks : int
    waktu : str
    ruang : str
    dosen : Optional[str] = None

class MatkulIn(MatkulBase):
    pass

class MatkulOut(MatkulBase):
    id : str

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