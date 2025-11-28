from PIL import Image
import pytesseract

# Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_and_print(file_path, language='spa'): #to see what languages are available: pytesseract.get_languages()
    """
    Extract text from image or PDF and print it
    """
    file_path = file_path.lower()
    
    if file_path.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
        # It's an image
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image, lang=language)
        print(text)
        
    elif file_path.endswith('.pdf'):
        # It's a PDF - need pdf2image
        try:
            import pdf2image
            images = pdf2image.convert_from_path(file_path)
            
            for i, image in enumerate(images):
                text = pytesseract.image_to_string(image, lang=language)
                print(f"\n--- Page {i+1} ---")
                print(text)
                
        except ImportError:
            print("Please install pdf2image: pip install pdf2image")
        except Exception as e:
            print(f"Error processing PDF: {e}")
    else:
        print("Unsupported file format")
