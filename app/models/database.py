"""Models for the mongoDb collections
"""

from typing import Optional

from sqlmodel import Field, SQLModel, create_engine

class UserBase(SQLModel):
    username: str = Field(primary_key=True)
    admin: bool = True
    super_admin: bool = False
    last_update: int
    lat: Optional[float] = 0
    lon: Optional[float] = 0
    course_id: Optional[str] = Field(default=None, foreign_key="course.name")

class RoboaBase(SQLModel):
    name: str = Field(primary_key=True)
    last_update: int
    lat: Optional[float] = 0
    lon: Optional[float] = 0
    eta: Optional[int] = 0 #estimate time of arrival
    assigned_buoy: Optional[int] = Field(default=None, foreign_key="buoy.id")
    target_lat: Optional[float] = 0
    target_lon: Optional[float] = 0

class BuoyBase(SQLModel):
    id: str = Field(primary_key=True)
    description: Optional[str] = ""
    color: Optional[int] = 0
    lat: int
    lon: int


class User(UserBase, table=True):
    hashed_password: str

class Roboa(RoboaBase, table=True):
    hashed_token: str

class Course(SQLModel, table=True):
    name: str = Field(primary_key=True)
    creation_date: int
    type: str
    jury_id: Optional[str] = Field(default=None, foreign_key="buoyjury.id")


class Buoy(BuoyBase, table=True):
    course_id: str = Field(foreign_key="course.name")

class BuoyJury(BuoyBase, table=True):
    pass
