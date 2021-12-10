from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.2'
desired_caps['deviceName'] = 'Nexus 7'
desired_caps['appPackage'] = 'com.shoretel.workspace'
desired_caps['appActivity'] = '.ui.activity.LoginActivity'
desired_caps['appWaitActivity'] = '.ui.activity.LoginActivity,.ui.activity.WorkspaceActivity'

#desired_caps['app'] = 'C:\\Users\\pkumar\\Downloads\\workspace-0.1.63-release.apk'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
ele = driver.find_element_by_id("com.shoretel.workspace:id/sign_in_email")
if ele.get_attribute("text") == "Sign-In with email":
    print("found match")
else:
    print("failed")
print(ele.get_attribute("text"))
driver.find_element_by_id("com.shoretel.workspace:id/sign_in_email").click()
username=driver.find_element_by_id("com.shoretel.workspace:id/login_email")
if username.get_attribute("text") == "email address's":
    print("found exact match")
else:
    print("not valid")
print(username.get_attribute("text"))
driver.find_element_by_id("com.shoretel.workspace:id/login_email").send_keys("scoblrtest1@cldc.shoretel.com")
driver.find_element_by_id("com.shoretel.workspace:id/login_server").send_keys("buddycloud.cldc.shoretel.com")
driver.find_element_by_id("com.shoretel.workspace:id/login_next").click()
driver.find_element_by_id("com.shoretel.workspace:id/login_password").send_keys("Shor1234")
driver.find_element_by_id("com.shoretel.workspace:id/login_sign_in").click()
time.sleep(2)
driver.find_element_by_id("com.shoretel.workspace:id/skip_introduction__btn").click()


