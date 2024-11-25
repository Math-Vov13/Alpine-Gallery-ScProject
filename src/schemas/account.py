# API
# Mathéo Vovard

from pydantic import BaseModel, Field
from typing_extensions import Annotated, Doc


class HTTPCredentials(BaseModel):
    email: Annotated[str, Doc("The HTTP Basic email.")]
    password: Annotated[str, Doc("The HTTP Basic password.")]


class LoginModel(BaseModel):
    model_config = {"extra": "forbid"}

    email: str = Field(
        title="Email", examples=["test@gmail.com"], max_length=50
    )
    password: str = Field(
        title="Password", examples=["password"], max_length=50
    )


class RegisterModel(BaseModel):
    model_config = {"extra": "forbid"}

    name: str = Field(
        title="Name", examples=["username"], max_length=20
    )
    email: str = Field(
        title="Email", examples=["test@gmail.com"], max_length=50
    )
    password: str = Field(
        title="Password", examples=["password"], max_length=50
    )


class Account_Schema_DB(BaseModel):
    id: int                         # id
    name: str                       # account name
    email: str                      # account email
    password: str                   # account password