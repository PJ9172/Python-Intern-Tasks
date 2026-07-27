import re
from typing import Dict, List


def clean_text(text: str) -> str:
    """Clean extracted OCR text."""
    text = text.replace("|", "I")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n+", "\n", text)
    return text.strip()


def get_text(ocr_result: List[Dict]) -> str:
    """
    Convert OCR result to plain text.
    OCR result format:
    [
        {
            "text": "...",
            "confidence": 0.99,
            "bbox": [...]
        }
    ]
    """
    return "\n".join(item["text"] for item in ocr_result)


def extract_invoice_number(text: str):
    patterns = [
        r"Invoice\s*no[:\s]*([A-Za-z0-9\-]+)",
        r"Invoice\s*Number[:\s]*([A-Za-z0-9\-]+)",
        r"Invoice[:\s]*([A-Za-z0-9\-]+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.I)
        if match:
            return match.group(1).strip()

    return None


def extract_invoice_date(text: str):
    patterns = [
        r"Date\s*of\s*issue[:\s]*([\d/\-.]+)",
        r"Invoice\s*Date[:\s]*([\d/\-.]+)",
        r"Date[:\s]*([\d/\-.]+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.I)
        if match:
            return match.group(1).strip()

    return None


def extract_seller(text: str):
    match = re.search(
        r"Seller:(.*?)Client:",
        text,
        re.S | re.I,
    )

    if not match:
        return {
            "name": None,
            "address": None,
        }

    block = match.group(1)

    lines = [
        line.strip()
        for line in block.split("\n")
        if line.strip()
    ]

    # Remove unwanted lines
    lines = [
        line
        for line in lines
        if not line.startswith("Tax Id")
        and not line.startswith("IBAN")
    ]

    if not lines:
        return {
            "name": None,
            "address": None,
        }

    name = lines[0]

    address = ", ".join(lines[1:]) if len(lines) > 1 else None

    return {
        "name": name,
        "address": address,
    }


def extract_client(text: str):
    match = re.search(
        r"Client:(.*?)ITEMS",
        text,
        re.S | re.I,
    )

    if not match:
        return {
            "name": None,
            "address": None,
        }

    block = match.group(1)

    lines = [
        line.strip()
        for line in block.split("\n")
        if line.strip()
    ]

    lines = [
        line
        for line in lines
        if not line.startswith("Tax Id")
    ]

    if not lines:
        return {
            "name": None,
            "address": None,
        }

    name = lines[0]

    address = ", ".join(lines[1:]) if len(lines) > 1 else None

    return {
        "name": name,
        "address": address,
    }


def extract_tax_ids(text: str):
    tax_ids = re.findall(
        r"Tax\s*Id[:\s]*([\d\-]+)",
        text,
        re.I,
    )

    seller_tax = tax_ids[0] if len(tax_ids) > 0 else None
    client_tax = tax_ids[1] if len(tax_ids) > 1 else None

    return seller_tax, client_tax


def extract_iban(text: str):
    match = re.search(
        r"IBAN[:\s]*([A-Z0-9]+)",
        text,
        re.I,
    )

    return match.group(1) if match else None


def extract_total_amount(text: str):
    """
    Returns the last currency amount in SUMMARY.
    """

    amounts = re.findall(
        r"\$\s*([\d\s,\.]+)",
        text,
    )

    if not amounts:
        return None

    total = amounts[-1]

    total = total.replace(" ", "")

    return total


def parse_invoice(ocr_result: List[Dict]):

    text = clean_text(get_text(ocr_result))

    seller_tax, client_tax = extract_tax_ids(text)

    return {
        "invoice_number": extract_invoice_number(text),
        "invoice_date": extract_invoice_date(text),

        "seller": extract_seller(text),

        "seller_tax_id": seller_tax,

        "iban": extract_iban(text),

        "client": extract_client(text),

        "client_tax_id": client_tax,

        "total_amount": extract_total_amount(text),

        "raw_text": text,
    }