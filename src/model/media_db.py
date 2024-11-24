# API
# Mathéo Vovard

from fastapi import UploadFile
from schemas.gallery import *
from model.media_json import media_json

from typing import Optional, AsyncGenerator
import os

fakedb : list[File_Schema] = []


class media_utils:

    @staticmethod
    def separate_path_and_ext(fullpath: str) -> tuple[str, str]:
        """
        Sépare le nom du fichier de son extension dans un t-uplet

        :param fullpath: nom entier du fichier (chemin + extension)
        :return: un t-uplet avec le nom du fichier en premier et son extension en deuxième
        """

        path, name = os.path.split(fullpath) # s'assurer que le chemin du fichier n'est pas compris dans le nom
        return os.path.splitext(name)

    @staticmethod
    def get_name_accepted(name: str) -> str:
        """
        Donne un nom de fichier valide

        :param name: nom du fichier
        :return: `nom` du fichier
        """

        MAX_NAME_LENGTH = 25
        
        return str.replace(name, " ", "_")[:MAX_NAME_LENGTH]

    @staticmethod
    def get_ext_enum(ext: str) -> Optional[FileExtension_Enum]:
        """
        Donne une extension de fichier valide

        :param ext: extension du fichier
        :return: `extension` du fichier en enum ou `None`
        """
        try:
            return FileExtension_Enum(str.lower(ext))
        except:
            return

class media_db:

    @staticmethod
    async def get_media_by_id(media_id: int) -> Optional[File_Schema]:
        for i in fakedb:
            if i.id == media_id:
                return i
    
    @staticmethod
    async def get_all_files() -> list[File_Schema]:
        return fakedb


    @staticmethod
    async def save_file(name: Update_File_Schema, filedata: UploadFile) -> Optional[int]:
        """
        Sauvegarder un fichier dans le storage

        :param content: contenu du fichier (en bytes)
        :return: media_id
        """

        # Ajoute le fichier dans la table
        newfile = File_Schema(
            id = len(fakedb) + 1,
            ext= name.ext,
            name= name.name,
            size= filedata.size,
            content_type= filedata.content_type
        )

        fakedb.append(newfile)
        await media_json.create_json(newfile.id, filedata.file)

        return newfile.id

    @staticmethod
    async def update_file(media_id: int, changes: Update_File_Schema) -> bool:
        """
        Modifier les informations d'un fichier

        :param media_id: id du fichier
        :param newName: nouveau nom du fichier
        :return: l'opération a réussie ou non
        """

        thisfile = await media_db.get_media_by_id(media_id= media_id)
        thisfile.name = changes.name if changes.name else thisfile.name
        thisfile.ext = changes.ext if changes.ext else thisfile.ext
        thisfile.content_type = f"image/{thisfile.ext[1:]}" if changes.ext else thisfile.content_type

        return True
    
    @staticmethod
    async def get_content(media_id: str) -> Optional[AsyncGenerator]:
        thisfile = await media_db.get_media_by_id(media_id= media_id)
        if not thisfile: return False

        return await media_json.get_json(media_id)

    # @staticmethod
    # async def get_path(media_id: str) -> Optional[str]:
    #     """
    #     Récupérer le chemin du fichier

    #     :param media_id: id du fichier
    #     :return: chemin du fichier
    #     """

    #     thisfile = await media_db.get_media_by_id(media_id= media_id)
    #     if not thisfile: return False

    #     return thisfile

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