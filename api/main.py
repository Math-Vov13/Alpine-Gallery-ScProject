from fastapi import FastAPI, status, HTTPException, Form
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated

from model.account_db import create_account, get_account
from schemas.login import LoginModel
from schemas.register import RegisterModel

app = FastAPI(root_path="/api/v1", root_path_in_servers="/api/v1")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)

@app.get("/")
def index():
    return RedirectResponse(
        url="/index.html"  # Redirection to the website
    )

@app.post("/register",
          tags=["Account"],
          description="", status_code=status.HTTP_201_CREATED)
async def register(data: RegisterModel):
    await create_account(data)
    return {"success": True, "message": "Account created successfully."}

@app.post("/login",
          tags=["Account"],
          description="", status_code=status.HTTP_200_OK)
async def login(
    email: str = Form(...), 
    password: str = Form(...)
):
    data = LoginModel(email=email, password=password)  # Construct the LoginModel manually
    if not await get_account(data):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Not Found!")
    return {"success": True, "message": "Login successful."}

