from fastapi.responses import JSONResponse
from fastapi import FastAPI
import requests
import json


api = FastAPI()
WEATHER_API_TOKEN = "da00a2d85203422db90195136232501"


@api.get("/weather")
def weather(city):
    error = json.dumps({"error": "Error has corrupted"})
    response = requests.get(f"https://api.weatherapi.com/v1/current.json?key=da00a2d85203422db90195136232501&q={city}&aqi=no")
    print(response)
    try:
        return JSONResponse(json.loads(response.text)["location"]["name"],
                            json.loads(response.text))
    finally:
        return JSONResponse(json.loads(error)["error"])
