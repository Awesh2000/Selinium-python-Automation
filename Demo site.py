from selenium import webdriver
import time
from faker import Faker
from selenium.webdriver.common.by import By
fake = Faker()

driver = webdriver.Chrome('E:/program files/chromedriver_win32/chromedriver.exe')

driver.get("https://demo.guru99.com/test/newtours/")

user_name = fake.email()
password = fake.password()
#-----------------------------------REGISTER----------------------------------------------
driver.find_element(by=By.XPATH, value= "//a[text() = 'REGISTER']").click()

driver.find_element(by=By.XPATH, value= "//input[@name = 'firstName']").send_keys(fake.first_name())

driver.find_element(by=By.XPATH, value= "//input[@name = 'lastName']").send_keys(fake.last_name())
time.sleep(2)
driver.find_element(by=By.XPATH, value= "//input[@name = 'phone']").send_keys(fake.phone_number())
time.sleep(2)
driver.find_element(by=By.XPATH, value= "//input[@name = 'userName']").send_keys(user_name)
time.sleep(2)
driver.find_element(by=By.XPATH, value= "//input[@name = 'city']").send_keys(fake.city())
time.sleep(2)
driver.find_element(by=By.XPATH, value= "//input[@name = 'address1']").send_keys(fake.address())
time.sleep(2)

driver.find_element_by_xpath("//input[@name = 'state']").send_keys(fake.state())

driver.find_element_by_xpath("//input[@name = 'postalCode']").send_keys(fake.text())

driver.find_element_by_xpath("//input[@id = 'email']").send_keys(user_name)
driver.find_element_by_xpath("//input[@name = 'password']").send_keys(password)

driver.find_element_by_xpath("//input[@name = 'confirmPassword']").send_keys(password)

time.sleep(10)

#driver.find_element_by_xpath("//input[@name = 'submit']").click()


#driver.find_element_by_xpath("//a[text()= 'Home']").click()

#driver.find_element_by_xpath("//input[@name = 'userName']").send.keys(user_name)
#driver.find_element_by_xpath("//input[@name = 'password']").send.keys(password)


driver.close()