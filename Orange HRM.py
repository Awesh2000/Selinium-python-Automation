
from selenium import webdriver
import time


driver = webdriver.Chrome('E:/program files/chromedriver_win32/chromedriver.exe')

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_xpath("//input[@id = 'txtUsername']").send_keys('Admin')

driver.find_element_by_xpath("//input[@id = 'txtPassword']").send_keys('admin123')

driver.find_element_by_xpath("//input[@id = 'btnLogin']").click()
'''
driver.find_element_by_xpath("//a[@id = 'menu_admin_viewAdminModule']").click()

driver.find_element_by_xpath("//input[@id = 'searchSystemUser_userName']").send_keys("Admin")

driver.find_element_by_xpath("//select[@id = 'searchSystemUser_userType']").click()

driver.find_element_by_xpath("//option[text() = 'Admin']").click()

driver.find_element_by_xpath("//input[@id = 'searchSystemUser_employeeName_empName']").send_keys('Paul Colling Walker')

driver.find_element_by_xpath("//option[text() = 'Admin']").click()

driver.find_element_by_xpath("//select[@id = 'searchSystemUser_status']").click()

driver.find_element_by_xpath("//option[text() = 'Enabled']").click()

driver.find_element_by_xpath("//input[@id = 'searchBtn']").click()

#--------------------------------------------PIM SECTION--------------------------------------
driver.find_element_by_xpath("//a[@id = 'menu_pim_viewPimModule']").click()

driver.find_element_by_xpath("//input[@id = 'empsearch_employee_name_empName']").send_keys('Lisa Andrews')

#driver.find_element_by_xpath("//li[@class = 'ac_even ac_over']").click() ##

driver.find_element_by_xpath("//input[@id = 'empsearch_id']").send_keys('Mahadev_2000')

driver.find_element_by_xpath("//select[@id = 'empsearch_employee_status']").click()

driver.find_element_by_xpath("//option[text() = 'Full-Time Permanent']").click()

driver.find_element_by_xpath("//select[@id = 'empsearch_termination']").click()

driver.find_element_by_xpath("//option[text() = 'Current and Past Employees']").click()

driver.find_element_by_xpath("//input[@id = 'empsearch_supervisor_name']").send_keys('Fiona Grace')

#driver.find_element_by_xpath("//strong[text() = 'Fiona Grace']").click()

driver.find_element_by_xpath("//select[@id = 'empsearch_job_title']").click()

driver.find_element_by_xpath("//option[text() = 'All']").click()

driver.find_element_by_xpath("//select[@id = 'empsearch_sub_unit']").click()

driver.find_element_by_xpath("//option[text() = 'All']").click()

driver.find_element_by_xpath("//input[@id = 'searchBtn']").click()

#----------------------------------(LEAVE SECTION)------------------------------------------------

driver.find_element_by_xpath("//a[@id = 'menu_leave_viewLeaveModule']").click()

driver.find_element_by_xpath("//input[@class = 'calendar hasDatepicker']").click()

driver.find_element_by_xpath("//select[@class = 'ui-datepicker-month']").click()

driver.find_element_by_xpath("//option[text()= 'Mar']").click()

driver.find_element_by_xpath("//a[text()= '31']").click()

driver.find_element_by_xpath("//input[@id= 'calToDate']").click()

driver.find_element_by_xpath("//select[@class= 'ui-datepicker-month']").click()

driver.find_element_by_xpath("//option[text()= 'Jun']").click()

driver.find_element_by_xpath("//a[text()= '9']").click()

driver.find_element_by_xpath("//input[@value='1']")

driver.find_element_by_xpath("//input[@id='leaveList_txtEmployee_empName']").send_keys('Fiona Grace')

driver.find_element_by_xpath("//select[@id = 'leaveList_cmbSubunit']").click()

driver.find_element_by_xpath("//option[@value = '4']").click()

driver.find_element_by_xpath("//input[@value = 'on']").click()

driver.find_element_by_xpath("//input[@id = 'btnSearch']").click()

#--------------------------------(Time)--------------------------------------------------
'''
driver.find_element_by_xpath("//a[@id = 'menu_time_viewTimeModule']").click()

driver.find_element_by_xpath("//input[@id = 'employee']").click()

driver.find_element_by_xpath("//input[@id = 'employee']").send_keys("Sara Tencrady")

driver.find_element_by_xpath("//input[@id = 'btnView']").click()

driver.find_element_by_xpath("//input[@id = 'btnSubmit']").click()

driver.find_element_by_xpath("//input[@id = 'btnEdit']").click()

#------------------------------------------------(recruitment)-----------------------------

driver.find_element_by_xpath("//a[@id = 'menu_recruitment_viewRecruitmentModule']").click()

driver.find_element_by_xpath("//select[@id = 'candidateSearch_jobTitle']").click()

driver.find_element_by_xpath("//option[@value = '3']").click()

#driver.find_element_by_xpath("//input[@id = 'btnSubmit']").click()

#driver.find_element_by_xpath("//input[@id = 'btnSubmit']").click()

#driver.find_element_by_xpath("//input[@id = 'btnSubmit']").click()

#driver.find_element_by_xpath("//input[@id = 'btnSubmit']").click()

#driver.find_element_by_xpath("//input[@id = 'btnSubmit']").click()
time.sleep(8)
driver.close()