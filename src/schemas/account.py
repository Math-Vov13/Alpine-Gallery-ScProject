# API
# Mathéo Vovard

from pydantic import BaseModel, Field
from typing_extensions import Annotated, Doc
from src.Core.Config import CONFIG


class HTTPCredentials(BaseModel):
    email: Annotated[str, Doc("The HTTP Basic email.")]
    password: Annotated[str, Doc("The HTTP Basic password.")]


class LoginModel(BaseModel):
    model_config = {"extra": "forbid"}

    email: str = Field(
        title="Email", examples=["test@gmail.com"], min_length=10, max_length=CONFIG.MAX_ACCOUNT_EMAIL_CHARS
    )
    password: str = Field(
        title="Password", examples=["password"], min_length=8, max_length=CONFIG.MAX_ACCOUNT_PASSWORD_CHARS
    )


class RegisterModel(BaseModel):
    model_config = {"extra": "forbid"}

    name: str = Field(
        title="Name", examples=["username"], min_length=5, max_length=CONFIG.MAX_ACCOUNT_NAME_CHARS
    )
    email: str = Field(
        title="Email", examples=["test@gmail.com"], min_length=10, max_length=CONFIG.MAX_ACCOUNT_EMAIL_CHARS
    )
    password: str = Field(
        title="Password", examples=["password"], min_length=8, max_length=CONFIG.MAX_ACCOUNT_PASSWORD_CHARS
    )


class Account_Schema_DB(BaseModel):
    id: int                         # id
    name: str                       # account name
    email: str                      # account email
    password: str                   # account password
    ip_address: str                 # client ip