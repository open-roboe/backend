import time
from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.auth import get_current_user, get_current_admin_user
from app.database import engine, get_session
from ..models import database, api  # same as "from app.models import database"

router = APIRouter(prefix='/api/course', tags=['course'])


@router.get("/", response_model=List[api.CourseResponse])
async def get_all_courses(*, user=Depends(get_current_user), session=Depends(get_session)):
    """
    get all courses
    """
    return session.exec(select(database.Course)).all()


@router.post("/", response_model=api.CourseResponse)
async def add_course(course_create: api.CourseCreate, admin_user=Depends(get_current_admin_user)):
    """
    TOIMPLEMENT
    Add a course
    """

    # insert the course
    course = database.Course(
        creation_date = time.time(),
        name=course_create.name,
        type=course_create.type,
    )
    with Session(engine) as session:
        session.add(course)
        session.commit()
        session.refresh(course)

    #insert the jury
    jury = database.BuoyJury()
    jury_create_dict = course_create.jury.dict(exclude_unset=True)
    for key, value in jury_create_dict.items():
        setattr(jury, key, value)
    with Session(engine) as session:
        session.add(jury)
        session.commit()
        session.refresh(jury)

    # update the course with the jury id
    course.jury_id = jury.id
    with Session(engine) as session:
        session.add(course)
        session.commit()
        session.refresh(course)


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
