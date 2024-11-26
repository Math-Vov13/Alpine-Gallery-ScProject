from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from typing import Annotated, Optional

from Core.Config import CONFIG
from api import subapp
from schemas.account import *
from endpoints.middlewares.auth import get_credentials


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[CONFIG.get_BASE_URL()],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]

)

templates = Jinja2Templates("./templates")


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



app.mount("/css", StaticFiles(directory= "./templates/css"), name="static")
app.mount("/img", StaticFiles(directory= "./templates/images"), name="static")
app.mount("/api/v1", subapp)



# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(
#         "app:app",
#         host    = "0.0.0.0",
#         port    = 8036, 
#         reload  = True
#     )