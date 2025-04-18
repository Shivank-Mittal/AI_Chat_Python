from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google import genai
from chat import gemini_chat
from chat.bot import gemini_query
from dto import gemini_input_dto
from config.cors import allow_origins


app = FastAPI();
app.add_middleware(
    CORSMiddleware,
        allow_origins = [
            "https://shivankmittal.com",
            "https://www.shivankmittal.com",
            "http://localhost:4200"
        ],
        allow_methods=["*"],
        allow_headers=["*"],
)

client = genai.Client(api_key="AIzaSyCgi4UT9risn5UYU9mcY0SxbLoZlWx6mrw")


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
def chat_with_bot(request_body: gemini_input_dto.Content):
    return gemini_chat.chat(request_body.content)


@app.post("/smart")
def chatWithHelper(request_body: gemini_input_dto.Content):
    return gemini_chat.chatWithHelper(request_body.content)