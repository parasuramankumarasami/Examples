import os
import unittest
from appium import webdriver
from hotshot import ENTER
import time


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SearchContactNumberInTrueCaller(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['udid'] = 'TA07001FDL'
        #desired_caps['appPackage'] = 'com.whatsapp'
        #desired_caps['appActivity'] = 'com.whatsapp.HomeActivity'
        desired_caps['app'] = 'C:\\Users\\pkumarasami\\Downloads\\Truecaller_5.87.apk'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_search_contacts(self):
        self.driver.find_element_by_id("com.truecaller:id/searchEdit").click()
        self.driver.find_element_by_id("com.truecaller:id/search_field").send_keys("9449616660")
        self.driver.find_element_by_id("com.truecaller:id/search_field").send_keys(ENTER)
        time.sleep(20)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SearchContactNumberInTrueCaller)
    unittest.TextTestRunner(verbosity=2).run(suite)
