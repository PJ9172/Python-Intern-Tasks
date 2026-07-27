from pathlib import Path
import easyocr

# Load model once when application starts
reader = easyocr.Reader(
    ['en'],
    gpu=False
)


def extract_text(image_path: Path):
    """
    Extract text using EasyOCR
    """

    result = reader.readtext(str(image_path))

    extracted = []

    for bbox, text, confidence in result:
        extracted.append({
            "text" : text,
            "confidence" : confidence,
            "bbox" : bbox
        })


    return extracted