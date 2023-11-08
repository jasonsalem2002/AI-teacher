# process_pptx.py
from pptx import Presentation
import pytesseract
from PIL import Image
import os

def extract_text_and_images_pptx(pptx_path):
    # Define subdirectories for text and images
    pptx_dir_name = os.path.splitext(os.path.basename(pptx_path))[0]
    text_dir = os.path.join(pptx_dir_name, "Texts")
    images_dir = os.path.join(pptx_dir_name, "Images")
    
    # Ensure directories exist
    os.makedirs(text_dir, exist_ok=True)
    os.makedirs(images_dir, exist_ok=True)
    
    # Initialize the PowerPoint presentation
    prs = Presentation(pptx_path)
    text_content = []
    
    for slide_number, slide in enumerate(prs.slides, start=1):
        # Extract text from each slide
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                text_content.append(shape.text)
        
        # Save images from each slide
        for shape in slide.shapes:
            if shape.shape_type == 13:  # This is the type number for Picture
                image = shape.image
                image_bytes = image.blob
                image_filename = f"image_slide_{slide_number}.jpeg"
                image_path = os.path.join(images_dir, image_filename)
                with open(image_path, 'wb') as f:
                    f.write(image_bytes)
    
    # Save all text to a file
    text_filename = os.path.join(text_dir, "extracted_text.txt")
    with open(text_filename, 'w', encoding="utf-8") as f:
        f.write("\n\n".join(text_content))

    return pptx_dir_name

