# main.py
import os
import sys
import process_pptx
import process_pdf
import process_docx

def main():
    # Gather file paths from command line arguments
    files_to_process = sys.argv[1:]

    for file_path in files_to_process:
        # Determine file type and call the appropriate function
        if file_path.endswith('.pptx'):
            process_pptx.extract_text_and_images_pptx(file_path)
        elif file_path.endswith('.pdf'):
            process_pdf.extract_text_pdf(file_path)
        elif file_path.endswith('.docx'):
            process_docx.extract_text_docx(file_path)
        else:
            print(f"File format of {file_path} is not supported.")

if __name__ == "__main__":
    main()

