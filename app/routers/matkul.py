from typing import List
from fastapi import APIRouter, status
from fastapi.param_functions import Depends

from .. import crud, schemas, deps

router = APIRouter(
    prefix="/api",
    tags=["mata kuliah"]
)





