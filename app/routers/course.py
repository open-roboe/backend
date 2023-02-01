import time
import uuid
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import select, Session

from app.auth import get_current_user, get_current_admin_user
from app.database import get_session
from ..models import database, api  # same as "from app.models import database"

router = APIRouter(prefix='/api/course', tags=['course'])


@router.get("/", response_model=List[api.ApiCourse])
async def get_all_courses(*, user=Depends(get_current_user), session=Depends(get_session)):
    """
    get all courses
    """
    return session.exec(select(database.Course)).all()


@router.post("/", response_model=api.ApiCourse)
async def add_course(course_create: api.ApiCourse,
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
    )
    course_create_dict = course_create.dict(exclude_unset=True)
    for key, value in course_create_dict.items():
        # NOTE: this 'merge blocklist' is dangerous: since the keys are hardcoded in a string they will not
        # be detected by the linter if the class attributes are changed in the future
        if key not in ['jury', 'buoys', 'creation_date']:
            setattr(course, key, value)
    # create the jury
    jury_id = str(uuid.uuid4())
    jury_create_dict = course_create.jury.dict(exclude_unset=True)
    jury = database.BuoyJury(
        **jury_create_dict,
        id=jury_id
    )
    # update the course with the jury id
    course.jury_id = jury_id
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
        raise HTTPException(status_code=400, detail="course_already_exist")
    return course


@router.put("/", response_model=api.ApiCourse)
async def update_course(
        course_update: api.ApiCourse,
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
    course_update_dict = course_update.dict(exclude_unset=True)
    for key, value in course_update_dict.items():
        # NOTE: this 'merge blocklist' is dangerous: since the keys are hardcoded in a string they will not
        # be detected by the linter if the class attributes are changed in the future
        if key not in ['jury', 'buoys']:
            setattr(course, key, value)
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


@router.delete("/{course_name}")
async def update_course(
        course_name: str,
        admin_user=Depends(get_current_admin_user),
        session = Depends(get_session)
):
    course: database.Course = session.get(database.Course, course_name)
    if not course:
        raise HTTPException(status_code=404, detail="course_not_found")
    jury = course.jury
    buoys = course.buoys
    #TODO: replace this manual work with the sqlalchemy relationship deletion features
    for buoy in buoys:
        session.delete(buoy)
    session.delete(course)
    session.delete(jury)
    session.commit()
    return "ok"

@router.post("/{course_name}/buoy/{buoy_id}/assign_roboa")
async def buoy_assign_roboa(
        course_name: str,
        buoy_id: int,
        roboa_get: api.RoboaGet,
        admin_user=Depends(get_current_admin_user),
        session: Session = Depends(get_session)
):
    """
    assign a roboa to a buoy. As of now it is not possible to assign a roboa to the jury buoy

    This operation will not cause the roboa to move!
    If you want to move the roboa use the roboa/move endpoint
    """
    # get the roboa
    roboa = session.get(database.Roboa, roboa_get.name)
    if roboa is None:
        raise HTTPException(status_code=404, detail="roboa_not_found")
    # get the buoy
    buoy = session.exec(
        select(database.Buoy).where(
            database.Buoy.id == buoy_id, database.Buoy.course_id == course_name
        )
    ).first()
    if buoy is None:
        raise HTTPException(status_code=404, detail="buoy_not_found")

    roboa.assigned_buoy = buoy_id
    session.add(roboa)
    session.commit()
    session.refresh(roboa)

    return "ok"
