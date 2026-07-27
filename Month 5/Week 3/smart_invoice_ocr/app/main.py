from fastapi import FastAPI
from pathlib import Path
from .routes.invoice import router as invoice_router

app = FastAPI(
    title="Smart Invoice OCR API",
    version="1.0.0",
    description="Extract structured invoice data using OCR."
)

UPLOAD_DIR = Path("app/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

app.include_router(invoice_router)

@app.get("/")
def home():
    return {
        "message": "Smart Invoice OCR API is running."
    }