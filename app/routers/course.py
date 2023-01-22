from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from fastapi.responses import JSONResponse
from fastapi.logger import logger
from app.database import engine
from typing import List
from app.auth import get_current_user, get_current_admin_user, get_current_super_admin_user
from ..models import database, api #same as "from app.models import database"

router = APIRouter(prefix='/api/course', tags=['course'])


@router.get("/", response_model=List[database.Course])
async def get_all_courses(*, user = Depends(get_current_user)):
    """
    get all courses
    """
    with Session(engine) as session:
        sessions = session.exec(select(database.Course)).all()
        return sessions


@router.post("/", response_model=database.Course)
async def add_course(course: database.Course, admin_user = Depends(get_current_admin_user)):
    """
    Add a course
    """
    with Session(engine) as session:
        session.add(course)
        session.commit()
        session.refresh(course)
        return course

# to implement ==============================


@router.post("/marker")
async def create_marker(*, admin_user = Depends(get_current_admin_user)):
    """
    create a new marker for the specified course
    ideas: uuid, lat, lon, color
    """
    pass

@router.put("/marker")
async def update_marker(*, admin_user = Depends(get_current_admin_user)):
    """
    update a marker
    """
    pass

@router.delete("/marker")
async def delete_marker(*, admin_user = Depends(get_current_admin_user)):
    """
    delete a marker
    """
    pass


@router.post("/marker/assign_roboa")
async def marker_assign_roboa(*, admin_user = Depends(get_current_admin_user)):
    """
    assign specified roboa to specified marker
    """
    pass

@router.post("/join_course")
async def join_course(*, admin_user = Depends(get_current_admin_user)):
    """
    assign current logged user to specified course
    """
    pass
