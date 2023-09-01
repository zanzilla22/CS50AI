from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time, os

email = "externaluse22@gmail.com"
password = "P0keb@11"

inp_title = "This is a title."
inp_description = "This is a description."
inp_phoneNumber = "1234567899"
inp_images = [
    "testImage1",
    "testImage2",
]


# Initialize the web driver (make sure you have the driver installed)
driver = webdriver.Chrome()  # You can use another driver if needed

# Step 1: Go to the Kijiji post-ad page


driver.get("https://www.kijiji.ca/p-post-ad.html?categoryId=87&adTitle=")
try:
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
except TimeoutException:
    print("Element with ID 'username' not found within 10 seconds.")
    driver.quit()

# Step 2: Perform login
# Input your email address
email_input = driver.find_element(By.ID, "username")
email_input.send_keys(email)

# Input your password
password_input = driver.find_element(By.ID, "password")
password_input.send_keys(password)

# Click the login button
login_button = driver.find_element(By.ID, "login-submit")
login_button.click()

# Step 3: After login, you should be redirected to another page
# Check the payment_s-cashless checkbox

try:
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "payment_s-cashless"))
    )
except TimeoutException:
    print("Element with ID 'payment_s-cashless' not found within 10 seconds.")
    driver.quit()

cashless_checkbox = driver.find_element(By.ID, "payment_s-cashless")
label_element = driver.find_element(By.XPATH, "//label[@for='payment_s-cashless']")

label_element.click()


# Input the ad_Title variable
ad_title_input = driver.find_element(By.ID, "postad-title")
ad_title = inp_title  # Replace with your ad title
ad_title_input.send_keys(ad_title)

# Input the ad_Description variable
ad_description_input = driver.find_element(By.ID, "pstad-descrptn")
ad_description = inp_description  # Replace with your ad description
ad_description_input.send_keys(ad_description)

# Input the ad_PhoneNumber variable
ad_phone_input = driver.find_element(By.ID, "PhoneNumber")
ad_phone = inp_phoneNumber  # Replace with your phone number
ad_phone_input.send_keys(ad_phone)

# Click the "Post Your Ad" button
# post_button = driver.find_element(By.CSS_SELECTOR, "button.button__primary-1681489609")
# post_button.click()

# file_input = driver.find_element(By.ID, 'html5_1h92cqkfo1b1t1t1qpmb144u1cqs3')
# for img in inp_images:
#     # uploadButton = driver.find_element(By.ID, "ImageUploadButton")
#     # uploadButton.click()
#
#     try:
#         file_input = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.ID, 'html5_1h92cqkfo1b1t1t1qpmb144u1cqs3'))
#         )
#     except TimeoutException:
#         print("File input element not found within 10 seconds.")
#         driver.quit()
#
#     # Replace 'image_path' with the path to the image you want to upload
#     image_path = 'path_to_image/image.jpg'
#
#     # Use send_keys to input the file path into the file input field
#     file_input.send_keys(image_path)


# Close the browser

time.sleep(5000)
driver.quit()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# browser = webdriver.Chrome()
# browser.get("https://wiki.ubuntu.com")
# time.sleep(3)
# element = browser.find_element(By.ID, "searchinput")
# element.send_keys("typing")
# print(element)
# time.sleep(3)
# browser.close()
