# process_docx.py
from docx import Document
import os

def extract_text_docx(docx_path):
    # Define subdirectories for text
    docx_dir_name = os.path.splitext(os.path.basename(docx_path))[0]
    text_dir = os.path.join(docx_dir_name, "Texts")
    
    # Ensure directory exists
    os.makedirs(text_dir, exist_ok=True)
    
    # Initialize the Document
    doc = Document(docx_path)
    text_content = [para.text for para in doc.paragraphs]
    
    # Save all text to a file
    text_filename = os.path.join(text_dir, "extracted_text.txt")
    with open(text_filename, 'w', encoding="utf-8") as f:
        f.write("\n\n".join(text_content))

    return docx_dir_name

