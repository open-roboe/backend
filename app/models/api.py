from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field

from . import database

class UserCreate(BaseModel):
    username: str
    password: str
    admin: bool = False
    super_admin: bool = False

class UserResponse(database.UserBase):
    pass

class RoboaCreate(BaseModel):
    name: str
    token: str

class RoboaResponse(database.RoboaBase):
    pass


class AuthToken(BaseModel):
    access_token: str
    token_type: str

# roboa

class RoboaGet(BaseModel):
    name: str
# course

class BuoyCreate(BaseModel):
    id: int
    description: Optional[str]
    color: Optional[int]
    lat: int
    lon: int

class BuoyUpdate(BaseModel):
    id: str
    description: Optional[str]
    color: Optional[int]
    lat: Optional[int]
    lon: Optional[int]

class CourseCreate(BaseModel):
    name: str
    type: str
    jury: BuoyCreate
    buoys: List[BuoyCreate]

class CourseUpdate(BaseModel):
    name: Optional[str]
    type: Optional[str]
    jury: BuoyUpdate
    buoys: List[BuoyUpdate]

class CourseResponse(BaseModel):
    name: str
    type: str
    jury: database.BuoyJury
    buoys: List[database.Buoy]

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

