from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
FB_EMAIL = os.getenv("FB_EMAIL")
FB_PASSWORD = os.getenv("FB_PASSWORD")

# Setup WebDriver
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

# Login
email_input = driver.find_element(By.ID, "email")
password_input = driver.find_element(By.ID, "pass")
email_input.send_keys(FB_EMAIL)
password_input.send_keys(FB_PASSWORD)
password_input.send_keys(Keys.RETURN)

time.sleep(5)

# Post a status update
status_box = driver.find_element(By.XPATH, "//div[@aria-label='What's on your mind?']")
status_box.click()
time.sleep(2)

# Type message
message = "This is an automated post using Selenium!"
active_box = driver.switch_to.active_element
active_box.send_keys(message)
time.sleep(2)

# Post
buttons = driver.find_elements(By.XPATH, "//div[@aria-label='Post']")
for btn in buttons:
    if btn.is_displayed():
        btn.click()
        break

print("Post published successfully!")
time.sleep(5)
driver.quit()
