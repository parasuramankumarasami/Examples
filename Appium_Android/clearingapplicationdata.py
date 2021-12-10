import time
import os
import unittest
from appium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from appium.webdriver.common import touch_action

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class clearingappdata(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        #desired_caps['app'] = PATH('\\Users\\pjayaram\\Documents\\workspace\\Appium\\src\\RaDialer.ipa')
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = 'com.android.settings.GridSettings'
        #desired_caps['udid'] = '57a3a54ea16a6fe189a5fe59a0a8734995b3e205'

        self.driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self):
        self.driver.find_element_by_class_name("android.widget.Button").click()

        self.driver.find_element_by_id("android:id/search_src_text").send_keys("application manager")

        self.driver.find_element_by_id("com.android.settings:id/menuTitle").click()
        ele1 = self.driver.find_element_by_name("Android System WebView")
        ele2 = self.driver.find_element_by_name("Chrome")
        self.driver.scroll(ele1, ele2)
        TouchActions(self.driver).scroll(50, 600).perform()
        #self.driver.find_element_by_name("ShoreTel").click()
        #self.driver.find_element_by_id("com.android.settings:id/right_button").click()
        
        time.sleep(20)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(clearingappdata)
    unittest.TextTestRunner(verbosity=2).run(suite)
