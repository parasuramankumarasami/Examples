import os
import unittest
from appium import webdriver
import time


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class AudioCall(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Moto G'
        desired_caps['app'] = PATH(
            'C:\\Users\\pkumarasami\\Desktop\\ShoreTel\\Appium\\ra_dialer-android-40(116).apk'
        )
#        desired_caps['appPackage'] = 'com.example.android.contactmanager'
#        desired_caps['appActivity'] = '.ContactManager'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(10)
        

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self):
        self.driver.find_element_by_id("com.shoretel.RADialer:id/digits").send_keys("1806")
        self.driver.find_element_by_id("com.shoretel.RADialer:id/dialButton").click()
        
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AudioCall)
    unittest.TextTestRunner(verbosity=2).run(suite)