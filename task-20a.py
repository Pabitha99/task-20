import os
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
driver_path="C:/Users/Pabitha/PycharmProjects/chromedriver.exe"
os.environ["PATH"] += os.pathsep+os.path.dirname(driver_path)
# Create a ChromeOptions object
chrome_options = Options()
# Add experimental option
chrome_options.add_experimental_option("detach", True)
# Initialize the WebDriver with ChromeOptions
chr_driver = webdriver.Chrome(options=chrome_options)
chr_driver.get("https://www.cowin.gov.in/")
faq_ele=chr_driver.find_element(By.XPATH,'//ul[@class="menuItemCenter"]//li[4]/a').click()
print(chr_driver.title)
time.sleep(3)
partner_ele=chr_driver.find_element(By.XPATH,'//ul[@class="menuItemCenter"]//li[5]/a').click()
time.sleep(3)
print(chr_driver.title)
# chr_driver.close()
time.sleep(5)
chr_driver.switch_to.window(chr_driver.window_handles[2])
chr_driver.close()
chr_driver.switch_to.window(chr_driver.window_handles[1])
chr_driver.close()






