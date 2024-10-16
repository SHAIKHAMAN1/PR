from PIL import Image
import pytesseract

# Path to the Tesseract executable (use the correct path on your system)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Path to the input image
input_image_path = r"C:\Users\amaan\OneDrive\Desktop\img.jpg"  # Update as necessary
output_text = ''

# Open the image using Pillow
try:
    image = Image.open(input_image_path)
except Exception as e:
    print(f"Error loading image: {str(e)}")
    exit()

# Perform OCR on the image
try:
    output_text = pytesseract.image_to_string(image)
except Exception as e:
    print(f"Error during OCR: {str(e)}")

# Print the recognized text
print("Recognized Text:")
print(output_text)
