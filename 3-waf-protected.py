import undetected_chromedriver as uc 
import time 
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

user_email = os.getenv('USER_EMAIL_WAF')
user_password = os.getenv('USER_PASSWORD_WAF')

chromeOptions = uc.ChromeOptions() 
chromeOptions.headless = True 
chromeOptions.binary_location = '/usr/bin/chromium-browser' 
driver = uc.Chrome(use_subprocess=True, options=chromeOptions) 

driver.get("https://www.datacamp.com/users/sign_in")
time.sleep(10) # To let the login page load.

uname = driver.find_element(By.ID, "user_email") 
uname.send_keys(user_email) 
driver.find_element(By.CSS_SELECTOR, ".js-account-check-email").click() 
time.sleep(5)

passwordF = driver.find_element(By.ID, "user_password") 
passwordF.send_keys(user_password) 
driver.find_element(By.NAME, "commit").click()

driver.get("https://app.datacamp.com/learn") 
myName = driver.find_element(By.CLASS_NAME, "mfe-app-learn-hub-15alavv") 
myCourse = driver.find_element(By.CLASS_NAME, "mfe-app-learn-hub-1f1m67o") 
 
print("Profile Name: " + myName.get_attribute("innerHTML")) 
print("Course Enrolled: " + myCourse.get_attribute("innerHTML")) 
driver.close()

