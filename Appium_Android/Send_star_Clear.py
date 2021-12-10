import time
from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.2'
desired_caps['deviceName'] = 'Android Emulator'
#desired_caps['udid'] = 'TA07001FDL'
desired_caps['appPackage'] = 'com.whatsapp'
desired_caps['appActivity'] = 'com.whatsapp.HomeActivity'
#desired_caps['app'] = 'C:\\Users\\pkumarasami\\Desktop\\ShoreTel\\Selenium\sdk\\platform-tools\\WhatsApp.apk'
driver = webdriver.Remote('http://127.0.0.1:4733/wd/hub', desired_caps)
driver.implicitly_wait(30)
driver.find_element_by_id("com.whatsapp:id/menuitem_search").click()
driver.find_element_by_id("com.whatsapp:id/search_src_text").send_keys("a kind manager")
time.sleep(10)
driver.find_elements_by_id("com.whatsapp:id/conversations_row_contact_name")[0].click()
driver.find_element_by_id("com.whatsapp:id/entry").send_keys("Good Morning..!!!")
driver.find_element_by_id("com.whatsapp:id/send").click()
driver.find_element_by_xpath("//android.widget.ImageView[Index=\"2\"]").click()
driver.quit()