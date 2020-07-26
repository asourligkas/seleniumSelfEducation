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
driver.get("https://the-internet.herokuapp.com/dynamic_controls")
driver.maximize_window()

# Validate checkbox exists and input field not enabled
checkbox_present = len(driver.find_elements_by_xpath("//input[@type='checkbox']")) > 0
if checkbox_present:
    print("checkbox exists!")
    assert "Remove" == driver.find_element_by_xpath("//form[@id='checkbox-example']/button").text
else:
    print("checkbox deleted")
    assert "Add" == driver.find_element_by_xpath("//form[@id='checkbox-example']/button").text

input_disabled = driver.find_element_by_xpath("//input[@type='text']").get_attribute("disabled")
if not input_disabled:
    print("input field is enabled")
    assert "Disable" == driver.find_element_by_xpath("//form[@id='input-example']/button").text
else:
    print("input field is disabled")
    assert "Enable" == driver.find_element_by_xpath("//form[@id='input-example']/button").text

# delete checkbox and validate
driver.find_element_by_xpath("//form[@id='checkbox-example']/button").click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//form[@id='checkbox-example']/p")))
checkbox_present = len(driver.find_elements_by_xpath("//input[@type='checkbox']")) > 0
if checkbox_present:
    print("checkbox exists!")
    assert "Remove" == driver.find_element_by_xpath("//form[@id='checkbox-example']/button").text
else:
    print("checkbox deleted")
    assert "Add" == driver.find_element_by_xpath("//form[@id='checkbox-example']/button").text
    assert "It's gone!" == driver.find_element_by_xpath("//form[@id='checkbox-example']/p").text

# add checkbox again and validate
driver.find_element_by_xpath("//form[@id='checkbox-example']/button").click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox']")))
checkbox_present = len(driver.find_elements_by_xpath("//input[@type='checkbox']")) > 0
if checkbox_present:
    print("checkbox exists!")
    assert "Remove" == driver.find_element_by_xpath("//form[@id='checkbox-example']/button").text
    assert "It's back!" == driver.find_element_by_xpath("//form[@id='checkbox-example']/p").text
else:
    print("checkbox deleted")
    assert "Add" == driver.find_element_by_xpath("//form[@id='checkbox-example']/button").text
    assert "It's gone!" == driver.find_element_by_xpath("//form[@id='checkbox-example']/p").text

# enable input field and validate
driver.find_element_by_xpath("//form[@id='input-example']/button").click()
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']")))
input_disabled = driver.find_element_by_xpath("//input[@type='text']").get_attribute("disabled")
if not input_disabled:
    print("input field is enabled")
    assert "Disable" == driver.find_element_by_xpath("//form[@id='input-example']/button").text
    assert "It's enabled!" == driver.find_element_by_xpath("//form[@id='input-example']/p").text
else:
    print("input field is disabled")
    assert "Enable" == driver.find_element_by_xpath("//form[@id='input-example']/button").text

# disable input field and validate
driver.find_element_by_xpath("//form[@id='input-example']/button").click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//form[@id='input-example']/input[@disabled='']")))
input_disabled = driver.find_element_by_xpath("//input[@type='text']").get_attribute("disabled")
if not input_disabled:
    print("input field is enabled")
    assert "Disable" == driver.find_element_by_xpath("//form[@id='input-example']/button").text
    assert "It's enabled!" == driver.find_element_by_xpath("//form[@id='input-example']/p").text
else:
    print("input field is disabled")
    assert "Enable" == driver.find_element_by_xpath("//form[@id='input-example']/button").text
    assert "It's disabled!" == driver.find_element_by_xpath("//form[@id='input-example']/p").text

# Close driver
driver.close()