import os
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome driver path and options
driver_path = "C:/Users/Pabitha/PycharmProjects/chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(driver_path)

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": r"C:\Users\Pabitha\PycharmProjects\sampletest\Selenium28\download_task_20_2b",  # Change to your desired download directory
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
})

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the labour.gov.in website
driver.get("https://labour.gov.in/")
time.sleep(4)

# Perform actions to navigate to the photo gallery
media_loc = driver.find_element(By.XPATH, '//*[@id="nav"]/li[10]/a')
actions = ActionChains(driver)
actions.move_to_element(media_loc).perform()
media_press = driver.find_element(By.XPATH, '//*[@id="nav"]/li[10]/ul/li/a')
media_press.click()
time.sleep(2)

more_info = driver.find_element(By.XPATH, "//*[@id='fontSize']/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/p/b/a").click()
time.sleep(5)

photo_gallery = driver.find_element(By.XPATH, "//*[@id='block-block-88']/ul/li[2]/strong/a").click()
time.sleep(5)

# Switch to the new window with the photo gallery
driver.switch_to.window(driver.window_handles[1])
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".views-field-field-image img")))

# Create a directory for downloaded photos if it doesn't exist
photo_folder = r"C:\Users\Pabitha\python prog\Photo gallery"
if not os.path.exists(photo_folder):
    os.makedirs(photo_folder)
time.sleep(5)

# Download the first 10 photos from the photo gallery
photos = driver.find_elements(By.CSS_SELECTOR, ".views-field-field-image img")[:10]
for index, photo in enumerate(photos):
    photo_url = photo.get_attribute('src')
    if not photo_url.startswith('http'):
        photo_url = "https://labour.gov.in" + photo_url  # Ensure the URL is absolute
    photo_response = requests.get(photo_url)
    with open(os.path.join(photo_folder, f"photo_{index + 1}.jpg"), 'wb') as file:
        file.write(photo_response.content)
    print(f"Downloaded photo {index + 1}")

print("Photos downloaded successfully.")

# Close the browser
driver.quit()
