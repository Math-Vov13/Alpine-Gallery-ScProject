# API
# Mathéo Vovard

from schemas.gallery import *
from typing import BinaryIO, Optional, AsyncGenerator
import base64           # Base64 (bits)
import os
import json

fakestorage_folder = os.path.dirname(__file__) + "\\storage"


def clear_storage_on_restart():
    if not os.path.exists(fakestorage_folder): os.mkdir(fakestorage_folder)
    
    i= 0
    e= 0
    for filename in os.listdir(fakestorage_folder):
        try:
            os.remove(os.path.join(fakestorage_folder, filename))
        except:
            e+=1
        else:
            i+=1
    print(f"Purged directory of {i} file(s) [{e} error(s) encountered]")


class media_json:

    async def __file_generator(path: str) -> AsyncGenerator:
        with open(path, "r") as f:
            while chunk := f.read(1024):  # Taille des chunks en octets
                yield base64.b64decode(chunk)

    def __get_path(filename: str) -> str:
        return os.path.join(fakestorage_folder, "_{}.txt".format(filename))

    async def create_json(media_id: int, contentObject= BinaryIO) -> bool:
        """
        Créer un nouveau json

        :param media_id: id du fichier
        :param content: contenu en binaire du fichier
        :return: l'opération a réussie ou non
        """
        with open(media_json.__get_path(str(media_id)), "w") as f:
            content: bytes = contentObject.read()                       # Récupère les bytes de l'image
            img_b64: str = base64.b64encode(content).decode("utf-8")    # Encode l'image en 64 bytes et la décode en utf8

            f.write(img_b64)
            #json.dump(img_b64, f)                                       # Ecrit dans le Json

        return True

    async def get_json(media_id: int) -> Optional[AsyncGenerator]:
        """
        Récupérer un json

        :param media_id: id du fichier
        :return: contenu du fichier
        """

        path = media_json.__get_path(str(media_id))
        if not os.path.exists(path) : return None
        try:
            return media_json.__file_generator(path)
        except Exception as e:
            print("erreur:", e)
            return

    async def delete_json(media_id: int) -> bool:
        """
        Supprime un json

        :param media_id: id du fichier
        :return: l'opération a réussie ou non
        """
        try:
            os.remove(media_json.__get_path(str(media_id)))
        except:
            return False
        return True


clear_storage_on_restart()