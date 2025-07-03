import re
from datetime import datetime

# Map German months to numbers for parsing date like "1. März 2024"
GERMAN_MONTHS = {
    'Januar': '01',
    'Februar': '02',
    'März': '03',
    'April': '04',
    'Mai': '05',
    'Juni': '06',
    'Juli': '07',
    'August': '08',
    'September': '09',
    'Oktober': '10',
    'November': '11',
    'Dezember': '12'
}

def parse_german_date(date_str):
    try:
        # Example input: "1. März 2024"
        parts = date_str.strip().split()
        day = parts[0].replace('.', '')
        month_name = parts[1]
        year = parts[2]
        month = GERMAN_MONTHS.get(month_name, '01')
        formatted_date = f"{year}-{month}-{day.zfill(2)}"  # ISO format yyyy-mm-dd
        return formatted_date
    except Exception:
        return date_str  # fallback, original string

def extract_invoice_data(text):
    invoice_data = {}

    # Invoice Number: look for 'Invoice No' followed by number on next line or same line
    inv_no_match = re.search(r'Invoice\s*No\.?\s*\n?\s*(\S+)', text, re.IGNORECASE)
    invoice_data['Invoice Number'] = inv_no_match.group(1).strip() if inv_no_match else 'Not Found'

    # Date: after "Date" keyword, parse German date format
    date_match = re.search(r'Date\s*\n?\s*([\d\.]+\s+[A-Za-zäöüÄÖÜ]+\s+\d{4})', text, re.IGNORECASE)
    if date_match:
        invoice_data['Date'] = parse_german_date(date_match.group(1))
    else:
        invoice_data['Date'] = 'Not Found'

    # Vendor: Not available in snippet, fallback to Not Found
    invoice_data['Vendor'] = 'Not Found'

    # Total Amount: try to find last amount in format "number,number €"
    amounts = re.findall(r'(\d{1,3}(?:\.\d{3})*,\d{2})\s*€', text)
    if amounts:
        # Take last amount as total (common in invoices)
        total_amount = amounts[-1].replace('.', '').replace(',', '.')
        invoice_data['Total Amount'] = total_amount
    else:
        invoice_data['Total Amount'] = 'Not Found'

    return invoice_data

