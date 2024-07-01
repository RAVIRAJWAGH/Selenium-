#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import os

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Function to create a directory if it doesn't exist
def create_directory(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

# Open Google Images
driver.get("https://www.google.com/imghp")
time.sleep(2)  # Give time for the page to load

# Search for "Serena Williams"
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Serena Williams')
search_box.send_keys(Keys.RETURN)
time.sleep(2)  # Give time for the search results to load

# Scroll down to load more images
for _ in range(5):  # Adjust the range for more/less images
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for the new images to load

# Find image elements
image_elements = driver.find_elements(By.CSS_SELECTOR, 'img.Q4LuWd')

# Create a directory to save images
create_directory(r"add your path here\serena_williams_images")
# Function to validate URLs
def is_valid_url(url):
    return url.startswith('http://') or url.startswith('https://')

# Download images
for i, img_elem in enumerate(image_elements):
    try:
        # Get the URL of the image
        img_url = img_elem.get_attribute('src') or img_elem.get_attribute('data-src')
        if img_url and is_valid_url(img_url):
            # Download and save the image
            img_data = requests.get(img_url).content
            with open(rf'add your path here/serena_williams_{i+1}.jpg', 'wb') as img_file:
                img_file.write(img_data)
                print("written")
        else:
            print(f"Skipping invalid URL for image {i+1}")
            continue
    except Exception as e:
        print(f"Could not download image {i+1}: {e}")

# Close the browser
driver.quit()


