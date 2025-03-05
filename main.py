from utils.scraper import scrape_website
from utils.ocr import extract_text_from_image
from utils.transcription import transcribe_audio
from utils.analysis import analyze_and_visualize

def run_automation():
    # Scrape data from a sample website
    url = "https://example.com"
    scraped_data = scrape_website(url)
    print("Scraped Data:", scraped_data)

    # Extract text from a sample image
    image_path = "data/sample_image.png"
    ocr_text = extract_text_from_image(image_path)
    print("OCR Extracted Text:", ocr_text)

    # Transcribe a sample audio file
    audio_path = "data/sample_audio.wav"
    transcribed_text = transcribe_audio(audio_path)
    print("Transcribed Text:", transcribed_text)

    # Analyze and visualize extracted data
    analyze_and_visualize(scraped_data, ocr_text, transcribed_text)

if __name__ == "__main__":
    run_automation()