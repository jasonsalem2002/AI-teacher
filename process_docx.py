# process_docx.py
from docx import Document
import os
from utils import setup_directories
import logging

def extract_text_docx(docx_path):
    try:
        base_dir = "output"
        docx_dir_name = os.path.splitext(os.path.basename(docx_path))[0]
        docx_base_dir = os.path.join(base_dir, docx_dir_name)
        directories = setup_directories(docx_base_dir, ["Texts"])

        doc = Document(docx_path)
        text_content = [para.text for para in doc.paragraphs if para.text.strip() != '']

        text_filename = os.path.join(directories["Texts"], "extracted_text.txt")
        with open(text_filename, 'w', encoding="utf-8") as f:
            f.write("\n\n".join(text_content))

        logging.info(f"Processed {docx_path} successfully.")

    except Exception as e:
        logging.error(f"Error processing {docx_path}: {e}")
