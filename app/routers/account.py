from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.logger import logger
from app.database import get_db
from app.auth import get_current_user, get_current_admin_user
from fastapi.security import OAuth2PasswordRequestForm

from fastapi import Depends, status
from app.models.api import User

router = APIRouter(prefix='/api/account', tags=['account'])


@router.get("/")
async def get_logged_user(current_user: User = Depends(get_current_user)):
    return current_user


@router.post("/")
async def create_user(current_user: User = Depends(get_current_admin_user)):
    #TODO: receive new user data, create user in db
    return current_user


"""
Oauth authentication endpoint
"""
@router.post("/auth")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db = Depends(get_db)):
    user_dict = db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    hashed_password = form_data.password
    user = User(**user_dict)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


