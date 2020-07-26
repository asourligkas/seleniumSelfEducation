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
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

# Click login and validate error [user & pass blank]
login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()
#Den mou doulevei xwris asteraki to classname, giati?
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@class='flash error']")))
print("Error message: ",driver.find_element_by_xpath("//*[@class='flash error']").text)
assert "Your username is invalid!" in driver.find_element_by_xpath("//*[@class='flash error']").text

# Click login and validate error [user correct & pass blank]
driver.find_element_by_id("username").send_keys("tomsmith")
#xreiazetai na ksanavrw to koumpi, yparxei alternative way?
login_button1 = driver.find_element_by_xpath("//button[@type='submit']")
login_button1.click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@class='flash error']")))
print("Error message: ",driver.find_element_by_xpath("//*[@class='flash error']").text)
assert "Your password is invalid!" in driver.find_element_by_xpath("//*[@class='flash error']").text

# Click login and validate error [user correct & pass wrong]
driver.find_element_by_id("username").send_keys("tomsmith")
driver.find_element_by_name("password").send_keys("12345")
#xreiazetai na ksanavrw to koumpi, yparxei alternative way?
login_button2 = driver.find_element_by_xpath("//button[@type='submit']")
login_button2.click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@class='flash error']")))
print("Error message: ",driver.find_element_by_xpath("//*[@class='flash error']").text)
assert "Your password is invalid!" in driver.find_element_by_xpath("//*[@class='flash error']").text

# Login successful
driver.find_element_by_id("username").send_keys("tomsmith")
driver.find_element_by_name("password").send_keys("SuperSecretPassword!")
#xreiazetai na ksanavrw to koumpi, yparxei alternative way?
login_button3 = driver.find_element_by_xpath("//button[@type='submit']")
login_button3.click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@class='flash success']")))
print("Success login message: ",driver.find_element_by_xpath("//*[@class='flash success']").text)
assert "You logged into a secure area!" in driver.find_element_by_xpath("//*[@class='flash success']").text
assert "Welcome to the Secure Area. When you are done click logout below." in driver.find_element_by_class_name("subheader").text

#Logout successful
driver.find_element_by_xpath('//a[@href="/logout"]').click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@class='flash success']")))
print("Success logout message: ",driver.find_element_by_xpath("//*[@class='flash success']").text)
assert "Login Page" in driver.find_element_by_xpath("//*[@class='example']/h2").text

# Close driver
driver.close()