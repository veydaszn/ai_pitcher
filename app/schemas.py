from pydantic import BaseModel
from typing import List

class PitchRequest(BaseModel):
    idea: str

class PitchResponse(BaseModel):
    names: List[str]
    slogans: List[str]
