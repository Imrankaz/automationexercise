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
time.sleep(2)
# driver.implicitly_wait(5)

# driver.get("https://automationexercise.com/login")

print("WebElements")
signup_or_Login_button = driver.find_element(By.XPATH, " //*[text()=' Signup / Login']")
# nameField_signup = driver.find_element(By.XPATH, "//input[@name='name']")
# emailField_signup = driver.find_element(By.XPATH, "//input[@name='email' and @data-qa ='signup-email']")
# signup_button = driver.find_element(By.XPATH, "// button[ @ data - qa = 'signup-button']")




print("Actions")
signup_or_Login_button.click()
time.sleep(2)

actual_URL = driver.current_url

if actual_URL == "https://automationexercise.com/login":
    assert True
else:
    assert False

nameField_signup = driver.find_element(By.XPATH, "//input[@name='name']")
nameField_signup.clear()
nameField_signup.send_keys("abc")
time.sleep(2)

emailField_signup = driver.find_element(By.XPATH, "//input[@name='email' and @data-qa ='signup-email']")
emailField_signup.clear()
emailField_signup.send_keys("acb@a.com")
time.sleep(2)

signup_button = driver.find_element(By.XPATH, " //button[@data-qa='signup-button']']")
signup_button.click()
time.sleep(2)



