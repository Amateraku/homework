from fastapi.responses import JSONResponse
from fastapi import FastAPI
import requests
import json

api = FastAPI()
WEATHER_API_TOKEN = "da00a2d85203422db90195136232501"


@api.get("/weather")
def weather(city):
    error_messages = json.dumps({"error": "Error has corrupted"})
    try:
        weather_info = requests.get(
            f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API_TOKEN}={city}&aqi=no")
        weather_for_user = {"city": json.loads(weather_info.text)["location"]["name"],
                            "temp": json.loads(weather_info.text)["current"]["temp_c"],
                            "humidity": json.loads(weather_info.text)["current"]["humidity"]}
        return JSONResponse(weather_for_user)
    except Exception as err:
        print(err)
        return JSONResponse(json.loads(error_messages)["error"])
