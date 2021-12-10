from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Remote(command_executor='http://localhost:9999',
                                desired_capabilities={'app': 'C:\\Program Files (x86)\\Microsoft Office\\Office15\\lync.exe'})
user = driver.find_element_by_class_name("NetUITextbox")
user.click()
user.send_keys("bb@shoretel.com")
user.send_keys(Keys.ENTER)
item = driver.find_element_by_class_name("NetUIListViewItem")
actionChains = ActionChains(driver)
actionChains.context_click(item).perform()
driver.find_element_by_class_name("NetUITextbox").clear()