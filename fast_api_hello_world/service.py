from fastapi.responses import JSONResponse
from fastapi import FastAPI
import requests
import json


api = FastAPI()
WEATHER_API_TOKEN = "da00a2d85203422db90195136232501"


@api.get("/weather")
def weather(city):
    error = json.dumps({"error": "Error has corrupted"})
    try:
        response = requests.get(
            f"https://api.weatherapi.com/v1/current.json?key=da00a2d85203422db90195136232501&q={city}&aqi=no")
        info = {"city": json.loads(response.text)["location"]["name"],
                "temp": json.loads(response.text)["current"]["temp_c"],
                "humidity": json.loads(response.text)["current"]["humidity"]}
        return JSONResponse(info)
    except Exception as err:
        print(err)
        return JSONResponse(json.loads(error)["error"])
