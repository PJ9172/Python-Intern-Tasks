import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

UPLOAD_DIR = Path("app/uploads")

def save_image(file: UploadFile) -> str:
    extension = Path(file.filename).suffix.lower()

    filename = f"{uuid4()}{extension}"

    file_path = UPLOAD_DIR / filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return filename


ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}

def validate_image(file: UploadFile):
    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError(
            "Only JPG, JPEG and PNG images are allowed."
        )