import os
import time
import requests
from zipfile import ZipFile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # Automatically manages ChromeDriver

# URL of the page containing the zip files
url = "https://www.ibge.gov.br/estatisticas/economicas/precos-e-custos/9258-indice-nacional-de-precos-ao-consumidor.html?=&t=downloads"

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no browser UI)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Automatically download and set up the WebDriver if not available
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Load the webpage
driver.get(url)

# Wait for the element containing the download links to load
wait = WebDriverWait(driver, 10)
downloads_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'jstree-children')))


#print(downloads_div.get_attribute('outerHTML') )

# Base directory to save the extracted files
base_dir = "C:/Users/sd74216/Desktop/Vpena/Python_excel_Automation/Datas"
os.makedirs(base_dir, exist_ok=True)

# Find all the <a> tags within the downloads section that contain .zip links
# Locate all ul elements inside the downloads_div
ul_elements = downloads_div.find_elements(By.TAG_NAME, 'i')

# Iterate through each ul element and print its HTML content
# for ul_element in ul_elements:

#print(ul_element.get_attribute('outerHTML'))


for link in ul_elements:
    print(link.text)
    zip_url = link.get_attribute('url')
    #print(zip_url)
#     if '.zip' in zip_url:
#         zip_name = os.path.basename(zip_url)
#         year_dir = os.path.join(base_dir, "2008")  # Adjust this to dynamically extract the year if needed
#         os.makedirs(year_dir, exist_ok=True)
#         zip_path = os.path.join(year_dir, zip_name)

#         # Download the zip file
#         print(f"Downloading {zip_name} from {zip_url}...")
#         zip_response = requests.get(zip_url)

#         # Save the zip file locally
#         with open(zip_path, 'wb') as f:
#             f.write(zip_response.content)

#         # Extract the zip file
#         print(f"Extracting {zip_name}...")
#         with ZipFile(zip_path, 'r') as zip_ref:
#             zip_ref.extractall(year_dir)

#         print(f"Finished processing {zip_name}.")

# # Close the WebDriver session
# driver.quit()

# print("All files have been downloaded and extracted.")
