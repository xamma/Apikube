import sys
import socket
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

#-Configurations---------------------------
from models import AppSettings

#-Setup------------------------------------
app = FastAPI()
app_settings = AppSettings()
templates = Jinja2Templates(directory="templates")

#-API Area--------------------------------
# Root
@app.get("/")
def read_root(request: Request):
    hostname = socket.gethostname()
    message = app_settings.custom_message
    return templates.TemplateResponse("index.html", {"request": request, "hostname": hostname, "message": message})

if __name__ == "__main__":
    if "dev".lower() in sys.argv:
        print("Running in Dev-Mode")
        uvicorn.run(app="__main__:app", host="0.0.0.0", port=app_settings.api_port, reload=True)
    else:
        uvicorn.run(app="__main__:app", host="0.0.0.0", port=app_settings.api_port)