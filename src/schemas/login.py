# API
# Mathéo Vovard

from pydantic import BaseModel, Field

class LoginModel(BaseModel):
    model_config = {"extra": "forbid"}

    email: str = Field(
        title="Email", examples=["test@gmail.com"], max_length=50
    )
    password: str = Field(
        title="Password", examples=["password"], max_length=50
    )