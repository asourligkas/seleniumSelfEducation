from selenium import webdriver
import os
from selenium.webdriver.support.ui import Select

# define chromedriver path
chromedriver_path = os.path.abspath('../../drivers') + '\chromedriver_win32\chromedriver.exe'

# create a chrome (driver)
driver = webdriver.Chrome('C:/bin/chromedriver.exe')

# Open portal and maximize window
driver.get("https://the-internet.herokuapp.com/dropdown")
driver.maximize_window()

#Find and print selected option
select = Select(driver.find_element_by_id("dropdown"))
print(select.first_selected_option.text," is selected")

#Select using text and validate
select.select_by_visible_text("Option 1")
print(select.first_selected_option.text," is selected")

#Select using value and validate
select.select_by_value("2")
print(select.first_selected_option.text," is selected")

# Close driver
driver.close()