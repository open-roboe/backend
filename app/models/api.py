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

class UserGet(BaseModel):
    username: str

class UserUpdate(BaseModel):
    lat: Optional[float] = 0
    lon: Optional[float] = 0
    course_id: Optional[str] = Field(default=None, foreign_key="course.name")

class RoboaCreate(BaseModel):
    name: str
    token: str

class RoboaResponse(database.RoboaBase):
    pass

class RoboaGet(BaseModel):
    name: str

class RoboaUpdate(BaseModel):
    lat: Optional[float] = 0
    lon: Optional[float] = 0
    course_id: Optional[str] = Field(default=None, foreign_key="course.name")


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
