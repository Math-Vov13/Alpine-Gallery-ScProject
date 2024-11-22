# API
# Mathéo Vovard

from schemas.gallery import *
from typing import BinaryIO

fakejson_path = "./media_storage.json"



class media_json:

    async def create_json(media_id: int, content= BinaryIO) -> bool:
        """
        Créer un nouveau json

        :param media_id: id du fichier
        :param content: contenu en binaire du fichier
        :return: l'opération a réussie ou non
        """
        pass

    async def get_json(media_id: int) -> file_json:
        """
        Récupérer un json

        :param media_id: id du fichier
        :return: contenu du fichier
        """
        pass

    async def delete_json(media_id: int) -> bool:
        """
        Supprime un json

        :param media_id: id du fichier
        :return: l'opération a réussie ou non
        """
        pass