from dataclasses import dataclass

@dataclass(frozen= True)
class Config:
    DEV = True

    MAX_NAME_CHARS = 25
    MAX_FILE_SIZE = 100000


CONFIG = Config