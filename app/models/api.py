from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field, constr


#doto: move to db
class User(BaseModel):
    username: str
    admin: bool = True
    superAdmin: bool = False
    disabled: bool = False
    hashed_password: str

#doto: move to db
class Roboa(BaseModel):
    name: str
    hashed_token: str

#doto: move to db
class Course(BaseModel):
    id: str
    name: str
    data: str #technical data, such as wind, markers, etch.
              #todo: define better, or keep as blob


class LiveBoat(BaseModel): #una barca è una persona in realta
    regataId: str
    username: str
    lat: int
    lon: int
    time: int #unix timestamp of last update


class LiveRoboa(BaseModel):
    regataId: str
    name: str
    lat: int
    lon: int
    telemetry: str #todo: define better, or keep as blob
    time: int #unix timestamp of last update


class PollData(BaseModel):
    courses: list[Course]
    boats: list[LiveBoat]
    roboas: list[LiveRoboa]
    





class WsAPIError(BaseModel):
  success = False
  error: str
  description: str = Field(description="Human readable error description")

class WsApiResponse(BaseModel):
  success = True
  data: Dict = {}

class WsAPIRequest(BaseModel):
  command: str
  data: Dict = {}
