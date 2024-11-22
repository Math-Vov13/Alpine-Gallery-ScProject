from fastapi import APIRouter, HTTPException
from fastapi import UploadFile, File
from fastapi.responses import FileResponse, JSONResponse

from typing import Annotated

from model.media_db import media_db

router = APIRouter(prefix= "/gallery", tags=["Gallery"])


@router.get("/")
async def get_all_file():
    return await media_db.get_all_files()


@router.get("/{media_id}")
async def upload_file(media_id: int):
    thisfile = await media_db.get_media_by_id(media_id= media_id)
    if not thisfile:
        raise HTTPException(status_code= 404,
                            detail= "This file doesn't exists!")
    
    return thisfile.model_dump()
    """
    EXAMPLE

    @router.get("/payments/xlsx", response_description='xlsx')
    async def payments():
        output = BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()
        worksheet.write(0, 0, 'ISBN')
        worksheet.write(0, 1, 'Name')
        worksheet.write(0, 2, 'Takedown date')
        worksheet.write(0, 3, 'Last updated')
        workbook.close()
        output.seek(0)

        headers = {
            'Content-Disposition': 'attachment; filename="filename.xlsx"'
        }
        return StreamingResponse(output, headers=headers)
    """
    
    # return UploadFile(file= )

# @router.post("/file")
# async def myfile(file: Annotated[bytes, File()]):
#     print(file)
#     return {'file': file.decode()}

@router.post("/")
async def create_files(files: Annotated[list[UploadFile] | None, File(description="A file read as UploadFile")]):
    if not files:
        raise HTTPException(status_code=400,
                            detail= "Array is empty!")

    data_list = []
    
    for file in files:
        print(await file.read())
        new_media_id = await media_db.save_file(file)
        data_list.append(await media_db.get_media_by_id(new_media_id))

    return dict([(file.name, file.model_dump()) for file in data_list])

@router.delete("/{media_id}")
async def delete_file(media_id_list: list[int]):
    if len(media_id_list) == 0:
        raise HTTPException(status_code= 400,
                            detail= "Array is empty!")

    if len(media_id_list) == 1 and not await media_db.get_media_by_id(media_id= media_id_list[0]):
        raise HTTPException(status_code= 404,
                            detail= "This file doesn't exists!")
    
    files_deleted = []
    for media_id in media_id_list:
        if await media_db.delete_file(media_id= media_id):
            files_deleted.append(media_id)
    
    return {"success": not len(files_deleted) == 0, "deleted": files_deleted}