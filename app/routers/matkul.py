from typing import List
from fastapi import APIRouter, status
from fastapi.param_functions import Depends

from .. import crud, schemas, deps

router = APIRouter(
    prefix="/api",
    tags=["mata kuliah"],
    dependencies=[Depends(deps.get_current_user)]
)

# Function to convert "_id" from MongoDB to "id"
def create_id_key(mk):
    mk['id'] = str(mk['_id'])
    return mk

@router.get("/matkuls", response_model=List[schemas.MatkulOut])
async def get_matkuls():
    """
    Get all mata kuliah

    Require authentication
    """
    # Need to converted as a list to match response_model
    return [create_id_key(i) for i in crud.get_all_matkuls()]



