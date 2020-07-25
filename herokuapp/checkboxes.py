from selenium import webdriver
import os

# define chromedriver path
chromedriver_path = os.path.abspath('../../drivers') + '\chromedriver_win32\chromedriver.exe'

# create a chrome (driver)
driver = webdriver.Chrome('C:/Selenium/chromedriver.exe')

# Open portal and maximize window
driver.get("https://the-internet.herokuapp.com/checkboxes")
driver.maximize_window()

#find which checkbox is already selected and print
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
i=1
for checkbox in checkboxes:
    if checkbox.is_selected():
        print("Checkbox", i, "is selected")
    else:
        print("Checkbox", i, "is not selected")
    i += 1

#check all checkboxes and validate
for checkbox in checkboxes:
    if checkbox.is_selected() == False:
        checkbox.click()

i=1
for checkbox in checkboxes:
    if checkbox.is_selected():
        print("Checkbox", i, "is selected")
    else:
        print("Checkbox", i, "is not selected")
    i += 1

#uncheck all checkboxes and validate
for checkbox in checkboxes:
    if checkbox.is_selected() == True:
        checkbox.click()

i=1
for checkbox in checkboxes:
    if checkbox.is_selected():
        print("Checkbox", i, "is selected")
    else:
        print("Checkbox", i, "is not selected")
    i += 1

# Close driver
driver.close()