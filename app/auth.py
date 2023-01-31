from fastapi.security import OAuth2PasswordBearer, HTTPBasic, HTTPBasicCredentials
from fastapi import Depends, status, HTTPException
from jose import JWTError, jwt
from fastapi.logger import logger
from argon2 import PasswordHasher
from sqlalchemy.exc import IntegrityError
from sqlmodel import Field, Session, select
import time, os
from datetime import datetime, timedelta
from typing import Union
from .database import engine, get_session
from .models import api, database #same as from app.models

# roboa security configuration
basic_security = HTTPBasic()

# user security configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/account/auth")
SECRET_KEY = os.environ['SECRET_KEY'] # openssl rand -hex 32
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 365

# code for users authentication

def verify_password(hashed_password: str, plain_password: str) -> bool:
    ph = PasswordHasher()
    try:
        ph.verify(hashed_password, plain_password)
        return True
    except:
        return False

def get_password_hash(password: str) -> str:
    ph = PasswordHasher()
    return ph.hash(password)

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def test_credentials(username: str, password: str):
    #get user with this username
    user = get_user(username)
    # Check user password
    if not verify_password(user.hashed_password, password):
        raise HTTPException(status_code=400, detail="wrong_password")
    # prepare response data
    response_json = {"username": user.username}
    return create_access_token(
        response_json, timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    )


def register_user(user: api.UserCreate) -> None:
    hashed_password = get_password_hash(user.password)
    new_user = database.User(
            hashed_password=hashed_password,
            username=user.username,
            admin = user.admin,
            super_admin = user.super_admin,
            last_update = time.time()
            )
    try:
        with Session(engine) as session:
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="user_already_exists")
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="registration_failed")

def get_user(username: str) -> database.User:
    try:
        with Session(engine) as session:
            statement = select(database.User).where(database.User.username == username)
            results = session.exec(statement)
            user = results.first()
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="user_fetch_failed")

    # Check if account is found
    if user is None:
        raise HTTPException(status_code=400, detail="user_not_found")

    return user


def decode_token(token) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: Union[str, None] = payload.get("username")
        if username is None:
            raise HTTPException(status_code=400, detail="jwt_decode_error")
    except JWTError:
        raise HTTPException(status_code=400, detail="jwt_decode_error")
    return username


async def get_current_user(token: str = Depends(oauth2_scheme)) -> database.User:
    username = decode_token(token)
    user = get_user(username)
    return user


async def get_current_admin_user(current_user: database.User = Depends(get_current_user)):
    if not current_user.admin:
        raise HTTPException(status_code=400, detail="Insufficient account permissions")
    return current_user

async def get_current_super_admin_user(current_user: database.User = Depends(get_current_user)):
    if not current_user.super_admin:
        raise HTTPException(status_code=400, detail="Insufficient account permissions")
    return current_user


# code for roboa authentication

def get_current_roboa(
        credentials: HTTPBasicCredentials = Depends(basic_security),
        session: Session = Depends(get_session)
) -> database.Roboa:
    statement = select(database.Roboa).where(database.Roboa.name == credentials.username)
    results = session.exec(statement)
    roboa = results.first()
    if roboa is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    if not verify_password(roboa.hashed_token, credentials.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    return roboa


