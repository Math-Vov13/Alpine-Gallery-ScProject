# API
# Mathéo Vovard

from pydantic import BaseModel, Field

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