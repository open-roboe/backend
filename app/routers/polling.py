from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.logger import logger
from app.database import get_db
from app.models.api import PollData

router = APIRouter(prefix='/api/polling', tags=['polling'])



@router.get("/", response_model=PollData)
async def poll():
  return {
          "courses": [],
          "boats": [],
          "roboas": []
  }



