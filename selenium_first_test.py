from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os


# define chromedriver path
chromedriver_path = os.path.abspath('../../drivers') + '\chromedriver_win32\chromedriver.exe'

# create a chrome (driver)
driver = webdriver.Chrome('C:/Selenium/chromedriver.exe')

# Open portal and maximize window
driver.get("https://duckduckgo.com/")
driver.maximize_window()

# Perform search
search_field = driver.find_element_by_id("search_form_input_homepage")
search_field.send_keys("python" + Keys.RETURN)

# Wait
sleep(1)

# Assertions on result page
assert "python" in driver.title
search_result_field = driver.find_element_by_id("search_form_input")
result_value = search_result_field.get_attribute("value")
assert "python" in result_value

result_links = driver.find_elements_by_class_name("result__a")
titles = [link.text for link in result_links]
matches = [t for t in titles if "python" in t.lower()]
print(matches)
assert len(matches) > 0


# Close driver
driver.close()
