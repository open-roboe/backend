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

# polling 
class PollResponse(BaseModel):
    courses: List[database.Course]
    users: List[UserResponse]
    roboas: List[RoboaResponse]


class PollUserUpdate(BaseModel):
    lat: float
    lon: float

class PollRoboaUpdate(BaseModel):
    lat: float
    lon: float


class AuthToken(BaseModel):
    access_token: str
    token_type: str

# roboa

class Coords(BaseModel):
    lat: float
    lon: float

class RoboaGet(BaseModel):
    name: str
# course

class CourseCreate(BaseModel):
    name: str
    type: str

class BuoyCreate(BaseModel):
    description: Optional[str]
    color: Optional[int]
    lat: int
    lon: int

class BuoyUpdate(BaseModel):
    description: Optional[str]
    color: Optional[int]
    lat: Optional[int]
    lon: Optional[int]

