import re

def extract_invoice_data(text):
    invoice_data = {
        'Invoice Number': re.search(r'(Invoice\s*(No\.?|Number)?|#)\s*[:\-]?\s*(\w+)', text, re.IGNORECASE),
        'Date': re.search(r'(Invoice\s*Date|Date)\s*[:\-]?\s*([0-9]{1,2}[/-][0-9]{1,2}[/-][0-9]{2,4})', text, re.IGNORECASE),
        'Vendor': re.search(r'(From|Billed\s*By|Supplier)\s*[:\-]?\s*(.*)', text, re.IGNORECASE),
        'Total Amount': re.search(r'(Total\s*(Amount)?|Amount\s*Due)\s*[:\-]?\s*\$?\s*([0-9]+[.,]?[0-9]{0,2})', text, re.IGNORECASE)
    }

    cleaned = {}
    for field, match in invoice_data.items():
        if match:
            # Use the last group matched (most specific one)
            cleaned[field] = match.groups()[-1].strip()
        else:
            cleaned[field] = 'Not Found'
    return cleaned
