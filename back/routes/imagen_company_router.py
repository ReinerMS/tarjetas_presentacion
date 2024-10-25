from fastapi import APIRouter, UploadFile, File
from services.imgen_company_service import save_image

router = APIRouter()

@router.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    message = await save_image(file)
    return {"message": message}