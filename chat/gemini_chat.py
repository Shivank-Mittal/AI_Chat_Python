from typing import List

from fastapi.exceptions import ValidationException
from dto.gemini_dto import GeminiDTO
from dto.gemini_step_dto import Step
from chat import bot
from dto.gemini_input_dto import Context, Part
from tools.tools import available_tools
import json

def chat(content: List[Context]):
    try:
        response = bot.gemini_query(content)
        candidate = response.candidates[0]
        content = candidate.content
        message:str = str(content.parts[0].text.strip())
        value = GeminiDTO(text = message, role= "Assistant", token_count = 24)
        return value
    except ValidationException as e:
        return {"text": "API Error Occurred"}
    except Exception as e:
        print(e)
        return {"text": "Error Accrued"}
    

def chatWithHelper(content: List[Context]):
    while True:
        try:
            response = bot.gemini_smart_resolver (content)
            candidate = response.candidates[0]
            responseContent = candidate.content
            message:str = str(responseContent.parts[0].text.strip())
            value = json.loads(message)
            step = Step(**value)

            if(step.step == "plan"):
                # print(f"🧠: {step.content}")
                content.append(Context(role="model", parts = [Part(text= step.json())]))
                continue

            if(step.step == "action"):
                # print(f"🔨: {step.content}")
                tool_name = step.function
                tool_input = step.input
                if available_tools.get(tool_name, False) == False:
                    return GeminiDTO(text = "Sorry i dont have this capability nowi", role= "Assistant", token_count = 24)
                output = available_tools[tool_name].get('fn')(tool_input)
                tempStep = Step(step="observe", output = output.text)
                content.append(Context(role="model", parts = [Part(text= tempStep.json())]))
                continue
            if(step.step == "output"):
                # print(f"🤖: {step.content}")
                return GeminiDTO(text = step.content, role= "Assistant", token_count = 24);

        except ValidationException as e:
            return {"text": "API Error Occurred"}
        except Exception as e:
            print(e)
            return {"text": "Error Accrued"}



def chat_health_check():
    try:
        response = bot.gemini_query("Are you connected")
        if response.candidates:
            return True
        else:
            return False
    except:
        return False

