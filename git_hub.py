from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('E:/program files/chromedriver_win32/chromedriver.exe')
driver.get("https://github.com/")

driver.find_element(by=By.XPATH, value= "//a[@class = 'HeaderMenu-link flex-shrink-0 no-underline']").click()

driver.find_element(by=By.XPATH, value= "//input[@id = 'login_field']").send_keys('Awesh2000')

driver.find_element(by=By.XPATH, value= "//input[@id = 'password']").send_keys('Mahadev@4843')

driver.find_element(by=By.XPATH, value= "//input[@value = 'Sign in']").click()

driver.find_element(by=By.XPATH, value= "(//summary[@class = 'Header-link'])[2]").click()

driver.find_element(by=By.XPATH, value= "(//a[@class='dropdown-item'])[7]").click()
