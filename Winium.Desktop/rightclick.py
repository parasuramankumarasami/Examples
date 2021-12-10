from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.touch_actions import TouchActions

try:
    driver = webdriver.Remote(command_executor='http://localhost:9999',
                                desired_capabilities={'app': 'C:\\Program Files (x86)\\Microsoft Office\\Office15\\lync.exe'})
  
    user = driver.find_element_by_class_name("NetUITextbox")
    user.click()
    user.send_keys("AdSingh@shoretel.com")
    name_list = driver.find_element_by_class_name("NetUIListViewItem")
    #ActionChains(driver).double_click(name_list).perform()
    ActionChains(driver).context_click(name_list).perform()
    
    menu = driver.find_element_by_class_name("NetUIToolWindow")
    menu.find_element_by_name("Shoretel Call").click()
    driver.quit()  
except:
    print ("error")
    raise 
