from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.logger import logger
from app.database import get_db
from app.models.api import PollData
from sqlmodel import Field, Session, select

from app.database import engine
from ..models import database #"from app.models import database" is better, but not recognized by my linter lol

router = APIRouter(prefix='/api/polling', tags=['polling'])

@router.post("/test")
async def test(user: database.User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

@router.get("/testget")
async def testget():
    with Session(engine) as session:
        users = session.exec(select(database.User)).all()
        return users



@router.get("/", response_model=PollData)
async def poll():
  return {
          "courses": [],
          "boats": [],
          "roboas": []
  }



