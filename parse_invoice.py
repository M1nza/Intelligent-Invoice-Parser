import pdfplumber
import json
from utils import extract_fields

def parse_invoice(pdf_path, output_json):
    full_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            full_text += page.extract_text() + "\n"

    data = extract_fields(full_text)

    with open(output_json, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Extracted data saved to {output_json}")

if __name__ == "__main__":
    parse_invoice("sample_invoice.pdf", "cleaned_invoice.json")
