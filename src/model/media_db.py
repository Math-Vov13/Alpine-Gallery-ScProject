# API
# Mathéo Vovard


async def save_file(content: bytes) -> str:
    """
    Sauvegarder un fichier dans le storage

    :param content: contenu du fichier (en bytes)
    :return: media_id
    """
    pass

async def update_file(media_id: str, newName: str) -> bool:
    """
    Modifier les informations d'un fichier

    :param media_id: id du fichier
    :param newName: nouveau nom du fichier
    :return: l'opération a réussie ou non
    """
    pass

async def get_path(media_id: str) -> str:
    """
    Récupérer le chemin du fichier

    :param media_id: id du fichier
    :return: chemin du fichier
    """
    pass

async def delete_file(media_id: str) -> bool:
    """
    Supprime un fichier du storage

    :return: l'opération a réussie ou non
    """
    pass