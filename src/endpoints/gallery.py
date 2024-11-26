from fastapi import APIRouter, HTTPException, status, Query, Depends
from fastapi import UploadFile, File
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse

from typing import Annotated, Optional, Literal

from Core.Config import CONFIG
from model.media_db import media_db, media_utils
from schemas.gallery import *
from endpoints.middlewares.auth import get_current_username


router = APIRouter(prefix= "/gallery", tags=["Gallery"])



@router.get("/",
            description= "Get the list of all medias files")
async def get_all_files(account: Annotated[str, Depends(get_current_username)], start: Annotated[int, Query()]= 1, step: Annotated[int, Query()]= 50):
    start -= 1 # retire 1 à start pour le début de la liste en python (commence par 0)

    STEP_LIST = [10, 25, 50, 100]

    if start < 0 or start%5 > 0 or not (step in STEP_LIST):
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,
                            detail= "start query can't be negative number!")
    
    result = await media_db.get_files_by_id(account_id= account["id"])
    result = result[start : start+step]

    return {"length": len(result), "contents": result}
    


@router.get("/{media_id}:{operation}",
            description= "Get a list of medias files")
async def upload_file(account: Annotated[str, Depends(get_current_username)], media_id: int, operation: Literal["read", "upload"]):
    thisfile = await media_db.get_media_by_id(media_id= media_id)
    if not thisfile:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= "This file doesn't exists!",
                            headers= {"media_id": str(media_id)})
    
    str_generator = await media_db.get_content(account_id= account["id"], media_id= media_id)
    if not str_generator:
        raise HTTPException(status_code=500,
                            detail= "An unexpected error has occurred while streaming a file!")

    response_headers = {}
    if operation == "upload":
        response_headers = {
            "Content-Disposition": f"attachment; filename=FastAPI-{thisfile.name + thisfile.ext}"
            }


    return StreamingResponse(
        content= str_generator,
        status_code= 200,
        media_type= thisfile.content_type,
        headers= response_headers
    )



@router.post("/",
             description= "Upload medias files")
async def download_files(account: Annotated[str, Depends(get_current_username)], files: Annotated[list[UploadFile] | None, File(description="A file read as UploadFile")]):
    if not files:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail= "Array is empty!")

    data_list = []
    
    for file in files:

        print(file.size)
        if file.size > CONFIG.MAX_FILE_SIZE:
            continue  # Le fichier est trop gros !

        # vérifie la validité du nom du fichier
        name, ext = media_utils.separate_path_and_ext(file.filename)
        if not name or not ext:
            continue # Erreur dans le nom !
        name = media_utils.get_name_accepted(name)
        if not name:
            continue # Le nom n'est pas accepté !
        ext = media_utils.get_ext_enum(ext)
        if not ext:
            continue # L'extension n'est pas acceptée !

        print("Enum :", repr(ext))
        new_media_id = await media_db.save_file(account["id"], Update_File_Schema(name= name, ext= ext), file)
        data_list.append(await media_db.get_media_by_id(new_media_id))

    # les fichiers qui ne sont pas dans le bon format ont été oublié (ils ne seront pas renvoyés dans la réponse)
    return {"length": len(data_list),
            "elements" : dict([(file.name, file.model_dump()) for file in data_list])}



@router.put("/{media_id}", status_code= status.HTTP_200_OK,
            description= "Upload files metadatas")
async def update_file(account: Annotated[str, Depends(get_current_username)], media_id: int, fullname: str):
    # Géré par FastAPI
    # if not fullname:
    #     raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,
    #                         detail= "At least one query parameter must be not empty!")

    if not await media_db.get_media_by_id(media_id= media_id):
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= "This file doesn't exists!",
                            headers= {"media_id": str(media_id)})


    new_name, new_extension = media_utils.separate_path_and_ext(fullpath= fullname)

    new_name = media_utils.get_name_accepted(name= new_name)
    if not new_name:
        raise HTTPException(status_code= status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                            detail= f"['{fullname}'] is not supported!")

    new_extension = media_utils.get_ext_enum(ext= new_extension)
    if not new_extension:
        raise HTTPException(status_code= status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                            detail= f"['{fullname}'] is not supported!")


    if not await media_db.update_file(account_id= account["id"], media_id= media_id, changes= Update_File_Schema(
        media_id= media_id,
        name= new_name,
        ext= new_extension
    )):
        return {"success": False, "message": "Operation failed!"}
    
    return {"success": True, "message": "Changed successfully"}



@router.delete("/{media_id}",
               description= "Delete all files")
async def delete_files(account: Annotated[str, Depends(get_current_username)], media_id: int = 0):
    if not await media_db.delete_file(account_id= account["id"], media_id= media_id):
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= "This file doesn't exists!")
    
    return {"success": True, "message": "deleted successfully!"}