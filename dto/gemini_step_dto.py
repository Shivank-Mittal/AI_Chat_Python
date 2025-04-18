from pydantic import BaseModel
from typing import Optional

class Step(BaseModel):
    step: str
    content: Optional[str] = None
    function: Optional[str] = None
    input: Optional[str] = None
    output: Optional[str] = None