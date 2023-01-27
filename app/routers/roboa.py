from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from fastapi.responses import JSONResponse
from fastapi.logger import logger
from app.database import engine
from typing import List
from app.auth import get_current_user, get_current_admin_user, get_current_super_admin_user
from ..models import database, api #same as "from app.models import database"


router = APIRouter(prefix='/api/roboa', tags=['roboa'])


@router.get("/", response_model=List[api.RoboaResponse])
async def get_all_roboas(*, user = Depends(get_current_user)):
    """
    TOTEST
    get all roboas
    """
    with Session(engine) as session:
        roboas = session.exec(select(database.Roboa)).all()
        return roboas


@router.post("/", response_model=api.RoboaResponse)
async def add_roboa(roboa: api.RoboaCreate, admin_user = Depends(get_current_admin_user)):
    """
    TOIMPLEMENT
    Add a roboa
    """
    #hash the token

    # with Session(engine) as session:
    #     session.add(course)
    #     session.commit()
    #     session.refresh(course)
    #     return course
    return "ok"

@router.delete("/{name}")
async def delete_roboa(name: str, admin_user = Depends(get_current_admin_user)):
    """
    TOIMPLEMENT
    delete a roboa
    """
    return "ok"


@router.put("/{name}/move")
async def assign_target_coords(name: str, coords: api.Coords, user = Depends(get_current_admin_user)):
    """
    TOIMPLEMENT
    set the target coordinates of the specified roboa,
    causing it to move to the location
    """
    return "ok"
