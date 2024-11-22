from fastapi import APIRouter, HTTPException, status, Query
from fastapi import UploadFile, File
from fastapi.responses import FileResponse, JSONResponse

from typing import Annotated, Optional

from model.media_db import media_db, media_utils
from schemas.gallery import *

router = APIRouter(prefix= "/gallery", tags=["Gallery"])


@router.get("/")
async def get_all_file(start: Annotated[int, Query()]= 0, step: Annotated[int, Query()]= 50):
    return await media_db.get_all_files()


@router.get("/{media_id}")
async def upload_file(media_id: int):
    thisfile = await media_db.get_media_by_id(media_id= media_id)
    if not thisfile:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= "This file doesn't exists!",
                            headers= {"media_id": str(media_id)})
    
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
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail= "Array is empty!")

    data_list = []
    
    for file in files:
        # print(await file.read())

        # vérifie la validité du nom du fichier
        name, ext = await media_utils.separate_path_and_ext(file.filename)
        if not name or not ext:
            continue # Erreur dans le nom !
        if not await media_utils.is_name_accepted(name):
            continue # Le nom n'est pas accepté !
        ext = await media_utils.get_ext_enum(ext)
        if not ext:
            continue # L'extension n'est pas acceptée !

        print("Enum :", repr(ext))
        new_media_id = await media_db.save_file(Update_File_Schema(name= name, ext= ext), file)
        data_list.append(await media_db.get_media_by_id(new_media_id))

    # les fichiers qui ne sont pas dans le bon format ont été oublié (ils ne seront pas renvoyés dans la réponse)
    return {"length": len(data_list),
            "elements" : dict([(file.name, file.model_dump()) for file in data_list])}


@router.put("/{media_id}", status_code= status.HTTP_200_OK)
async def update_file(media_id: int, fullname: str):
    # Géré par FastAPI
    # if not fullname:
    #     raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,
    #                         detail= "At least one query parameter must be not empty!")

    if not await media_db.get_media_by_id(media_id= media_id):
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= "This file doesn't exists!",
                            headers= {"media_id": str(media_id)})


    new_name, new_extension = await media_utils.separate_path_and_ext(fullpath= fullname)

    if not await media_utils.is_name_accepted(name= new_name):
        raise HTTPException(status_code= status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                            detail= f"['{fullname}'] is not supported!")

    new_extension = await media_utils.get_ext_enum(ext= new_extension)
    if not new_extension:
        raise HTTPException(status_code= status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                            detail= f"['{fullname}'] is not supported!")


    if not await media_db.update_file(media_id, changes= Update_File_Schema(
        media_id= media_id,
        name= new_name,
        ext= new_extension
    )):
        return {"success": False, "message": "Operation failed!"}
    
    return {"success": True, "message": "Changed successfully"}


@router.delete("/{media_id}")
async def delete_file(media_id_list: list[int]):
    if len(media_id_list) == 0:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,
                            detail= "Array is empty!")

    if len(media_id_list) == 1 and not await media_db.get_media_by_id(media_id= media_id_list[0]):
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= "This file doesn't exists!")
    
    files_deleted = []
    for media_id in media_id_list:
        if await media_db.delete_file(media_id= media_id):
            files_deleted.append(media_id)
    
    return {"success": not len(files_deleted) == 0, "deleted": files_deleted}