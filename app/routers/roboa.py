from typing import List
import time
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from app.auth import get_current_user, get_current_admin_user, get_password_hash
from app.database import engine, get_session
from ..models import database, api  # same as "from app.models import database"

router = APIRouter(prefix='/api/roboa', tags=['roboa'])


@router.get("/", response_model=List[api.RoboaResponse])
async def get_all_roboas(*, user=Depends(get_current_user)):
    """
    get all roboas
    """
    with Session(engine) as session:
        roboas = session.exec(select(database.Roboa)).all()
        return roboas


@router.post("/", response_model=api.RoboaResponse)
async def add_roboa(
        roboa: api.RoboaCreate,
        admin_user=Depends(get_current_admin_user),
        session: Session = Depends(get_session)
):
    """
    Register a new roboa in the system
    """
    # hash the token
    hashed_token = get_password_hash(roboa.token)
    # create the roboa
    roboa = database.Roboa(
        name=roboa.name,
        hashed_token=hashed_token,
        last_update=time.time()
    )
    session.add(roboa)
    try:
        session.commit()
        session.refresh(roboa)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="roboa_name_already_exists")
    except Exception as e:
        raise HTTPException(status_code=500, detail="registration_failed")

    return roboa


@router.delete("/{name}")
async def delete_roboa(name: str, admin_user=Depends(get_current_admin_user)):
    """
    TOIMPLEMENT
    delete a roboa
    """
    return "ok"


@router.put("/{name}/move_to_buoy")
async def move_to_assigned_buoy(name: str, user=Depends(get_current_admin_user)):
    """
    TOIMPLEMENT
    set the target coordinates of the specified roboa,
    causing it to move to the location
    """
    return "ok"
