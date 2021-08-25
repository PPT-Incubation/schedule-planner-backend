from typing import Optional
from datetime import date
from pydantic import BaseModel

class MatkulBase(BaseModel):
    nama : str
    sks : int
    hari : str
    jam : str
    ruang : str
    kelas : Optional[str] = None
    dosen : Optional[str] = None

class MatkulCreate(MatkulBase):
    pass

class MatkulUpdate(MatkulBase):
    id : str

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