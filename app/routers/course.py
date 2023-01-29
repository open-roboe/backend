import time
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import select

from app.auth import get_current_user, get_current_admin_user
from app.database import get_session
from ..models import database, api  # same as "from app.models import database"

router = APIRouter(prefix='/api/course', tags=['course'])


@router.get("/", response_model=List[api.CourseResponse])
async def get_all_courses(*, user=Depends(get_current_user), session=Depends(get_session)):
    """
    get all courses
    """
    return session.exec(select(database.Course)).all()


@router.post("/", response_model=api.CourseResponse)
async def add_course(course_create: api.CourseCreate,
                     admin_user=Depends(get_current_admin_user),
                     session=Depends(get_session)
                     ):
    """
    Add a course, with its jury and buoys.

    Courses are the same thing as Regattas. It's just a synonym
    """
    # create the course
    course = database.Course(
        creation_date=time.time(),
        name=course_create.name,
        type=course_create.type,
    )
    # create the jury
    jury_create_dict = course_create.jury.dict(exclude_unset=True)
    jury = database.BuoyJury(
        **jury_create_dict
    )
    # update the course with the jury id
    course.jury_id = jury.id
    # create all the buoys
    for buoy_create in course_create.buoys:
        buoy = database.Buoy(
            course_id=course.name,
            **buoy_create.dict()
        )
        session.add(buoy)
    # attempt database commit
    try:
        session.add(jury)
        session.add(course)
        session.commit()
        session.refresh(course)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="course_or_jury_already_exist")
    return course


@router.put("/", response_model=api.CourseResponse)
async def update_course(
        course_update: api.CourseUpdate,
        admin_user=Depends(get_current_admin_user),
        session = Depends(get_session)
):
    """
    update a course

    note: course.name, jury.id and buoy.id are identifiers and cannot be changed
    """
    #get the original course
    course: database.Course = session.get(database.Course, course_update.name)
    if not course:
        raise HTTPException(status_code=404, detail="course_not_found")
    jury = course.jury
    buoys = course.buoys
    #modify the course
    if course_update.type:
        course.type = course_update.type
    #modify the jury
    saved_jury_id = jury.id
    jury_update_dict = course_update.jury.dict(exclude_unset=True)
    for key, value in jury_update_dict.items():
        setattr(jury, key, value)
    jury.id = saved_jury_id
    #modify the buoys
    for buoy_update in course_update.buoys:
        #find an existing buoy to modify
        for buoy in buoys:
            if buoy.id == buoy_update.id:
                buoy_update_dict = buoy_update.dict(exclude_unset=True)
                for key, value in buoy_update_dict.items():
                    setattr(buoy, key, value)
                session.add(buoy)

    session.add(jury)
    session.add(course)
    session.commit()
    session.refresh(course)
    return course


@router.post("/{course_name}/buoy/{buoy_id}/assign_roboa")
async def marker_assign_roboa(buoy_id: str, roboa: api.RoboaGet, admin_user=Depends(get_current_admin_user)):
    """
    TOIMPLEMENT
    assign a roboa to a buoy. This also works for buoys of type jury.
    Just pass the id of the jury in the buoy_id parameter

    This operation will not cause the roboa to move!
    If you want to move the roboa use the roboa/move endpoint
    """
    return "ok"
