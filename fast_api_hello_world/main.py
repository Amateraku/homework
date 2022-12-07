import uvicorn
from service import api


uvicorn.run(app=api, host="127.0.0.1", port=8080)
