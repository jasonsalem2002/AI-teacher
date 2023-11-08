# process_pdf.py
import PyPDF2
import os

def extract_text_pdf(pdf_path):
    # Define subdirectories for text
    pdf_dir_name = os.path.splitext(os.path.basename(pdf_path))[0]
    text_dir = os.path.join(pdf_dir_name, "Texts")
    
    # Ensure directory exists
    os.makedirs(text_dir, exist_ok=True)
    
    # Initialize the PDF reader
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text_content = [page.extract_text() for page in reader.pages]
    
    # Save all text to a file
    text_filename = os.path.join(text_dir, "extracted_text.txt")
    with open(text_filename, 'w', encoding="utf-8") as f:
        f.write("\n\n".join(text_content))

    return pdf_dir_name

