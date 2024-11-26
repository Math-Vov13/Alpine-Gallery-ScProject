from dataclasses import dataclass

@dataclass(frozen= True)
class Config:
    DEV = True
    PublicUrl = "https://alpine-gallery-dd79325dcd85.herokuapp.com"
    DevUrl = "http://127.0.0.1:8000"

    MAX_NAME_CHARS = 25
    MAX_FILE_SIZE = 100000

    def get_BASE_URL() -> str:
        return Config.DevUrl if Config.DEV else Config.PublicUrl


CONFIG = Config