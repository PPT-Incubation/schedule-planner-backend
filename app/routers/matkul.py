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
def create_id_key(matkul):
    matkul['id'] = str(matkul['_id'])
    return matkul

@router.get("/matkuls", response_model=List[schemas.MatkulOut])
async def get_matkuls():
    """
    Get all mata kuliah

    Require authentication
    """
    # Need to converted as a list to match response_model
    return [create_id_key(i) for i in crud.get_all_matkuls()]

@router.get("/matkul", response_model=schemas.MatkulOut)
async def get_matkul(id : str):
    """
    Get a matkul by id

    Require authentication
    """
    return create_id_key(crud.get_a_matkul(id))

@router.post("/matkul", status_code=status.HTTP_201_CREATED)
async def create_matkul(matkul : schemas.MatkulCreate):
    """
    Create new matkul

    Require authentication
    """
    
    # Convert ObjectId object from mongoDB as string to satisfy FastAPI return specs
    return str(crud.create_a_matkul(matkul))

@router.put("/matkul")
async def update_matkul(matkul : schemas.MatkulUpdate):
    """
    Update existing matkul

    Require authentication
    """

    return str(crud.update_a_matkul(matkul))

@router.delete("/matkul", response_model=schemas.MatkulOut)
async def delete_matkul(id : str):
    """
    Delete matkul by ID

    Require authentication
    """

    return create_id_key(crud.delete_a_matkul(id))

