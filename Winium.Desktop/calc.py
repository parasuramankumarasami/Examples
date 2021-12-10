from selenium import webdriver
import time
driver = webdriver.Remote(
    command_executor='http://localhost:9999',
    desired_capabilities={
        #"debugConnectToRunningApp": 'false',
        #"app": r"C:/windows/system32/calc.exe"
        'app':"C:\\Program Files (x86)\\Microsoft Office\\Office15\\OUTLOOK.EXE"
    })

#window = driver.find_element_by_class_name('CalcFrame') 
#menu = window.find_element_by_id('MenuBar').find_element_by_name('View')

#menu.click()
#view_menu_item.find_element_by_class_name("Scientific").click()

#view_menu_item.click()
#view_menu_item.find_element_by_name("History").click()

#window.find_element_by_id('132').click()
#window.find_element_by_id('93').click()
#window.find_element_by_id('134').click()
#window.find_element_by_id('97').click()
#window.find_element_by_id('138').click()
#window.find_element_by_id('121').click()
#driver.find_element_by_id('132').click()
time.sleep(20)
driver.find_element_by_name("RE: Review of automated mobility API's and Scripts").click()
driver.close()
