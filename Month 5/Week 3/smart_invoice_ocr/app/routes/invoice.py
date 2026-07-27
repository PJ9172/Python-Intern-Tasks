from fastapi import APIRouter, File, UploadFile, HTTPException

from app.services import upload_service, parser, ocr_service

from ..schemas.upload_response import UploadResponse
from ..schemas.ocr_response import OCRResponse
from pathlib import Path

router = APIRouter(
    prefix="/invoice",
    tags=["Invoice OCR"]
)


@router.get("/")
def test_route():
    return {
        "message": "Invoice route working."
    }

@router.post("/upload", response_model=UploadResponse)
def upload_invoice(
    file: UploadFile = File(...),
):
    try:
        upload_service.validate_image(file)

        filename = upload_service.save_image(file)

        return UploadResponse(
            success=True,
            message="Invoice uploaded successfully.",
            filename=filename,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.post(
    "/extract"
)
def extract_invoice(
    file: UploadFile = File(...)
):
    upload_service.validate_image(file)

    filename = upload_service.save_image(file)

    image_path = Path("app/uploads") / filename

    text = ocr_service.extract_text(image_path)

    invoice = parser.parse_invoice(text)

    return {
        "success": True,
        "text": invoice
    }