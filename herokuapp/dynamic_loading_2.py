from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# define chromedriver path
chromedriver_path = os.path.abspath('../../drivers') + '\chromedriver_win32\chromedriver.exe'

# create a chrome (driver)
driver = webdriver.Chrome('C:/Selenium/chromedriver.exe')

# Open portal and maximize window
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
driver.maximize_window()

#assert correct page and element "finish" is not present
assert "Example 2: Element rendered after the fact" == driver.find_element_by_xpath("//div[@class='example']/h4").text
assert not len(driver.find_elements_by_id("finish"))

#click on start and assert element "finish" is visible
driver.find_element_by_xpath("//div[@id='start']/button").click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "finish")))
print("Displayed message: ", driver.find_element_by_id("finish").text)

# Close driver
driver.close()