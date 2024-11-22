# API
# Mathéo Vovard

from pydantic import BaseModel
from enum import StrEnum

class FileExtension_Enum(StrEnum):
    PNG = ".png"    # Portable Network Graphics
    JPG = ".jpg"    # Joint Photographic Group
    JPEG = ".jpeg"  # Joint Photographic Experts Group
    TIFF = ".tiff"  # Tagged Image File
    PSD = ".psd"    # Photoshop Document
    AI = ".ai"      # Adobe Illustrator Document
    INDD = ".indd"  # Adobe Indesign Document
    SVG = ".svg"    # Scalable Vector Graphics
    BMP = ".bmp"    # Bitmap
    WEBP = ".webp"  # WebP (Google)


class File_Schema(BaseModel):
    id : int
    ext: FileExtension_Enum
    name: str
    size: int
    content_type: str

class Update_File_Schema(BaseModel):
    name: str
    ext: FileExtension_Enum

class Json_File_Schema(BaseModel):
    content: bytes