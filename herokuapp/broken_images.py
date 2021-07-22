from selenium import webdriver
import requests
import os

# define chromedriver path
chromedriver_path = os.path.abspath('../../drivers') + '\chromedriver_win32\chromedriver.exe'

# create a chrome (driver)
driver = webdriver.Chrome('C:/bin/chromedriver.exe')

# Open portal and maximize window
driver.get("https://the-internet.herokuapp.com/broken_images")
driver.maximize_window()

#find broken images
images = driver.find_elements_by_css_selector("img")

for image in images:
    print(image.get_attribute("src"))
    r = requests.get(image.get_attribute("src"))
    print(r.status_code)
    if r.status_code != 200:
        print(image.get_attribute("src"), "not available!")

# Close driver
driver.close()