from typing import Annotated, Optional

from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from model.account_db import get_account
from schemas.account import *


router = APIRouter()
security = HTTPBasic()


async def get_current_username(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
) -> Account_Schema_DB:
    print(credentials)
    thisuser = await get_account(LoginModel(
        email= credentials.username,
        password= credentials.password
    ))

    if not thisuser:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return thisuser.model_dump()


async def get_credentials(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
) -> Optional[Account_Schema_DB]:
    print(credentials)
    thisuser = await get_account(LoginModel(
        email= credentials.username,
        password= credentials.password
    ))

    if thisuser:
        return thisuser


# @router.get("/users/me")
# def read_current_user(username: Annotated[str, Depends(get_current_username)]):
#     return {"username": username}