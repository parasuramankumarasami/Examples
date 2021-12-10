from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
try:
    driver = webdriver.Remote(command_executor='http://localhost:9999',
                                desired_capabilities={'app': 'C:\\Program Files (x86)\\Microsoft Office\\Office15\\lync.exe'})
  
    time.sleep(10)
    name_list = driver.find_element_by_id("btnCall")
    #ActionChains(driver).double_click(name_list).perform()
    ActionChains(driver).move_to_element(name_list).perform()
    
    
    
except:
    print ("error")
    raise 



