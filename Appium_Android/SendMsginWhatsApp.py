import os
import unittest
from appium import webdriver
import time

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SendMsginWhatsApp(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['udid'] = 'TA07001FDL'
        #desired_caps['appPackage'] = 'com.whatsapp'
        #desired_caps['appActivity'] = 'com.whatsapp.HomeActivity'
        desired_caps['app'] = 'C:\\Users\\pkumarasami\\Desktop\\ShoreTel\\Selenium\sdk\\platform-tools\\WhatsApp.apk'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_send_msg(self):
        self.driver.find_element_by_id("com.whatsapp:id/conversations_row_contact_name").click()
      
        self.driver.find_element_by_id("com.whatsapp:id/entry").send_keys("all")
        time.sleep(5)
        self.driver.find_element_by_id("com.whatsapp:id/send").click()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SendMsginWhatsApp)
    unittest.TextTestRunner(verbosity=2).run(suite)
