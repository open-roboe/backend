from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.auth import get_current_user, get_current_admin_user
from app.database import engine
from ..models import database, api  # same as "from app.models import database"

router = APIRouter(prefix='/api/course', tags=['course'])


@router.get("/", response_model=List[api.CourseResponse])
async def get_all_courses(*, user=Depends(get_current_user)):
    """
    get all courses
    """
    with Session(engine) as session:
        sessions = session.exec(select(database.Course)).all()
        return sessions


@router.post("/", response_model=api.CourseResponse)
async def add_course(course: api.CourseCreate, admin_user=Depends(get_current_admin_user)):
    """
    TOIMPLEMENT
    Add a course
    """
    # with Session(engine) as session:
    #     session.add(course)
    #     session.commit()
    #     session.refresh(course)
    #     return course


# to implement ==============================


@router.put("/{course}", response_model=api.CourseResponse)
async def update_course(course: str, buoy: api.CourseUpdate, admin_user=Depends(get_current_admin_user)):
    """
    TOIMPLEMENT
    create a new buoy for the specified course
    """
    # generate id
    return buoy


@router.post("/buoy/{id}/assing_roboa")
async def marker_assign_roboa(id: str, roboa: api.RoboaGet, admin_user=Depends(get_current_admin_user)):
    """
    TOIMPLEMENT
    assign specified roboa to specified buoy.
    This operation will not cause the roboa to move
    If you want to move the roboa use the roboa/move endpoint
    """
    return "ok"
