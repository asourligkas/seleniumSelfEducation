from selenium import webdriver
from selenium.webdriver import ActionChains
import os

# define chromedriver path
chromedriver_path = os.path.abspath('../../drivers') + '\chromedriver_win32\chromedriver.exe'

# create a chrome (driver)
driver = webdriver.Chrome('C:/Selenium/chromedriver.exe')

# Open portal and maximize window
driver.get("https://the-internet.herokuapp.com/context_menu")
driver.maximize_window()

# find context menu and right-click on it
actionChains = ActionChains(driver)
actionChains.context_click(driver.find_element_by_id("hot-spot")).perform()

# navigate to alert and click ok on it
alert = driver.switch_to.alert
print("Alert shows message: " + alert.text)
alert.accept()

# Close driver
driver.close()