from google import genai
from google.genai import types
from prompt.two_shot import prompt

client = genai.Client(api_key="AIzaSyCgi4UT9risn5UYU9mcY0SxbLoZlWx6mrw")

def gemini_query(content: str):
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents = content,
        config= types.GenerateContentConfig(
            system_instruction= prompt,
        )
    )
    return response