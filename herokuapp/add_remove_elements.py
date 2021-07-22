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

#Select add/remove elements option on list
add_remove_link_xpath = driver.find_element_by_xpath("//a[@href='/add_remove_elements/']")
# add_remove_link_linktext = driver.find_element_by_link_text("Add/Remove Elements") alternative way
add_remove_link_xpath.click()

#locate and click add button
add_button = driver.find_element_by_xpath('//button[text()="Add Element"]')
# add_button = driver.find_element_by_xpath('//button[@onclick="addElement()"]') alternative way
add_button.click()
sleep(0.5)

#validate one delete button exists and then delete it
delete_buttons = driver.find_elements_by_xpath('//button[text()="Delete"]')
assert len(delete_buttons) == 1
delete_buttons[0].click()
sleep(0.5)

#press add 5 more times
count = 1
while count < 6:
    add_button.click()
    delete_buttons = driver.find_elements_by_xpath('//button[text()="Delete"]')
    assert len(delete_buttons) == count
    count +=1
    # Wait
    sleep(0.3)

#delete one by one
count = 5
while count > 0:
    delete_buttons[count-1].click()
    delete_buttons = driver.find_elements_by_xpath('//button[text()="Delete"]')
    count -=1
    assert len(delete_buttons) == count
    # Wait
    sleep(0.3)

# Close driver
driver.close()