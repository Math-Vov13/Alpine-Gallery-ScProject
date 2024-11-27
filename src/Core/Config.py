from dataclasses import dataclass

@dataclass(frozen= True)
class Config:
    PROD = True
    PublicUrl = "https://alpine-gallery-dd79325dcd85.herokuapp.com"
    DevUrl = "http://127.0.0.1:8000"

    MAX_ACCOUNT_NAME_CHARS = 35
    MAX_ACCOUNT_EMAIL_CHARS = 50
    MAX_ACCOUNT_PASSWORD_CHARS = 50
    MAX_FILE_NAME_CHARS = 40
    MAX_FILE_SIZE = 5000000

    MAX_IMAGE_PER_ACCOUNT = 15
    MAX_ACCOUNT = 5 # LIMIT DATA BECAUSE I HAVE A FREE ACCOUNT...

    def get_BASE_URL() -> str:
        return Config.PublicUrl if Config.PROD else Config.DevUrl


CONFIG = Config