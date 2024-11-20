# API
# Mathéo Vovard

from pydantic import BaseModel, Field

class LoginModel(BaseModel):
    model_config = {"extra": "forbid"}

    email: str = Field(
        title="Email", max_length=50, min_length=10
    )
    password: str = Field(
        title="Password", max_length=50, min_length=5
    )