from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# Set up Chrome options to download PDF files automatically
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": r"C:\Users\Pabitha\PycharmProjects\sampletest\Selenium28\download_pdf1",  # Change to your desired download directory
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
})
# Initialize the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
# Navigate to the webpage containing PDF links
driver.get("https://labour.gov.in/")
document_link =driver.find_element(By.LINK_TEXT,"Documents")
# '//ul[@class="menuItemCenter"]//li[4]/a'
actions=ActionChains(driver)
actions.move_to_element(document_link).perform()
monthly_report=driver.find_element(By.XPATH,'//*[@id="nav"]//li[7]//ul//li[2]/a').click()
# ActionChains(dri).move_to_element(monthly_report).click()
time.sleep(5)
# Find all links on the webpage
all_links = driver.find_elements(By.XPATH,"//tbody//a[contains(@href,'.pdf')]")
# Filter out PDF links
pdf_links = []
for link in all_links:
    href = link.get_attribute("href")
    if href and href.endswith(".pdf"):
        pdf_links.append(href)

# Download each PDF file
for pdf_link in pdf_links:
    driver.get(pdf_link)
    time.sleep(5)  # Wait for the download to complete (adjust as needed)

# Close the browser
driver.quit()
