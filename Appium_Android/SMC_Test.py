import os
import unittest
import time
from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SMC_Test(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Nexus 7'
        #desired_caps['app'] = 'C:\\Users\\pkumarasami\\Desktop\\ShoreTel\\Appium\\ra_dialer-android-40(116).apk'
        desired_caps['appPackage'] = 'com.shoretel.RADialer'
        desired_caps['appActivity'] = 'com.shoretel.RADialer.ProvisionActivity'
        #desired_caps['udid'] = '4d00b23e4f04a0ed'

        self.driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps)
        self.driver.implicitly_wait(80)
        
        desired_cap = {}
        desired_cap['platformName'] = 'Android'
        desired_cap['platformVersion'] = '4.2'
        desired_cap['deviceName'] = 'Nexus 7'
        desired_cap['app'] = 'C:\\Users\\pkumarasami\\Desktop\\ShoreTel\\Appium\\ra_dialer-android-40(116).apk'
        #desired_cap['appPackage'] = 'com.shoretel.RADialer'
        #desired_cap['appActivity'] = 'com.shoretel.RADialer.RADialer'
        desired_cap['udid'] = '4d00a5fed4941201'

        #self.sam_driver = webdriver.Remote('http://127.0.0.1:4727/wd/hub', desired_cap)
        #self.sam_driver.implicitly_wait(80)
        

    def tearDown(self):
        self.driver.quit()

#     def test_1provisionuser(self):
#        
#         
#         self.driver.find_element_by_name("Accept").click()
#         self.driver.find_element_by_name("Yes").click()
#         self.driver.find_element_by_id("com.shoretel.RADialer:id/router_edit").send_keys("10.198.128.113")
#         self.driver.find_element_by_id("com.shoretel.RADialer:id/username_edit").send_keys("suser5")
#         self.driver.find_element_by_id("com.shoretel.RADialer:id/password_edit").send_keys("123456")
#         self.driver.find_element_by_id("com.shoretel.RADialer:id/provision_ok_btn").click()
#         self.driver.find_element_by_id("com.shoretel.RADialer:id/mobilenum_edit").send_keys("9886867999")
#         self.driver.find_element_by_id("com.shoretel.RADialer:id/provision_config_ok_btn").click()
#         self.driver.find_element_by_id("android:id/button1").click()
#         self.driver.find_element_by_id("com.shoretel.RADialer:id/button_dont_show_again").click()
#         self.driver.find_element_by_id("com.shoretel.RADialer:id/img_home").click()
#         self.driver.find_element_by_id("com.shoretel.RADialer:id/button_dont_show_again").click()
#         self.driver.find_element_by_name("Keypad").click()
#         
#         
#         self.sam_driver.find_element_by_name("Accept").click()
#         self.sam_driver.find_element_by_name("Yes").click()
#         self.sam_driver.find_element_by_id("com.shoretel.RADialer:id/router_edit").send_keys("10.198.128.113")
#         self.sam_driver.find_element_by_id("com.shoretel.RADialer:id/username_edit").send_keys("suser6")
#         self.sam_driver.find_element_by_id("com.shoretel.RADialer:id/password_edit").send_keys("123456")
#         self.sam_driver.find_element_by_id("com.shoretel.RADialer:id/provision_ok_btn").click()
#         self.sam_driver.find_element_by_id("com.shoretel.RADialer:id/mobilenum_edit").send_keys("9886867989")
#         self.sam_driver.find_element_by_id("com.shoretel.RADialer:id/provision_config_ok_btn").click()
#         self.sam_driver.find_element_by_id("android:id/button1").click()
#         self.sam_driver.find_element_by_id("com.shoretel.RADialer:id/button_dont_show_again").click()
#         self.sam_driver.find_element_by_id("com.shoretel.RADialer:id/img_home").click()
#         self.sam_driver.find_element_by_id("com.shoretel.RADialer:id/button_dont_show_again").click()
#         self.sam_driver.find_element_by_name("Keypad").click()
       
    def test_videocall(self):
        #self.driver.find_element_by_id("com.shoretel.RADialer:id/digits").send_keys("1027")
        #self.driver.find_element_by_id("com.shoretel.RADialer:id/videoButton").click()
        #self.sam_driver.find_element_by_name("Answer Video").click()
        #time.sleep(10)
        #self.driver.find_element_by_id("com.shoretel.RADialer:id/endButton").click()
        self.driver.find_element_by_name("Accept").click()
    
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SMC_Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
    