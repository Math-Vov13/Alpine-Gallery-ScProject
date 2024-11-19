from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

from typing import Annotated
from pydantic import BaseModel, Field

from db import *


app = FastAPI(root_path="/api/v1", root_path_in_servers="/api/v1")
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://127.0.0.1:8000"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


class RegisterModel(BaseModel):
    model_config = {"extra": "forbid"}

    name: str = Field(
        title="Name", max_length=20
    )
    email: str = Field(
        title="Email", max_length=50
    )
    password: str = Field(
        title="Password", max_length=50
    )


class LoginModel(BaseModel):
    model_config = {"extra": "forbid"}

    email: str = Field(
        title="Email", max_length=50
    )
    password: str = Field(
        title="Password", max_length=50
    )


@app.post("/register",
          tags=["Account"],
          description= "")
async def test(data: Annotated[RegisterModel, Form()]):
    return await create_account(data)


@app.post("/login",
          tags=["Account"],
          description= "")
async def test(data: Annotated[LoginModel, Form()]) -> bool:
    return await get_account(data)