from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.logger import logger
from app.database import get_db

router = APIRouter(prefix='/api/account', tags=['account'])



@router.get("/")
async def test():
  return {"test": "working"}

