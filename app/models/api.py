from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field

from . import database

# ====================
# user and auth models

class UserCreate(BaseModel):
    username: str
    password: str
    admin: bool = False
    super_admin: bool = False


class UserResponse(database.UserBase):
    pass


class AuthToken(BaseModel):
    access_token: str
    token_type: str


# ====================
# roboa

class RoboaCreate(BaseModel):
    name: str
    token: str


class RoboaResponse(database.RoboaBase):
    pass


class RoboaGet(BaseModel):
    name: str

# ====================
# Jury

class ApiJury(BaseModel):
    description: Optional[str]
    color: Optional[int]
    lat: Optional[float]
    lon: Optional[float]

# ====================
# Buoy

class ApiBuoy(BaseModel):
    id: int
    description: Optional[str]
    color: Optional[int]
    lat: Optional[float]
    lon: Optional[float]

# ====================
# Course

class ApiCourse(database.CourseBase):
    creation_date: Optional[int]
    #these are not database fields!
    jury: ApiJury
    buoys: List[ApiBuoy]

# ====================
# polling

class PollResponse(BaseModel):
    courses: List[ApiCourse]
    users: List[UserResponse]
    roboas: List[RoboaResponse]


class PollUserUpdate(BaseModel):
    lat: float
    lon: float


class PollRoboaUpdate(BaseModel):
    lat: float
    lon: float
