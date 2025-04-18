from pydantic import BaseModel
class GeminiDTO(BaseModel):
    text:str
    role:str
    token_count: int

