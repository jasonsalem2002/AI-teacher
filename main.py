# main.py
import os
import logging
import process_pptx
import process_pdf
import process_docx

# Configure logging
logging.basicConfig(filename='processing.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the directory containing the files to process
files_directory = "files_to_process"

# Automatically discover files in the directory
def discover_files(directory):
    for entry in os.scandir(directory):
        if entry.is_file():
            yield entry.path

def main():
    for file_path in discover_files(files_directory):
        # Determine file type and call the appropriate function
        if file_path.endswith('.pptx'):
            process_pptx.extract_text_and_images_pptx(file_path)
        elif file_path.endswith('.pdf'):
            process_pdf.extract_text_pdf(file_path)
        elif file_path.endswith('.docx'):
            process_docx.extract_text_docx(file_path)
        else:
            logging.warning(f"File format of {file_path} is not supported.")

if __name__ == "__main__":
    main()
