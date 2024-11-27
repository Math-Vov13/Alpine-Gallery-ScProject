from hypercorn.config import Config
from hypercorn.asyncio import serve

from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

import os
import asyncio
import logging
from typing import Annotated, Optional

from src.Core.Config import CONFIG
from src.api import subapp
from src.schemas.account import *
from src.endpoints.middlewares.auth import get_credentials


# Configurer le module logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[CONFIG.get_BASE_URL()],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]

)

templates = Jinja2Templates("./src/templates")


@app.get("/")
def index(request : Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.get("/dashboard")
def dashboard(credentials: Annotated[Account_Schema_DB, Depends(get_credentials)], request: Request):
    print(credentials)
    if not credentials:
        return RedirectResponse(url= "/") # redirect to login page

    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "credentials": {
            "name": credentials.name,
            "username": credentials.email,
            "password": credentials.password
        }}
    )



app.mount("/css", StaticFiles(directory= "./src/templates/css"), name="static")
app.mount("/img", StaticFiles(directory= "./src/templates/images"), name="static")
app.mount("/api/v1", subapp)


if __name__ == "src.main":
    config = Config()
    config.bind = [f"0.0.0.0:{os.getenv('PORT', 8000)}"]
    asyncio.run(serve(app, config))