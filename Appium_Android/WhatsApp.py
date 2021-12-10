import os
import unittest
from appium import webdriver


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class WhatsApp(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        #desired_caps['platformVersion'] = '8.1.0'
        desired_caps['deviceName'] = 'Android Emulator'
        #desired_caps['udid'] = 'FA6A60313917'
        desired_caps['appPackage'] = 'com.whatsapp'
        desired_caps['appActivity'] = 'com.whatsapp.HomeActivity'
        #desired_caps['app'] = 'C:\\Users\\pkumarasami\\Desktop\\ShoreTel\\Selenium\sdk\\platform-tools\\WhatsApp.apk'
        self.driver = webdriver.Remote('http://127.0.0.1:4733/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self):
        self.driver.find_element_by_id("com.whatsapp:id/eula_accept").click()
              
        self.driver.find_element_by_id("com.whatsapp:id/registration_phone").send_keys("12345")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WhatsApp)
    unittest.TextTestRunner(verbosity=2).run(suite)
