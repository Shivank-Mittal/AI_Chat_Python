from dto.gemini_dto import GeminiDTO
from chat.bot import gemini_query

def chat(content):
    try:
        response = gemini_query(content)
        candidate = response.candidates[0]
        content = candidate.content
        text = content.parts[0].text
        # token_count = candidate.token_count

        value = GeminiDTO(text= text, role= "Assistant", token_count = 24)
        return value
    except:
        return {text: "Error Accrued"}


def chat_health_check():
    try:
        response = gemini_query("Are you connected")
        if response.candidates:
            return True
        else:
            return False
    except:
        return False

