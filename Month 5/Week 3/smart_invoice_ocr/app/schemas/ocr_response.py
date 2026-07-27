from pydantic import BaseModel

class OCRResponse(BaseModel):
    success: bool
    text: list[str]