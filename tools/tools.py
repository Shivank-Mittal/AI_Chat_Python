
import requests

def get_wether(cityName):
    # print("Tool is looking 👀", cityName)
    response  = requests.get(f"https://wttr.in/{cityName}?format=%C+%t")
    return response



available_tools  = {
    "get_weather": {
        "fn": get_wether,
        "description": "Takes a city name as an input and returns the current weather of that city"
    }
}