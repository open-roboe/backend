"""Models for the mongoDb collections
"""

from typing import Optional

from sqlmodel import Field, SQLModel, create_engine

class Course(SQLModel, table=True):
    name: str = Field(primary_key=True)
    data: str = ""

class User(SQLModel, table=True):
    username: str = Field(primary_key=True)
    admin: bool = True
    super_admin: bool = False
    hashed_password: str
    last_update: int
    lat: Optional[float] = 0
    lon: Optional[float] = 0
    course_id: Optional[str] = Field(default=None, foreign_key="course.name")

class Roboa(SQLModel, table=True):
    name: str = Field(primary_key=True)
    hashed_token: str
    last_update: int
    lat: Optional[float] = 0
    lon: Optional[float] = 0
    course_id: Optional[str] = Field(default=None, foreign_key="course.name")


