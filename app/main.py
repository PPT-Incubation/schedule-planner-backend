from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from . import schemas, crud, security
from .routers import matkul

description = """
Schedule Planner API

"""

app = FastAPI(
    title = "SchedulePlannerAPI",
    description = description
)

app.include_router(matkul.router)

@app.post("/login/get-token", response_model=schemas.Token, include_in_schema=True)
async def login_get_token(form_data : OAuth2PasswordRequestForm = Depends()):
    user = crud.authenticate_user(schemas.UserIn(username=form_data.username, password=form_data.password))
    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Incorrect username or password!",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token = security.create_access_token(user.username)
    return {
        "access_token" : access_token,
        "token_type" : "Bearer"
    }


@app.get("/")
async def home():
    return "Hello World, Welcome to SchedulePlannerAPI, please check /docs for documentation!"