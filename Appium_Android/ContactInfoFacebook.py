import os
import unittest
from appium import webdriver


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ContactInfoFacebook(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        #desired_caps['udid'] = 'TA07001FDL'
        desired_caps['appPackage'] = 'com.facebook.katana'
        desired_caps['appActivity'] = 'com.facebook.katana.LoginActivity'
        #desired_caps['app'] = 'C:\\Users\\pkumarasami\\Desktop\\ShoreTel\\Selenium\sdk\\platform-tools\\WhatsApp.apk'
        self.driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self):
        self.driver.find_element_by_id("com.facebook.katana:id/bookmarks_tab").click()
        self.driver.find_element_by_id("com.facebook.katana:id/bookmarks_tab").click()
        self.driver.find_element_by_id("com.whatsapp:id/registration_phone").send_keys("12345")
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactInfoFacebook)
    unittest.TextTestRunner(verbosity=2).run(suite)
