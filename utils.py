import re

def extract_fields(text):
    fields = {
        "invoice_number": re.search(r"Invoice\s*#?:?\s*(\d+)", text),
        "invoice_date": re.search(r"Date\s*:?[\s]*(\d{2}/\d{2}/\d{4})", text),
        "due_date": re.search(r"Due Date\s*:?[\s]*(\d{2}/\d{2}/\d{4})", text),
        "total": re.search(r"Total\s*Amount\s*:?[\s$]*([\d,]+\.\d{2})", text),
        "vendor": re.search(r"Bill\s*From\s*:?[\s]*(.*)", text),
    }

    cleaned = {k: (v.group(1).strip() if v else None) for k, v in fields.items()}
    return cleaned
