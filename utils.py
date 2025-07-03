import re

def extract_invoice_data(text):
    invoice_data = {
        'Invoice Number': re.search(r'Invoice\s*#?:?\s*(\S+)', text, re.IGNORECASE),
        'Date': re.search(r'Date\s*:? (\d{1,2}[/-]\d{1,2}[/-]\d{2,4})', text, re.IGNORECASE),
        'Vendor': re.search(r'(From|Billed\s*By):\s*(.+)', text, re.IGNORECASE),
        'Total Amount': re.search(r'Total\s*Amount\s*:? \$?(\d+[.,]?\d{0,2})', text, re.IGNORECASE),
    }

    cleaned = {}
    for field, match in invoice_data.items():
        if match:
            cleaned[field] = match.group(1) if field != 'Vendor' else match.group(2)
        else:
            cleaned[field] = 'Not Found'
    return cleaned
