from selenium import webdriver
import os

# define chromedriver path
chromedriver_path = os.path.abspath('../../drivers') + '\chromedriver_win32\chromedriver.exe'

# create a chrome (driver)
driver = webdriver.Chrome('C:/Selenium/chromedriver.exe')

# Open portal and maximize window
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#alert accept (only ok option available)
driver.find_element_by_xpath("//*[contains(text(), 'Click for JS Alert')]").click()
alert = driver.switch_to.alert
print("Alert shows message: " + alert.text)
alert.accept()
print(driver.find_element_by_id("result").text)
assert "You successfuly clicked an alert" == driver.find_element_by_id("result").text

#alert with ok and cancel
driver.find_element_by_xpath("//*[contains(text(), 'Click for JS Confirm')]").click()
alert = driver.switch_to.alert
print("Alert shows message: " + alert.text)
alert.accept()
print(driver.find_element_by_id("result").text)
assert "You clicked: Ok" == driver.find_element_by_id("result").text

driver.find_element_by_xpath("//*[contains(text(), 'Click for JS Confirm')]").click()
alert = driver.switch_to.alert
print("Alert shows message: " + alert.text)
alert.dismiss()
print(driver.find_element_by_id("result").text)
assert "You clicked: Cancel" == driver.find_element_by_id("result").text

#prompt alert
driver.find_element_by_xpath(".//button[contains(@onclick, 'jsPrompt()')]").click()
alert = driver.switch_to.alert
print("Alert shows message: " + alert.text)
alert.send_keys("TEST")
alert.accept()
print(driver.find_element_by_id("result").text)
assert "You entered: TEST" == driver.find_element_by_id("result").text

# Close driver
driver.close()