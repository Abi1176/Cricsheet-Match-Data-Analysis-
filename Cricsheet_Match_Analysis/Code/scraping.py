import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm

# Setup Selenium
options = Options()
options.add_argument("--headless")  # Run in headless mode
service = Service("D:\\MyFolderFiles\\chromedriver-win64\\chromedriver.exe")  # Update with correct path
driver = webdriver.Chrome(service=service, options=options)

# Navigate to Cricsheet match page
url = "https://cricsheet.org/matches/"
driver.get(url)
time.sleep(5)  # Allow page to load

# Find all match links
match_links = driver.find_elements(By.CSS_SELECTOR, "a[href$='.json']")

# Create directory for storing JSON files
os.makedirs("Data/match_data", exist_ok=True)

# Download JSON files
for link in tqdm(match_links, desc="Downloading JSON files"):
    file_url = link.get_attribute("href")
    file_name = file_url.split("/")[-1]
    file_path = os.path.join("Data/match_data", file_name)

    # Download file
    response = requests.get(file_url)
    with open(file_path, "wb") as f:
        f.write(response.content)

# Close Selenium browser
driver.quit()
print("JSON files downloaded successfully!")
