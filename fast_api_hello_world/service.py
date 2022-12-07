from fastapi import FastAPI
from starlette.responses import HTMLResponse
import time


api = FastAPI()


@api.get("/time")
def clock():
    local_time = time.localtime()
    time_string = time.strftime("%m/%d/%Y %H:%M:%S", local_time)
    return HTMLResponse(f"<h1>{time_string}</h1>")
