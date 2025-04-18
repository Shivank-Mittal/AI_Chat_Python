import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')
MODEL = os.getenv("MODEL")

client = genai.Client(API_KEY)
