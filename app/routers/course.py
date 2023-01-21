from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from fastapi.responses import JSONResponse
from fastapi.logger import logger
from app.database import engine
from typing import List
from app.auth import get_current_user, get_current_admin_user, get_current_super_admin_user
from ..models import database #same as "from app.models import database"

router = APIRouter(prefix='/api/course', tags=['course'])


@router.get("/", response_model=List[database.Course])
async def get_all_courses(*, user = Depends(get_current_user)):
    with Session(engine) as session:
        sessions = session.exec(select(database.Course)).all()
        return sessions


@router.post("/", response_model=database.Course)
async def add_course(course: database.Course, admin_user = Depends(get_current_admin_user)):
    with Session(engine) as session:
        session.add(course)
        session.commit()
        session.refresh(course)
        return course

