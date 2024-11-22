# API
# Mathéo Vovard

from pydantic import BaseModel

class file(BaseModel):
    id : int
    name: str
    size: int
    content_type: str

class file_json(BaseModel):
    content: bytes