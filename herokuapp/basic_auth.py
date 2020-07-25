from selenium import webdriver
import os

# define chromedriver path
chromedriver_path = os.path.abspath('../../drivers') + '\chromedriver_win32\chromedriver.exe'

# create a chrome (driver)
driver = webdriver.Chrome('C:/Selenium/chromedriver.exe')

# Open portal and maximize window
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()

#Select add/remove elements option on list
basic_auth_link_xpath = driver.find_element_by_xpath("//a[@href='/basic_auth']")
basic_auth_link_linktext = driver.find_element_by_link_text("Basic Auth")
basic_auth_link_linktext.click()

#trick to authenticate immediately
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
header_text = driver.find_element_by_xpath("//div[@class='example']/h3").text
expected_header = "Basic Auth"
assert expected_header == header_text

# Close driver
driver.close()
# Is there a better way?
