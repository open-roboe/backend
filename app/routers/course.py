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
async def add_course(course: api.CourseCreate, admin_user = Depends(get_current_admin_user)):
    """
    TOIMPLEMENT
    Add a course
    """
    with Session(engine) as session:
        session.add(course)
        session.commit()
        session.refresh(course)
        return course

# to implement ==============================


@router.post("/{course}/buoy", response_model=database.BuoyBase)
async def create_buoy(buoy: api.BuoyCreate, admin_user = Depends(get_current_admin_user)):
    """
    TOIMPLEMENT
    create a new buoy for the specified course
    """
    #generate id
    return buoy

@router.post("/{course}/jury", response_model=database.BuoyBase)
async def create_jury(buoy: api.BuoyCreate, admin_user = Depends(get_current_admin_user)):
    """
    TOIMPLEMENT
    create the course jury buoy
    """
    #generate id,
    #update course.jury.id
    return buoy

@router.put("/buoy/{id}")
async def update_buoy(id: str, buoy: api.BuoyUpdate, admin_user = Depends(get_current_admin_user)):
    """
    TOIMPLEMENT
    update a buoy
    """
    return "ok"


@router.put("/jury/{id}")
async def update_jury(id: str, buoy: api.BuoyUpdate, admin_user = Depends(get_current_admin_user)):
    """
    TOIMPLEMENT
    update a buoy
    """
    return "ok"


@router.delete("/buoy/{id}")
async def delete_buoy(id: str, admin_user = Depends(get_current_admin_user)):
    """
    TOIMPLEMENT
    delete a buoy
    """
    return "ok"


@router.post("/buoy/{id}/assing_roboa")
async def marker_assign_roboa(id: str, roboa: api.RoboaGet, admin_user = Depends(get_current_admin_user)):
    """
    TOIMPLEMENT
    assign specified roboa to specified buoy.
    This operation will not cause the roboa to move
    If you want to move the roboa use the roboa/move endpoint
    """
    return "ok"
