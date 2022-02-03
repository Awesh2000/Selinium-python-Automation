from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
search_str = input("Enter url or string you want to search").strip()

#search_str = search_str.replace(' ','+')

driver = webdriver.Chrome('E:/program files/chromedriver_win32/chromedriver.exe')

driver.get("https://www.google.com/")

search = driver.find_element_by_name('q')
search.send_keys(search_str)
search.send_keys(Keys.RETURN)
time.sleep(5)
driver.close()