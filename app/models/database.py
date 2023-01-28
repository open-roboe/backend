"""Models for the mongoDb collections
"""

from typing import Optional, List

from sqlmodel import Field, SQLModel, create_engine, Relationship

# ====================
# base models, used by both db models and api models

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
    eta: Optional[int] = 0  # estimate time of arrival
    assigned_buoy: Optional[int] = Field(default=None, foreign_key="buoy.id")
    target_lat: Optional[float] = 0
    target_lon: Optional[float] = 0


class BuoyBase(SQLModel):
    id: str = Field(primary_key=True)
    description: Optional[str] = ""
    color: Optional[int] = 0
    lat: int
    lon: int

class CourseBase(SQLModel):
    name: str = Field(primary_key=True)
    creation_date: int
    type: str
    jury_id: Optional[str] = Field(default=None, foreign_key="buoyjury.id")


# ====================
# database models. It's not recomended to
# use these models for api operations

class User(UserBase, table=True):
    hashed_password: str


class Roboa(RoboaBase, table=True):
    hashed_token: str


class Course(CourseBase, table=True):
    jury: Optional["BuoyJury"] = Relationship()
    buoys: List["Buoy"] = Relationship()


class Buoy(BuoyBase, table=True):
    course_id: str = Field(foreign_key="course.name")


class BuoyJury(BuoyBase, table=True):
    pass
