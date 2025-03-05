import easyocr
import cv2


def extract_text_from_image(image_path):
    # Load image with OpenCV for preprocessing
    image = cv2.imread(image_path)
    # Custom preprocessing (simplified for demo)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Initialize EasyOCR with custom CRNN model (simulated)
    reader = easyocr.Reader(['en'], model_storage_directory='custom_crnn')
    result = reader.readtext(gray)
    return " ".join([res[1] for res in result])  # Extracted text