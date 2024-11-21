from fastapi import APIRouter
from fastapi import UploadFile, File
from fastapi.responses import FileResponse

from typing import Annotated

from model.media_db import *

router = APIRouter(prefix= "/gallery", tags=["Gallery"])


@router.get("/")
async def get_all_file():
    return {}

async def file_generator(media_id: str):
    for _ in range(10):
        yield b"some fake video bytes"

@router.get("/{media_id}")
async def upload_file(media_id: str):
    return FileResponse(
        path= "",
        status_code= 200
    )

# @router.post("/file")
# async def myfile(file: Annotated[bytes, File()]):
#     print(file)
#     return {'file': file.decode()}

@router.post("/")
async def create_files(files: Annotated[list[UploadFile] | None, File(description="A file read as UploadFile")]):
    for file in files:
        await save_file(file.filename)
    return dict([(file.filename, {'name': file.filename, 'size': file.size}) for file in files])

@router.delete("/{media_id}")
def delete_file(media_id: str):
    pass