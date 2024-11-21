from fastapi import APIRouter, status, HTTPException, Form
from fastapi.responses import JSONResponse, RedirectResponse
from typing import Annotated
from model.account_db import create_account, get_account
from schemas.login import LoginModel
from schemas.register import RegisterModel

router = APIRouter(prefix= "/account", tags= ["Account"])



@router.post("/register",
          tags=["Account"],
          description="", status_code=status.HTTP_201_CREATED)
async def register(data: RegisterModel):
    await create_account(data)
    return {"success": True, "message": "Account created successfully."}


@router.post("/login",
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