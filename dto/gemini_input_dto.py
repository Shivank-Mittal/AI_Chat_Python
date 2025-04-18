from typing import List, Dict
from pydantic import BaseModel

class Part(BaseModel):
    text: str

class Context(BaseModel):
    role: str
    parts: List[Part]

class Content(BaseModel):
    content: List[Context]

