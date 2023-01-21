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
    course_id: Optional[str] = Field(default=None, foreign_key="course.name")


class Course(SQLModel, table=True):
    name: str = Field(primary_key=True)
    data: str = ""

class User(UserBase, table=True):
    hashed_password: str

class Roboa(RoboaBase, table=True):
    hashed_token: str


