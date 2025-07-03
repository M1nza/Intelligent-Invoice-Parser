import streamlit as st
import fitz  # PyMuPDF
import tempfile
from utils import extract_invoice_data

st.set_page_config(page_title="Intelligent Invoice Parser", layout="centered")
st.title("Intelligent Invoice Parser")

uploaded_file = st.file_uploader("Upload an Invoice PDF", type="pdf")

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    doc = fitz.open(tmp_path)
    text = ""
    for page in doc:
        text += page.get_text()

    extracted_data = extract_invoice_data(text)

    st.subheader("Extracted Fields")
    st.json(extracted_data)
