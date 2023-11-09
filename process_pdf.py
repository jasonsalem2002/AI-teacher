# process_pdf.py
import PyPDF2
import os
from utils import setup_directories
import logging

def extract_text_pdf(pdf_path):
    try:
        base_dir = "output"
        pdf_dir_name = os.path.splitext(os.path.basename(pdf_path))[0]
        pdf_base_dir = os.path.join(base_dir, pdf_dir_name)
        directories = setup_directories(pdf_base_dir, ["Texts"])

        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text_content = [page.extract_text() for page in reader.pages if page.extract_text().strip() != '']

        text_filename = os.path.join(directories["Texts"], "extracted_text.txt")
        with open(text_filename, 'w', encoding="utf-8") as f:
            f.write("\n\n".join(text_content))

        logging.info(f"Processed {pdf_path} successfully.")

    except Exception as e:
        logging.error(f"Error processing {pdf_path}: {e}")
