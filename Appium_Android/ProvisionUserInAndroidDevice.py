import os
import unittest
from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ProvisionUser(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Nexus 7'
        desired_caps['app'] = 'C:\\Users\\pkumarasami\\Desktop\\ShoreTel\\Appium\\ra_dialer-android-40(116).apk'
        #desired_caps['appPackage'] = 'com.shoretel.RADialer'
        #desired_caps['appActivity'] = 'com.shoretel.RADialer.RADialer'
        desired_caps['udid'] = '4d00a5fed4941201'

        self.driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps)
        self.driver.implicitly_wait(80)
        

    def tearDown(self):
        self.driver.quit()

    def test_provisionuser(self):
        self.driver.find_element_by_name("Accept").click()
        self.driver.find_element_by_name("Yes").click()
        self.driver.find_element_by_id("com.shoretel.RADialer:id/router_edit").send_keys("10.198.128.113")
        self.driver.find_element_by_id("com.shoretel.RADialer:id/username_edit").send_keys("suser3")
        self.driver.find_element_by_id("com.shoretel.RADialer:id/password_edit").send_keys("123456")
        self.driver.find_element_by_id("com.shoretel.RADialer:id/provision_ok_btn").click()
        self.driver.find_element_by_id("com.shoretel.RADialer:id/mobilenum_edit").send_keys("9886867999")
        self.driver.find_element_by_id("com.shoretel.RADialer:id/provision_config_ok_btn").click()
        self.driver.find_element_by_id("android:id/button1").click()
        self.driver.find_element_by_id("com.shoretel.RADialer:id/button_dont_show_again").click()
        self.driver.find_element_by_id("com.shoretel.RADialer:id/img_home").click()
        self.driver.find_element_by_id("com.shoretel.RADialer:id/button_dont_show_again").click()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ProvisionUser)
    unittest.TextTestRunner(verbosity=2).run(suite)