print("Start")

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://automationexercise.com/")

driver.maximize_window()
#print(driver.current_window_handle)
time.sleep(15)
# driver.implicitly_wait(5)



print("WebElements")