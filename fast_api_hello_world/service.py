from starlette.responses import HTMLResponse
from fastapi import FastAPI
import requests
import json


api = FastAPI()
WEATHER_API_TOKEN = "da00a2d85203422db90195136232501"


@api.get("/weather")
def weather(city):
    response = requests.get(f"https://api.weatherapi.com/v1/current.json?key=da00a2d85203422db90195136232501&q={city}&aqi=no")
    location_info = json.loads(response.text)["location"]
    weather_info = json.loads(response.text)["current"]
    print(weather_info)
    return HTMLResponse(f"<h1>In {location_info['name']} temperature is {weather_info['temp_c']}°C and humidity is {weather_info['humidity']}%.</h1>")
