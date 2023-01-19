from fastapi.security import OAuth2PasswordBearer
from app.database import get_db
from app.models.api import User
from fastapi import Depends, status, HTTPException


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/account/auth")

def get_user(username: str):
    db = get_db()
    if username in db:
        user_dict = db[username]
        return User(**user_dict)


def fake_decode_token(token):
    # This doesn't provide any security at all
    # Replace with token lookup in db, or jwt
    user = get_user(token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_admin_user(current_user: User = Depends(get_current_user)):
    if not current_user.admin:
        raise HTTPException(status_code=400, detail="Insufficient account permissions")
    return current_user
