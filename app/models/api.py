from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field, constr


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
