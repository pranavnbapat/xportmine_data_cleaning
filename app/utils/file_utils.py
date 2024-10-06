import shutil
import os
from fastapi import UploadFile


def save_file(file: UploadFile, upload_dir: str):
    file_location = f"{upload_dir}/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return file_location


def delete_file(file_path: str):
    if os.path.exists(file_path):
        os.remove(file_path)
