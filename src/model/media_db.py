# API
# Mathéo Vovard

from fastapi import UploadFile
from schemas.gallery import *
from model.media_json import media_json

fakedb = []



class media_db:

    @staticmethod
    async def get_media_by_id(media_id: int) -> file:
        for i in fakedb:
            if i.id == media_id:
                return i
    
    @staticmethod
    async def get_all_files() -> list[file]:
        return fakedb


    @staticmethod
    async def save_file(filedata: UploadFile) -> int:
        """
        Sauvegarder un fichier dans le storage

        :param content: contenu du fichier (en bytes)
        :return: media_id
        """

        # Ajoute le fichier dans la table
        newfile = file(
            id = len(fakedb) + 1,
            name= filedata.filename,
            size= filedata.size,
            content_type= filedata.content_type
        )

        fakedb.append(newfile)
        await media_json.create_json(newfile.id, filedata.file)

        return newfile.id

    @staticmethod
    async def update_file(media_id: int, newName: str) -> bool:
        """
        Modifier les informations d'un fichier

        :param media_id: id du fichier
        :param newName: nouveau nom du fichier
        :return: l'opération a réussie ou non
        """

        thisfile = await media_db.get_media_by_id(media_id= media_id)
        thisfile.name = newName

        return True

    @staticmethod
    async def get_path(media_id: str) -> str:
        """
        Récupérer le chemin du fichier

        :param media_id: id du fichier
        :return: chemin du fichier
        """

        thisfile = await media_db.get_media_by_id(media_id= media_id)
        if not thisfile: return False

        return thisfile

    @staticmethod
    async def delete_file(media_id: str) -> bool:
        """
        Supprime un fichier du storage

        :return: l'opération a réussie ou non
        """
        
        thisfile = await media_db.get_media_by_id(media_id= media_id)
        if not thisfile: return False
        
        fakedb.remove(thisfile)
        await media_json.delete_json(thisfile.id)

        return True