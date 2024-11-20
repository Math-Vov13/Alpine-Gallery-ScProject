# API
# Mathéo Vovard

from fastapi import FastAPI, Form, status, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from typing import Annotated

from model.account_db import *
from schemas.login import LoginModel
from schemas.register import RegisterModel


app = FastAPI(root_path="/api/v1", root_path_in_servers="/api/v1")
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://127.0.0.1:8000", "*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)




@app.get("/")
def index():
    return RedirectResponse(
        url= "/index.html"  # redirection vers le site web
    )

@app.post("/register",
          tags=["Account"],
          description= "", status_code=status.HTTP_201_CREATED)
async def test(data: Annotated[RegisterModel, Form()]):
    await create_account(data)


@app.post("/login",
          tags=["Account"],
          description= "", status_code= status.HTTP_200_OK)
async def test(data: Annotated[LoginModel, Form()]):
    if not await get_account(data):
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= "Not Found!")