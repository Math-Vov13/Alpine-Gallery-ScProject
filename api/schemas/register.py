# API
# Mathéo Vovard

from pydantic import BaseModel, Field

class RegisterModel(BaseModel):
    model_config = {"extra": "forbid"}

    name: str = Field(
        title="Name", max_length=20, min_length=5
    )
    email: str = Field(
        title="Email", max_length=50, min_length=10
    )
    password: str = Field(
        title="Password", max_length=50, min_length=10
    )