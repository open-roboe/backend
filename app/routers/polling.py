from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.logger import logger
from sqlmodel import Field, Session, select
import time
from app.database import engine
from ..models import database, api #"from app.models import database" is better, but not recognized by my linter lol
from app.auth import get_current_user, get_current_admin_user, get_current_super_admin_user

router = APIRouter(prefix='/api/polling', tags=['polling'])



@router.post("/roboa")
async def poll_roboa_update(roboaData: api.PollRoboaUpdate):
    """
    Polling endpoint, called repeatedly by an authenticated roboa to send its metrics, and receive back commands

    This endpoint updates the roboa last_update timestamp
    """
    #TODO: define and implement
    return "commands to define"


@router.post("/user", response_model=api.PollResponse)
async def poll_user_update(new_data: api.PollUserUpdate, user: database.User = Depends(get_current_user)):
    """
    Polling endpoint, called repeatedly by an authenticated user to send its metrics
    and get data updates

    This endpoint updates the user last_update timestamp
    """
    #update user data with received metrics, and update last_update
    with Session(engine) as session:
        user.last_update = int(time.time())
        new_data = new_data.dict(exclude_unset=True)
        for key, value in new_data.items():
            setattr(user, key, value)
        session.add(user)
        session.commit()
        session.refresh(user)

    #read and return users, courses and roboas
    with Session(engine) as session:
        users = session.exec(select(database.User)).all()
        courses = session.exec(select(database.Course)).all()
        roboas = session.exec(select(database.Roboa)).all()
        return {
                'users': users,
                'courses': courses,
                'roboas': roboas
                }


@router.get("/", response_model=api.PollResponse)
async def poll(*, user: database.User = Depends(get_current_user)):
    """
    Polling endpoint, called repeatedly by an authenticated user to get data updates.
    This endpoint does not update user metrics
    """
    #read and return users, courses and roboas
    with Session(engine) as session:
        users = session.exec(select(database.User)).all()
        courses = session.exec(select(database.Course)).all()
        roboas = session.exec(select(database.Roboa)).all()
        return {
                'users': users,
                'courses': courses,
                'roboas': roboas
                }


