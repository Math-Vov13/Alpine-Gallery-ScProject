# API
# Mathéo Vovard

from fastapi import UploadFile
from typing import Optional, AsyncGenerator
import os
import random, time

from src.schemas.gallery import *
from src.model.media_json import media_json
from src.Core.Config import CONFIG


fakedb : list[File_Schema] = []


class media_utils:

    @staticmethod
    async def generate_id() -> int:
        random.seed(time.time())
        return random.randint(10000, 999999)

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

        return str.replace(name, " ", "_")[:CONFIG.MAX_FILE_NAME_CHARS]

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
    def get_all_files():
        return [i.model_dump() for i in fakedb]

    @staticmethod
    async def get_media_by_id(media_id: int) -> Optional[File_Schema]:
        for i in fakedb:
            if i.id == media_id:
                return i
    

    @staticmethod
    async def get_files_by_id(account_id: int) -> list[File_Schema]:
        result = []
        for i in fakedb:
            if i.acc_id == account_id:
                result.append(i)
        return result




    @staticmethod
    async def save_file(account_id: int, name: Update_File_Schema, filedata: UploadFile) -> Optional[int]:
        """
        Sauvegarder un fichier dans le storage

        :param account_id: id du compte
        :param content: contenu du fichier (en bytes)
        :return: media_id
        """

        if len(await media_db.get_files_by_id(account_id= account_id)) >= CONFIG.MAX_IMAGE_PER_ACCOUNT:
            return

        # Ajoute le fichier dans la table
        newfile = File_Schema(
            id = await media_utils.generate_id(),
            acc_id= account_id,
            ext= name.ext,
            name= name.name,
            size= filedata.size,
            content_type= filedata.content_type
        )

        fakedb.append(newfile)
        await media_json.create_json(newfile.id, filedata.file)

        return newfile.id


    @staticmethod
    async def update_file(account_id: int, media_id: int, changes: Update_File_Schema) -> bool:
        """
        Modifier les informations d'un fichier

        :param account_id: id du compte
        :param media_id: id du fichier
        :param newName: nouveau nom du fichier
        :return: l'opération a réussie ou non
        """

        thisfile = await media_db.get_media_by_id(media_id= media_id)
        if not thisfile: return False
        if thisfile.acc_id != account_id: return False

        thisfile.name = changes.name if changes.name else thisfile.name
        thisfile.ext = changes.ext if changes.ext else thisfile.ext
        thisfile.content_type = f"image/{thisfile.ext[1:]}" if changes.ext else thisfile.content_type

        return True


    @staticmethod
    async def get_content(account_id: int, media_id: int) -> Optional[AsyncGenerator]:
        """
        Récupérer le contenu d'un fichier

        :param account_id: id du compte
        :param media_id: id du fichier
        :return: un générateur asynchrone ou rien
        """
        
        thisfile = await media_db.get_media_by_id(media_id= media_id)
        if not thisfile: return
        if thisfile.acc_id != account_id: return

        return await media_json.get_json(media_id)


    @staticmethod
    async def delete_file(account_id: int, media_id: int) -> bool:
        """
        Supprime un fichier du storage

        :param account_id: id du compte
        :param media_id: id du fichier
        :return: l'opération a réussie ou non
        """
        
        thisfile = await media_db.get_media_by_id(media_id= media_id)
        if not thisfile: return False
        if thisfile.acc_id != account_id: return False
        
        fakedb.remove(thisfile)
        await media_json.delete_json(thisfile.id)

        return True