from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from chat import gemini_chat
from chat.bot import gemini_query
from dto import gemini_input_dto

app = FastAPI();
app.add_middleware(
    CORSMiddleware,
        allow_origins= [
            "https://shivankmittal.com",
            "https://www.shivankmittal.com",
            # "http://localhost:4200"
        ],
        allow_methods=["*"],
         allow_headers=["*"],
)

# To me moved in its own class
class Tea(BaseModel):
    id: int
    name: str
    origin: str


teas: List[Tea] = []

@app.get("/")
def read_root():
    return "Welcome to chat system"



@app.get("/server")
def read_root():
    return True
        

@app.get("/connected")
def read_root():
    return gemini_chat.chat_health_check()


@app.post("/chat")
def chat_with_bot(dto: gemini_input_dto.Gemini_Input_DTO):
    return gemini_chat.chat(dto.content)