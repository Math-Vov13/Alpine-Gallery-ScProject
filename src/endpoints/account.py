from fastapi import APIRouter, status, HTTPException, Form
from fastapi.responses import JSONResponse, RedirectResponse
from typing import Annotated
from model.account_db import create_account, get_account
from schemas.login import LoginModel
from schemas.register import RegisterModel

router = APIRouter(prefix= "", tags= ["Account"])



@router.post("/register",
          tags=["Account"],
          description="", status_code=status.HTTP_201_CREATED)
async def register(data_form: Annotated[RegisterModel, Form()]):
    if not await create_account(data_form):
        return JSONResponse({"success": False, "message": "Error!"})

    return JSONResponse({"success": True, "message": "Account created successfully."})


@router.post("/login",
          tags=["Account"],
          description="", status_code=status.HTTP_200_OK)
async def login(data_form: Annotated[LoginModel, Form()]):
    if not await get_account(data_form):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Not Found!")
    
    return JSONResponse({"success": True, "message": "Login successful."})