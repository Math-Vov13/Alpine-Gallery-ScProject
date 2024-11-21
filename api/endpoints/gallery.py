from fastapi import APIRouter
from fastapi import UploadFile, File
from fastapi.responses import StreamingResponse, FileResponse

from typing import Annotated

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
async def create_file(files: Annotated[list[UploadFile], File(description="A file read as UploadFile")]):
    return dict([(file.filename, {'name': file.filename, 'size': file.size}) for file in files])

@router.delete("/{media_id}")
def aa():
    pass