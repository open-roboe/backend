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

class JuryCreate(BaseModel):
    description: Optional[str]
    color: Optional[int]
    lat: float
    lon: float


class JuryUpdate(BaseModel):
    description: Optional[str]
    color: Optional[int]
    lat: Optional[float]
    lon: Optional[float]

class JuryResponse(BaseModel):
    description: Optional[str] = ""
    color: Optional[int] = 0
    lat: float
    lon: float

# ====================
# Buoy

class BuoyCreate(BaseModel):
    id: int
    description: Optional[str]
    color: Optional[int]
    lat: float
    lon: float


class BuoyUpdate(BaseModel):
    id: int
    description: Optional[str]
    color: Optional[int]
    lat: Optional[float]
    lon: Optional[float]

class BuoyResponse(database.BuoyBase):
    pass

# ====================
# Course

class CourseCreate(database.CourseBase):
    jury: JuryCreate
    buoys: List[BuoyCreate]


class CourseUpdate(database.CourseBase):
    name: str
    type: Optional[str]
    jury: JuryUpdate
    buoys: List[BuoyUpdate]

class CourseResponse(database.CourseBase):
    creation_date: int
    #these are not database fields!
    jury: JuryResponse
    buoys: List[database.Buoy]


# ====================
# polling

class PollResponse(BaseModel):
    courses: List[CourseResponse]
    users: List[UserResponse]
    roboas: List[RoboaResponse]


class PollUserUpdate(BaseModel):
    lat: float
    lon: float


class PollRoboaUpdate(BaseModel):
    lat: float
    lon: float
