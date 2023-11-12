print("Start")

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://trytestingthis.netlify.app/")

driver.maximize_window()
#print(driver.current_window_handle)
time.sleep(2)
# driver.implicitly_wait(5)


print("WebElements")
First_name = driver.find_element(By.XPATH, "//input[@id='fname']")
Last_name = driver.find_element(By.XPATH, "//input[@name='lname']")
# nameField_signup = driver.find_element(By.XPATH, "//input[@name='name']")
# emailField_signup = driver.find_element(By.XPATH, "//input[@name='email' and @data-qa ='signup-email']")
# signup_button = driver.find_element(By.XPATH, "// button[ @ data - qa = 'signup-button']")
# //option[@value='Vanilla']
# //*[text()=' Signup / Login']


print("Actions1")
# First_name.click()
First_name.clear()
First_name.send_keys("aaaaaaAAegr123123")
time.sleep(2)

print("Actions2")
# First_name.click()
Last_name.clear()
Last_name.send_keys("zzZZZgbrtgher213234")
time.sleep(2)

#
# actual_URL = driver.current_url
#
# if actual_URL == "https://automationexercise.com/login":
#     assert True
# else:
#     assert False
#
# nameField_signup = driver.find_element(By.XPATH, "//input[@name='name']")
# nameField_signup.clear()
# nameField_signup.send_keys("abc")
# time.sleep(2)
#
# emailField_signup = driver.find_element(By.XPATH, "//input[@name='email' and @data-qa ='signup-email']")
# emailField_signup.clear()
# emailField_signup.send_keys("acb@a.com")
# time.sleep(2)
#
# signup_button = driver.find_element(By.XPATH, " //button[@data-qa='signup-button']']")
# signup_button.click()
# time.sleep(2)
#


