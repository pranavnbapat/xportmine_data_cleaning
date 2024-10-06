from fastapi import APIRouter, File, UploadFile, HTTPException
from app.services.file_service import process_excel_file
from app.utils.file_utils import save_file, delete_file
import os

router = APIRouter()

UPLOAD_DIR = "./uploaded_files"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Save the uploaded file
        file_location = save_file(file, UPLOAD_DIR)

        # Process the Excel file
        data = process_excel_file(file_location)
        print(data.head())

        # Clean up file after processing
        delete_file(file_location)

        return {"status": "success", "filename": file.filename}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing file: {str(e)}")


@router.get("/process_file/")
def process_file(file_path: str):
    try:
        if not os.path.exists(file_path):
            return {"error": "File not found"}, 404

        data = process_excel_file(file_path)
        print(data.head())

        return {"status": "success", "message": f"Processed file: {file_path}"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing file: {str(e)}")
