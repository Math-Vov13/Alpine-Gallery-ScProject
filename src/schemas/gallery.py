# API
# Mathéo Vovard

from pydantic import BaseModel
from enum import StrEnum

class FileExtension_Enum(StrEnum):
    PNG = ".png"    # Portable Network Graphics
    JPG = ".jpg"    # Joint Photographic Group
    JPEG = ".jpeg"  # Joint Photographic Experts Group
    TIFF = ".tiff"  # Tagged Image File Format
    PSD = ".psd"    # Photoshop Document
    AI = ".ai"      # Adobe Illustrator Document
    INDD = ".indd"  # Adobe Indesign Document
    SVG = ".svg"    # Scalable Vector Graphics
    BMP = ".bmp"    # Bitmap
    WEBP = ".webp"  # WebP (Google)


class File_Schema(BaseModel):
    id : int                    # id
    acc_id: int                 # account id
    ext: FileExtension_Enum     # file extension
    name: str                   # file name
    size: int                   # file size (bytes)
    content_type: str           # request content_type

class Update_File_Schema(BaseModel):
    name: str                   # file name
    ext: FileExtension_Enum     # file extension

class Json_File_Schema(BaseModel):
    content: bytes              # File content (in bytes)