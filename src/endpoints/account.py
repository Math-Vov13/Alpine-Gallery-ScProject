from fastapi import APIRouter, status, HTTPException, Form
from fastapi.responses import JSONResponse, RedirectResponse

from typing import Annotated
from base64 import b64encode

from Core.Config import CONFIG
from model.account_db import create_account, get_account
from schemas.account import LoginModel, RegisterModel



router = APIRouter(prefix= "", tags= ["Account"])



@router.post("/register",
          tags=["Account"],
          description="", status_code=status.HTTP_201_CREATED)
async def register(data_form: Annotated[RegisterModel, Form()]):
    error_response = await create_account(data_form)
    if type(error_response) == str:
        return JSONResponse({"success": False, "message": error_response})

    return JSONResponse({"success": True, "message": "Account created successfully."})


@router.post("/login",
          tags=["Account"],
          description="", status_code=status.HTTP_200_OK)
async def login(data_form: Annotated[LoginModel, Form()]):
    if not await get_account(data_form):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Not Found!")
    
    credentials = b64encode(f"{data_form.email}:{data_form.password}".encode('utf-8')).decode('utf-8')

    # return RedirectResponse(f"{CONFIG.get_BASE_URL()}/dashboard", status_code= 303,
    #     headers={"Authorization": f"Basic {credentials}"}
    # )
    
    response = JSONResponse({"success": True, "message": "Login successful."})
    response.headers['X-Redirect'] = '/dashboard'

    return response