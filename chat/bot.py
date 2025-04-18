from typing import Any, List
from google import genai
from google.genai import types
from prompt.two_shot import prompt
from prompt.chain_of_thoughts import prompt as helper_prompt
from dto.gemini_input_dto import Context
from dto import gemini_smart_dto

client = genai.Client(api_key="AIzaSyCgi4UT9risn5UYU9mcY0SxbLoZlWx6mrw")

def gemini_query(content: List[Context]):
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents = content,
        config= types.GenerateContentConfig(
            system_instruction= prompt,
            
        )
    )
    return response


def gemini_smart_resolver(content: List[Context]):
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents = content,
        config= types.GenerateContentConfig(
            system_instruction= helper_prompt,
            response_mime_type= "application/json"
        )
    )
    return response