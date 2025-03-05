from seleniumbase import SB
from bs4 import BeautifulSoup
import pyautogui

def scrape_website(url):
    scraped_data = {}
    with SB(uc=True, headless=True) as driver:
        driver.open(url)
        pyautogui.hotkey('ctrl', 's')  # Simulate saving page
        html = driver.get_page_source()
        soup = BeautifulSoup(html, 'html.parser')
        scraped_data['title'] = soup.title.text if soup.title else "No Title"
        scraped_data['links'] = [a['href'] for a in soup.find_all('a', href=True)]
    return scraped_data