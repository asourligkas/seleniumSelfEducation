from selenium import webdriver
from time import sleep
import os

# define chromedriver path
chromedriver_path = os.path.abspath('../../drivers') + '\chromedriver_win32\chromedriver.exe'

# create a chrome (driver)
driver = webdriver.Chrome('C:/bin/chromedriver.exe')

# Open portal and maximize window
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()

#Select abtesting option on list
ab_testing_link_xpath = driver.find_element_by_xpath("//a[@href='/abtest']")
# ab_testing_link_linktext = driver.find_element_by_link_text("A/B Testing") alternative way
ab_testing_link_xpath.click()

# Wait
sleep(1)

# Assertions on result page

#paragraph_text = driver.find_element_by_class_name("example")

header_text = driver.find_element_by_xpath("//div[@class='example']/h3").text
expected_header_1 = "A/B Test Variation 1"
expected_header_2 = "A/B Test Control"
#actual header is one of the two expected
assert header_text in [expected_header_1,expected_header_2]

main_text = driver.find_element_by_xpath("//div[@class='example']/p").text
expected_text = "Also known as split testing. This is a way in which businesses are able to simultaneously test and learn different versions of a page to see which text and/or functionality works best towards a desired outcome (e.g. a user action such as a click-through)."
assert expected_text == main_text

# Close driver
driver.close()