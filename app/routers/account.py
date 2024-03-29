from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.logger import logger
from app.auth import get_current_user, get_current_admin_user, get_current_super_admin_user, register_user, \
    test_credentials
from fastapi.security import OAuth2PasswordRequestForm

from fastapi import Depends, status
from ..models import api  # same as: from app.models import api
from ..models.database import User

router = APIRouter(prefix='/api/account', tags=['account'])


@router.get("/", response_model=api.UserResponse)
async def get_logged_user(current_user: User = Depends(get_current_user)):
    """
    Returns account info, requires authentication
    """
    return current_user


@router.get("/admin", response_model=api.UserResponse)
async def get_logged_admin_user(current_user: User = Depends(get_current_admin_user)):
    """
    Returns account info, requires authentication in an admin account.
    Used to test if the current account is admin
    """
    return current_user


@router.get("/super_admin", response_model=api.UserResponse)
async def get_logged_super_admin_user(current_user: User = Depends(get_current_super_admin_user)):
    """
    Returns account info, requires authentication in a super admin account.
    Used to test if the current account is super admin
    """
    return current_user


@router.post("/register")
async def register(form_data: api.UserCreate):
    """
    TODO: require super admin permissions

    Register a new user. Requires authentication in a super admin account
    """
    # Note: This endpoint does not use the superadmin oject, but by importing it
    #       we automatically make sure that this endpoint only works for
    #       superadmin users
    register_user(form_data)
    return JSONResponse(content="ok", status_code=status.HTTP_201_CREATED)


"""
Oauth authentication endpoint
"""


@router.post("/auth", response_model=api.AuthToken)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    jwt = test_credentials(form_data.username, form_data.password)
    return {"access_token": jwt, "token_type": "bearer"}
